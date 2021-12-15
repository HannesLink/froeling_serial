from .agent_based_api.v1 import *

def discover_froeling_sensors(section):
    for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')
        if int(sensor_id) == 1:
            yield Service(item="Status")
        yield Service(item=desc)

def check_froeling_sensors(item, section):
    for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')
        if int(sensor_id) == 1 and item == "Status":
            yield Result(state=State.OK, summary=desc)
            return
        if desc == item:
            s = State.OK
            yield Result(
                state = s,
                summary = f"{total}"
            )
            return
    yield Result(state=State.CRIT, summary="No status message found")

def check_froeling_temps(item, section):
   for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')
        if desc == item:
            s = State.OK
            yield Result(
                state = s,
                summary = f"{total}"
            )

register.check_plugin(
    name="froeling",
    service_name="Fröling %s",
    discovery_function=discover_froeling_sensors,
    check_function=check_froeling_sensors,
)
