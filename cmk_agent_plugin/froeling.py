from .agent_based_api.v1 import *

def discover_froeling_status(section):
    yield Service()

def check_froeling_status(section):
    for line in section:
        desc, value, sensor_id, factor, unit, total = line[0].split(';')
        if int(sensor_id) == 1:
            yield Result(state=State.OK, summary=desc)
            return
    yield Result(state=State.CRIT, summary="No status message found")

register.check_plugin(
    name="froeling",
    service_name="Fröling Status",
    discovery_function=discover_froeling_status,
    check_function=check_froeling_status,
)
