from .agent_based_api.v1 import * # pylint: disable=wildcard-import,unused-wildcard-import
from cmk.base.check_legacy_includes.temperature import *  # pylint: disable=wildcard-import,unused-wildcard-import


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

def check_froeling_temp(item, params, section):
    for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')

        # Try to compute a float mytotal for metrics
        try:
            mytotal = round(float(int(value) / int(factor)),2)
        except ValueError:
            mytotal = value

        if desc == item:
            yield Metric(
                desc,
                mytotal
            )
            yield check_temperature(
                mytotal,
                params,
                "Fröling %s" % item
            )
            return
    yield Result(state=State.UNKNOWN, summary="No sensor data found")

register.check_plugin(
    name="froeling",
    service_name="Fröling %s",
    discovery_function=discover_froeling_sensors,
    check_function=check_froeling_sensors,
)

register.check_plugin(
    name="froeling_temps",
    service_name="Fröling %s",
    discovery_function=discover_froeling_sensors,
    check_function=check_froeling_temp,
    check_ruleset_name = "temperature",
    check_default_parameters={},
)

register.check_plugin(
    name="froeling_percent",
    service_name="Fröling %s",
    discovery_function=discover_froeling_sensors,
    check_function=check_froeling_sensors,
)
