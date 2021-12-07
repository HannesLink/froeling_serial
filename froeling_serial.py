#!/usr/bin/env python3
"""Fröling Python Module"""

import json
import re
import csv
import serial

class Froeling:
    """Read data from Fröling heating systems using serial communication"""
    sensors = None
    max_sensors = None
    filename = None

    def __init__(self, port):
        self.sensors = {}
        self.max_sensors = 1000
        self.filename = "/tmp/sensor_data.csv"
        self.ser = serial.Serial(port, 57600, timeout=1)
        self.ser.flushInput()

    def read_data(self):
        """Open serrial connection to Fröling system and store data in Class"""
        for i in range(0, self.max_sensors):
            try:
                ser_bytes = self.ser.readline()
                # Get rid of unwanted characters
                decoded_bytes = ser_bytes[1:len(ser_bytes)-2].decode("iso-8859-1")
            except serial.serialutil.SerialException as err:
                raise err

            # Split line into proper variables, skip the line if unpacking does not work
            try:
                desc, value, sensor_id, factor, unit = decoded_bytes.split(';')
            except ValueError as err:
                continue

            # Add sensor data to Fröling Class
            self.add_sensor(
                sensor_id.strip(),
                desc.strip(),
                value.strip(),
                factor.strip(),
                unit.strip()
            )

            # Check each sensor twice to prevent crooked reads
            # that sometimes happen at the beginning of serial transmission
            if i > self.counter*2:
                break

    def add_sensor(self, *sensordata):
        """Add data to sensors dict and do some cleanup/transformation of data"""
        mysensor_id = sensordata[0]
        mydesc = sensordata[1]
        myvalue = sensordata[2]
        myfactor = sensordata[3]
        myunit = sensordata[4]
        # Remove unwanted characters from Fröling status sensor data
        if int(mysensor_id) == 1:
            mydesc = re.sub('[^a-zA-Z0-9äüöÄÜÖß ]', '', mydesc)
            mydesc = mydesc.lstrip()
        # Replace blank spaces with underscore for checkmk for all Sensors except ID 1
        if int(mysensor_id) != 1:
            mydesc = mydesc.replace(" ", "_")
        # Try to compute a total if we have numbers, otherwise simply use myvalue
        try:
            mytotal = round(float(int(myvalue) / int(myfactor)),2)
        except ValueError:
            mytotal = myvalue
        # Add data to sensors dict
        self.sensors[mysensor_id] = {
            'sensor_id': mysensor_id,
            'desc': mydesc,
            'value': myvalue,
            'factor': myfactor,
            'unit': myunit,
            'total': mytotal,
            'output': str(mytotal) + myunit,
        }

    def __str__(self):
        """Generate JSON output for printing"""
        return json.dumps(self.output_array(),ensure_ascii=False, sort_keys=True, indent=4)

    def __repr__(self):
        """Generate JSON output for machine reading"""
        return json.dumps(self.output_array(),ensure_ascii=False, sort_keys=True)

    def output_array(self):
        """Generate a sorted ourput array"""
        return sorted(list(self.sensors.values()), key=lambda d: int(d['sensor_id']))

    def output_csv(self):
        """Generate a CSV file for storing sensor data"""
        with open(self.filename,"w") as filehandle:
            writer = csv.writer(filehandle,delimiter=",")
            for line in self.output_array():
                writer.writerow([
                    line['desc'],
                    line['value'],
                    line['sensor_id'],
                    line['factor'],
                    line['unit'],
                    line['output']
                ])

    def output_cmk(self):
        """Generate output for checkmk host agent"""
        cmkout = ['<<<froeling>>>',]
        for line in self.output_array():
            cmkout.append(";".join([
                    line['desc'],
                    line['value'],
                    line['sensor_id'],
                    line['factor'],
                    line['unit'],
                    line['output']
                ]))
        return "\n".join(cmkout)

    @property
    def counter(self):
        """Count of active sensors"""
        return len(self.sensors)

def main():
    """Main Function"""
    # Create myfroeling object
    myfroeling = Froeling('/dev/ttyUSB0')

    # Read Serial data from Fröling
    myfroeling.read_data()

    # Generate CSV file
    myfroeling.output_csv()

    # Output checkmk hostagent data
    print(myfroeling.output_cmk())

if __name__ == "__main__":
    main()
