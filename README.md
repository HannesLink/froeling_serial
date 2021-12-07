# Fröling Serial Interface

Small collection of scripts to retrieve serial data from Fröling heating system
COM2 and use them for monitoring and data visualization.

## Hardware Setup
- Fröling P4 heating system
- RaspberryPi
- USB to Serial adapter (PL2303 Chipset)
- Null modem cable

## Settings in Fröling P4
| Parameter | Wert |
| --------- | ---- |
| Bei ASCII Datenausgabe auf COM2 einen Zeilenumbruch senden | Ja |
| COM 2 wird als MODBUS Schnittstelle verwendet | Nein |

## Roadmap
- CheckMK integration (work in progress)
- Provide Prometheus metrics (planned)
- Create Grafana dashboards (planned)
- Switch from RaspberryPi to ESP32 (planned)
- Switch to Modbus and rs485 (planned)

## License
GPLv3

## Author
Johannes Link <hannes1977@gmail.com>