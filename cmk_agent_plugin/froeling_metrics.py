from cmk.gui.plugins.metrics import perfometer_info, metric_info

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
