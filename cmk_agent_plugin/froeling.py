from .agent_based_api.v1 import *

def discover_froeling_sensors(section):
    for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')
        if int(sensor_id) == 1:
            yield Service(item="Status")
        else:
            yield Service(item=desc)

def check_froeling_sensors(item, section):
    for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')

        # Try to compute a float mytotal for metrics
        try:
            mytotal = round(float(int(value) / int(factor)),2)
        except ValueError:
            mytotal = value

        # Special Sensors
        if int(sensor_id) == 1 and item == "Status":
            yield Result(state=State.OK, summary=desc)
            return

        if int(sensor_id) == 99:
            if value == "Kein_Fehler":
                yield Result(state=State.OK, summary=value)
            else:
                yield Result(state=State.CRIT, summary=value)
            return

        # Sensors with numeric data
        if desc == item:
            s = State.OK
            yield Metric(
                desc,
                mytotal
            )
            yield Result(
                state = s,
                summary = f"{total}"
            )
            return
    yield Result(state=State.UNKNOWN, summary="No sensor data found")

register.check_plugin(
    name="froeling",
    service_name="Fröling %s",
    discovery_function=discover_froeling_sensors,
    check_function=check_froeling_sensors,
)
