from cmk.gui.plugins.metrics import perfometer_info, metric_info
#   __                _ _
#  / _|_ __ ___   ___| (_)_ __   __ _
# | |_| '__/ _ \ / _ \ | | '_ \ / _` |
# |  _| | | (_) |  __/ | | | | | (_| |
# |_| |_|  \___/ \___|_|_|_| |_|\__, |
#                               |___/
metric_info["Saugzug_Ist"] = {
    "title": _("Saugzug_Ist"),
    "help": _("UPM"),
    "unit": "rpm",
    "color": "35/a",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Saugzug_Ist",
    "half_value": 1000,
    "exponent": 10,
})

metric_info["Ansauggeschw."] = {
    "title": _("Ansauggeschwindigkeit"),
    "help": _("m/s"),
    "unit": "1/s",
    "color": "35/a",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Ansauggeschw.",
    "half_value": 2.0,
    "exponent": 0.2,
})

metric_info["Strom_Austrags"] = {
    "title": _("Stromaufnahme Austragschnecke"),
    "help": _("Ampere"),
    "unit": "a",
    "color": "35/a",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Strom_Austrags",
    "half_value": 1,
    "exponent": 0.5,
})

metric_info["HK_Pumpe_1"] = {
    "title": _("Keizkreis 1 Pumpe"),
    "help": _("Prozent"),
    "unit": "count",
    "color": "35/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["HK_Pumpe_1"],
    "total": 1,
})

metric_info["HK_Pumpe_2"] = {
    "title": _("Keizkreis 2 Pumpe"),
    "help": _("Prozent"),
    "unit": "count",
    "color": "35/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["HK_Pumpe_2"],
    "total": 1,
})

metric_info["Betriebsstunden"] = {
    "title": _("Betriebsstunden"),
    "help": _("Hours"),
    "unit": "count",
    "color": "35/a",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Betriebsstunden",
    "half_value": 10000,
    "exponent": 2,
})

#   __                _ _              _
#  / _|_ __ ___   ___| (_)_ __   __ _ | |_ ___ _ __ ___  _ __  ___
# | |_| '__/ _ \ / _ \ | | '_ \ / _` || __/ _ \ '_ ` _ \| '_ \/ __|
# |  _| | | (_) |  __/ | | | | | (_| || ||  __/ | | | | | |_) \__ \
# |_| |_|  \___/ \___|_|_|_| |_|\__, (_)__\___|_| |_| |_| .__/|___/
#                               |___/                   |_|

metric_info["Kesseltemp."] = {
    "title": _("Kesseltemperatur"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Kesseltemp.",
    "half_value": 50.0,
    "exponent": 1.2,
})

metric_info["Abgastemp."] = {
    "title": _("Abgastemperatur"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Abgastemp.",
    "half_value": 100.0,
    "exponent": 1.2,
})

metric_info["Abgastemp_S"] = {
    "title": _("Abgassolltemperatur"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Abgastemp_S",
    "half_value": 100.0,
    "exponent": 1.2,
})

metric_info["Fühler_1"] = {
    "title": _("Fühler 1"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Fühler_1",
    "half_value": 50.0,
    "exponent": 1.2,
})

metric_info["Kesselsoll"] = {
    "title": _("Kesselsolltemperatur"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Kesselsoll",
    "half_value": 50.0,
    "exponent": 1.2,
})

metric_info["Pufferoben"] = {
    "title": _("Pufferoben"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Pufferoben",
    "half_value": 50.0,
    "exponent": 1.2,
})

metric_info["Pufferunten"] = {
    "title": _("Pufferunten"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Pufferunten",
    "half_value": 50.0,
    "exponent": 1.2,
})

metric_info["Boiler_1"] = {
    "title": _("Boiler 1"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    # "color": "#cc071e",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Boiler_1",
    "half_value": 50.0,
    "exponent": 1.2,
})

metric_info["Vorlauf_1"] = {
    "title": _("Vorlauf 1"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Vorlauf_1",
    "half_value": 40.0,
    "exponent": 1.2,
})

metric_info["Vorlauf_2"] = {
    "title": _("Vorlauf 2"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Vorlauf_2",
    "half_value": 40.0,
    "exponent": 1.2,
})

metric_info["Aussentemp"] = {
    "title": _("Aussentemperatur"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Aussentemp",
    "half_value": 20.0,
    "exponent": 1.2,
})

metric_info["Kollektortemp"] = {
    "title": _("Kollektortemp"),
    "help": _("Temperatur Anzeige"),
    "unit": "c",
    "color": "14/b",
}

perfometer_info.append({
    "type": "logarithmic",
    "metric": "Kollektortemp",
    "half_value": 50.0,
    "exponent": 1.2,
})

#   __                _ _                                                _
#  / _|_ __ ___   ___| (_)_ __   __ _      _ __   ___ _ __ ___ ___ _ __ | |_
# | |_| '__/ _ \ / _ \ | | '_ \ / _` |    | '_ \ / _ \ '__/ __/ _ \ '_ \| __|
# |  _| | | (_) |  __/ | | | | | (_| |    | |_) |  __/ | | (_|  __/ | | | |_
# |_| |_|  \___/ \___|_|_|_| |_|\__, |____| .__/ \___|_|  \___\___|_| |_|\__|
#                               |___/_____|_|

metric_info["Kesselstrg"] = {
    "title": _("Kesselsteuerung"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Kesselstrg"],
    "total": 100.0,
})

metric_info["Primärluft"] = {
    "title": _("Primärluft"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Primärluft"],
    "total": 100.0,
})

metric_info["Rest_O2_ist"] = {
    "title": _("Restsauerstoffgehalt"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Rest_O2_ist"],
    "total": 100.0,
})

metric_info["O2_Regler"] = {
    "title": _("O2 Regler"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["O2_Regler"],
    "total": 100.0,
})

metric_info["Sekundärluft"] = {
    "title": _("Sekundärluft"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Sekundärluft"],
    "total": 100.0,
})

metric_info["Saugzug_Soll"] = {
    "title": _("Saugzug_Soll"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Saugzug_Soll"],
    "total": 100.0,
})

metric_info["Einschub_Ist"] = {
    "title": _("Einschub_Ist"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Einschub_Ist"],
    "total": 100.0,
})

metric_info["O2_Regler_Pell"] = {
    "title": _("O2_Regler_Pell"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["O2_Regler_Pell"],
    "total": 100.0,
})

metric_info["Füllstand"] = {
    "title": _("Füllstand Tagesbehälter"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Füllstand"],
    "total": 100.0,
})

metric_info["Pufferpumpe"] = {
    "title": _("Pufferpumpe"),
    "help": _("Prozent"),
    "unit": "%",
    "color": "26/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["Pufferpumpe"],
    "total": 100.0,
})
