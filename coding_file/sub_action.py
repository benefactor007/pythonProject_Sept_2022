#!/usr/bin/python3.5
"""
<class '__main__.Sub'> is inherited by <class 'set_coding_cfg.HU'>

"""
from set_coding_cfg import HU

import os, sys, json, jsonpath, pexpect

#
# json_data = {
#     "Adaptions": [
#         {
#             "RDI": "0x04FB",
#             "Name": "Activate roller test stand mode",
#             "Value": {
#                 "Status": "0x00"
#             }
#         },
#         {
#             "RDI": "0x04FC",
#             "Name": "Deactivate productionmode",
#             "Value": {
#                 "P-Mode Parameter Deaktivierung": "0x00 0x00 0x00"
#             }
#         },
#         {
#             "RDI": "0x04FE",
#             "Name": "Productionmode",
#             "Value": {
#                 "Bedienung": "0x00",
#                 "Lautstärkeeinstellung": "0x00",
#                 "Frequenzänderungsfunktionen": "0x00",
#                 "WLAN": "0x00",
#                 "Display 1 ein-/ausfahren": "0x00",
#                 "Display 1 ein/aus": "0x00",
#                 "Funkverbindung eSIM": "0x00",
#                 "FPK": "0x00",
#                 "FPK Display": "0x00",
#                 "Display 2 ein-/ausfahren": "0x00",
#                 "Display 2 ein/aus": "0x00",
#                 "SDS": "0x00",
#                 "P-Mode ID gemäß P-Mode Parameterdefinition": "0x00",
#                 "P-Mode ID \"14\" gemäß P-Mode Parameterdefinition": "0x00",
#                 "Bluetooth": "0x00",
#                 "Parameter 16": "0x00",
#                 "Parameter 17": "0x00",
#                 "Parameter 18": "0x00",
#                 "Parameter 19": "0x00",
#                 "P-Mode ID \"20\" gemäß P-Mode Parameterdefinition": "0x00",
#                 "Parameter 21": "0x00",
#                 "Parameter 22": "0x00",
#                 "Parameter 23": "0x00",
#                 "Parameter 24": "0x00"
#             }
#         },
#         {
#
#             "RDI": "0x0505",
#             "Name": "Function configuration Rear View Low",
#             "Value": {
#                 "Rear View Low (RVC)": "0x00",
#                 "RVClow Black Screen velocity threshold": "0x00",
#                 "RVClow FailSafe": "0x00",
#                 "RVClow Black Screen trunk open": "0x00",
#                 "Reserved": "0x00",
#                 "RVClow Lid Close Delay Time": "0x00",
#                 "RVClow Videofailure DetectionTime": "0x00"
#             }
#         },
#
#         {
#             "RDI": "0x050E",
#             "Name": "Radio level offsets",
#             "Value": {
#                 "AM Q-Level Offset Einstellung": "0x1F",
#                 "FM Q-Level Offset Einstellung": "0x1F"
#             }
#         },
#         {
#             "RDI": "0x050F",
#             "Name": "Error mask",
#             "Value": {
#                 "DTC-DFCC 1": "0x00 0x00 0x00",
#                 "DTC-DFCC 2": "0x00 0x00 0x00",
#                 "DTC-DFCC 3": "0x00 0x00 0x00",
#                 "DTC-DFCC 4": "0x00 0x00 0x00",
#                 "DTC-DFCC 5": "0x00 0x00 0x00",
#                 "DTC-DFCC 6": "0x00 0x00 0x00",
#                 "DTC-DFCC 7": "0x00 0x00 0x00",
#                 "DTC-DFCC 8": "0x00 0x00 0x00",
#                 "DTC-DFCC 9": "0x00 0x00 0x00",
#                 "DTC-DFCC 10": "0x00 0x00 0x00"
#             }
#         }
#     ]
# }

json_data = {
    "Adaptions": [
        {
            "RDI": "0x04FB",
            "Name": "Activate roller test stand mode",
            "Value": {
                "Status": "0x00"
            }
        },
        {
            "RDI": "0x04FC",
            "Name": "Deactivate productionmode",
            "Value": {
                "P-Mode Parameter Deaktivierung": "0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x04FE",
            "Name": "Productionmode",
            "Value": {
                "Bedienung": "0x00",
                "Lautstärkeeinstellung": "0x00",
                "Frequenzänderungsfunktionen": "0x00",
                "WLAN": "0x00",
                "Display 1 ein-/ausfahren": "0x00",
                "Display 1 ein/aus": "0x00",
                "Funkverbindung eSIM": "0x00",
                "FPK": "0x00",
                "FPK Display": "0x00",
                "Display 2 ein-/ausfahren": "0x00",
                "Display 2 ein/aus": "0x00",
                "SDS": "0x00",
                "P-Mode ID gemäß P-Mode Parameterdefinition": "0x00",
                "P-Mode ID \"14\" gemäß P-Mode Parameterdefinition": "0x00",
                "Bluetooth": "0x00",
                "Parameter 16": "0x00",
                "Parameter 17": "0x00",
                "Parameter 18": "0x00",
                "Parameter 19": "0x00",
                "P-Mode ID \"20\" gemäß P-Mode Parameterdefinition": "0x00",
                "Parameter 21": "0x00",
                "Parameter 22": "0x00",
                "Parameter 23": "0x00",
                "Parameter 24": "0x00"
            }
        },
        {

            "RDI": "0x0505",
            "Name": "Function configuration Rear View Low",
            "Value": {
                "Rear View Low (RVC)": "0x00",
                "RVClow Black Screen velocity threshold": "0x00",
                "RVClow FailSafe": "0x00",
                "RVClow Black Screen trunk open": "0x00",
                "Reserved": "0x00",
                "RVClow Lid Close Delay Time": "0x00",
                "RVClow Videofailure DetectionTime": "0x00"
            }
        },

        {
            "RDI": "0x050E",
            "Name": "Radio level offsets",
            "Value": {
                "AM Q-Level Offset Einstellung": "0x1F",
                "FM Q-Level Offset Einstellung": "0x1F"
            }
        },
        {
            "RDI": "0x050F",
            "Name": "Error mask",
            "Value": {
                "DTC-DFCC 1": "0x00 0x00 0x00",
                "DTC-DFCC 2": "0x00 0x00 0x00",
                "DTC-DFCC 3": "0x00 0x00 0x00",
                "DTC-DFCC 4": "0x00 0x00 0x00",
                "DTC-DFCC 5": "0x00 0x00 0x00",
                "DTC-DFCC 6": "0x00 0x00 0x00",
                "DTC-DFCC 7": "0x00 0x00 0x00",
                "DTC-DFCC 8": "0x00 0x00 0x00",
                "DTC-DFCC 9": "0x00 0x00 0x00",
                "DTC-DFCC 10": "0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0512",
            "Name": "Erweiterte Funktionskonfiguration Bauteil",
            "Value": {
                "Android Navigation": "0x01",
                "Reserved": "0x00 0x00"
            }
        },

        {
            "RDI": "0x0513",
            "Name": "Powermanagement timer",
            "Value": {
                "MMI Off 1": "0x1E",
                "MMI Off 2": "0x1E",
                "MMI Standby": "0x1E",
                "Pdd": "0x0A",
                "PDD Online Update": "0x0A",
                "MMI Standby Pwr Save": "0x1E",
                "Shutdown Suspend": "0x00 0x78",
                "Sleep": "0x00 0x3C",
                "MMI on Tel": "0x00 0x3C",
                "MMI on Online Swdl": "0x00 0x0F",
                "MMI online Uota": "0x00 0x3C",
                "MMI online Delay": "0x00 0x3C",
                "BEM Shutdown": "0x00 0x0A",
                "Max Cluster Wakeup": "0x02",
                "MMI Rtc": "0x00 0x3C",
                "Max Car Wakeup": "0x0A",
                "Max Unit Wakeup": "0x01",
                "Max RTC Wakeup": "0x0A",
                "MMI DCI": "0x78",
                "MMI Online Min": "0x78"
            }
        },
        {
            "RDI": "0x0514",
            "Name": "Key code monitoring",
            "Value": {
                "Keycode 0x00-0x07": "0xFF",
                "Keycode 0x08-0x0F": "0xFF",
                "Keycode 0x10-0x17": "0xFF",
                "Keycode 0x18-0x1F": "0xFF",
                "Keycode 0x20-0x27": "0xFF",
                "Keycode 0x28-0x2F": "0xFF",
                "Keycode 0x30-0x37": "0xFF",
                "Keycode 0x38-0x3F": "0xFF",
                "Keycode 0x40-0x47": "0xFF",
                "Keycode 0x48-0x4F": "0xFF",
                "Keycode 0x50-0x57": "0xFF",
                "Keycode 0x58-0x5F": "0xFF",
                "Keycode 0x60-0x67": "0xFF",
                "Keycode 0x68-0x6F": "0xFF",
                "Keycode 0x70-0x77": "0xFF",
                "Keycode 0x78-0x7F": "0xFF",
                "Keycode 0x80-0x87": "0xFF",
                "Keycode 0x88-0x8F": "0xFF",
                "Keycode 0x90-0x97": "0xFF",
                "Keycode 0x98-0x9F": "0xFF",
                "Keycode 0xA0-0xA7": "0xFF",
                "Keycode 0xA8-0xAF": "0xFF",
                "Keycode 0xB0-0xB7": "0xFF",
                "Keycode 0xB8-0xBF": "0xFF",
                "Keycode 0xC0-0xC7": "0xFF",
                "Keycode 0xC8-0xCF": "0xFF",
                "Keycode 0xD0-0xD7": "0xFF",
                "Keycode 0xD8-0xDF": "0xFF",
                "Keycode 0xE0-0xE7": "0xFF",
                "Keycode 0xE8-0xEF": "0xFF",
                "Keycode 0xF0-0xF7": "0xFF",
                "Keycode 0xF8-0xFF": "0xFF"
            }
        },
        {
            "RDI": "0x0515",
            "Name": "Logging_configuration",
            "Value": {
                "Zugriff": "0x00",
                "Speicher": "0x00",
                "Umfang": "0x00"
            }
        },
        {
            "RDI": "0x0516",
            "Name": "WLAN 5 GHz",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0517",
            "Name": "Same SSID for 2_4 and 5 GHz",
            "Value": {
                "Status": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0518",
            "Name": "Channel band-width 802_11ac",
            "Value": {
                "Bandbreite": "0x02",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0519",
            "Name": "WLAN channel numbers",
            "Value": {
                "Kanalnummer für 2.4 GHz": "0x06",
                "Kanalnummer für 5 GHz": "0x0C"
            }
        },
        {
            "RDI": "0x0520",
            "Name": "Alphabetic scrollbar",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0521",
            "Name": "Create Geocoordinate",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0522",
            "Name": "Show Geocoordinate",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0523",
            "Name": "Number to name matching algorithm",
            "Value": {
                "Status": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0524",
            "Name": "Sortorder",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0525",
            "Name": "Calendar Reminder",
            "Value": {
                "Akustischer Reminder": "0x01",
                "Hapticher Reminder": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x052A",
            "Name": "NHTSA properties - Smartphone integration",
            "Value": {
                "Grenzwertabhängigkeit": "0x00",
                "NHTSA Begrenzungsschalter für AndroidAuto - Keine Videowiedergabe": "0x00",
                "NHTSA Begrenzungsschalter für AndroidAuto - Keine Texteingabe": "0x00",
                "NHTSA Begrenzungsschalter für AndroidAuto - Keine Spracheingabe": "0x00",
                "NHTSA Begrenzungsschalter für AndroidAuto - Keine Konfiguration": "0x00",
                "NHTSA Begrenzungsschalter für AndroidAuto - Limit angezeigte Nachrichtenlänge": "0x00",
                "NHTSA Begrenzungsschalter für CarPlay - Kein softKeyboard": "0x00",
                "NHTSA Begrenzungsschalter für CarPlay - Kein softPhoneKeypad": "0x00",
                "NHTSA Begrenzungsschalter für CarPlay - Limit nonMusikliste": "0x00",
                "NHTSA Begrenzungsschalter für CarPlay - Limit Musikliste": "0x00",
                "NHTSA Begrenzungsschalter für CarPlay - Japan Maps": "0x00",
                "Reserved": "0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0530",
            "Name": "Exit screen configuration",
            "Value": {
                "Exit Screen": "0x01",
                "Exit Screen Anzeigedauer": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0550",
            "Name": "Function configuration Audio",
            "Value": {
                "Sound System": "0x01",
                "Kanal 1 Hochtonlautsprecher": "0x01",
                "Kanal 1 Tieftonlautsprecher": "0x01",
                "Kanal 2 Hochtonlautsprecher": "0x01",
                "Kanal 2 Tieftonlautsprecher": "0x01",
                "Kanal 3 Hochtonlautsprecher": "0x01",
                "Kanal 3 Tieftonlautsprecher": "0x01",
                "Kanal 4 Hochtonlautsprecher": "0x01",
                "Kanal 4 Tieftonlautsprecher": "0x01",
                "Kanal 5 Hochtonlautsprecher": "0x00",
                "Kanal 5 Tieftonlautsprecher": "0x00",
                "Kanal 6 Hochtonlautsprecher": "0x00",
                "Kanal 6 Tieftonlautsprecher": "0x00",
                "Kanal 7 Hochtonlautsprecher": "0x00",
                "Kanal 7 Tieftonlautsprecher": "0x00",
                "Kanal 8 Hochtonlautsprecher": "0x00",
                "Kanal 8 Tieftonlautsprecher": "0x00",
                "Kanal 9 Hochtonlautsprecher": "0x00",
                "Kanal 9 Tieftonlautsprecher": "0x00",
                "Kanal 10 Hochtonlautsprecher": "0x00",
                "Kanal 10 Tieftonlautsprecher": "0x00",
                "Kanal 11 Hochtonlautsprecher": "0x00",
                "Kanal 11 Tieftonlautsprecher": "0x00",
                "Kanal 12 Hochtonlautsprecher": "0x00",
                "Kanal 12 Tieftonlautsprecher": "0x00",
                "Kanal 13 Hochtonlautsprecher": "0x00",
                "Kanal 13 Tieftonlautsprecher": "0x00",
                "Kanal 14 Hochtonlautsprecher": "0x00",
                "Kanal 14 Tieftonlautsprecher": "0x00",
                "Kanal 15 Hochtonlautsprecher": "0x00",
                "Kanal 15 Tieftonlautsprecher": "0x00",
                "Kanal 16 Hochtonlautsprecher": "0x00",
                "Kanal 16 Tieftonlautsprecher": "0x00",
                "Kanal 17 Hochtonlautsprecher": "0x00",
                "Kanal 17 Tieftonlautsprecher": "0x00",
                "Kanal 18 Hochtonlautsprecher": "0x00",
                "Kanal 18 Tieftonlautsprecher": "0x00",
                "Kanal 19 Hochtonlautsprecher": "0x00",
                "Kanal 19 Tieftonlautsprecher": "0x00",
                "Kanal 20 Hochtonlautsprecher": "0x00",
                "Kanal 20 Tieftonlautsprecher": "0x00",
                "Kanal 21 Hochtonlautsprecher": "0x00",
                "Kanal 21 Tieftonlautsprecher": "0x00",
                "Kanal 22 Hochtonlautsprecher": "0x00",
                "Kanal 22 Tieftonlautsprecher": "0x00",
                "Kanal 23 Hochtonlautsprecher": "0x00",
                "Kanal 23 Tieftonlautsprecher": "0x00",
                "Kanal 24 Hochtonlautsprecher": "0x00",
                "Kanal 24 Tieftonlautsprecher": "0x00",
                "Mikrofon 1": "0x01",
                "Mikrofon 2": "0x00",
                "Mikrofon 3": "0x00",
                "Mikrofon 4": "0x00",
                "Start Sound": "0x01",
                "Kanal 25 Hochtonlautsprecher": "0x01",
                "Kanal 25 Tieftonlautsprecher": "0x00",
                "Früher Motorsound": "0x00",
                "Signalfluss-Topologie": "0x00",
                "Reserviert2": "0x00",
                "Reserviert1": "0x00"
            }
        },
        {
            "RDI": "0x0551",
            "Name": "Function Configuration Sound",
            "Value": {
                "Markensound": "0x00",
                "Fahrbereitschaftssound": "0x01",
                "Vehicle Leaving Sound": "0x01",
                "Mikrofon zur Unterdrückung von Fahrzeuggeräuschen": "0x00",
                "Einziehbare Hochtöner": "0x00"
            }
        },
        {
            "RDI": "0x0552",
            "Name": "Function configuration CAR",
            "Value": {
                "Klimavariante": "0x00",
                "Reserviert1": "0x00",
                "BAP SDS_SD": "0x01",
                "BAP Online Funktionen": "0x00",
                "Kombi Anbindung": "0x02",
                "Reserviert2": "0x00"
            }
        },
        {
            "RDI": "0x0553",
            "Name": "Function configuration Phone",
            "Value": {
                "Koppelbox mit PWM Anschluss": "0x00",
                "Koppelbox Antenne": "0x01",
                "Koppelbox Wireless Charging": "0x01",
                "Koppelbox NFC": "0x00",
                "DTMF ohne aktiven Anruf": "0x01",
                "Anruf annehmen und halten": "0x01",
                "Weitere Bluetooth Telefone": "0x03",
                "LTE Modul": "0x00",
                "Telefonmodul NAD": "0x00",
                "Menüpunkt 3-Wege Calling": "0x01",
                "Unterstützung für 3-Wege Calling": "0x01",
                "MAP SMS Unterstützung": "0x01",
                "MAP Email Unterstützung": "0x01",
                "MAP InstantMessaging Unterstützung": "0x01",
                "Reserviert1": "0x01",
                "eSIM Unterstützung SMS Only": "0x01",
                "Nachrichten editieren": "0x01",
                "GSM Antenne 3": "0x00",
                "GSM Antenne 4": "0x00",
                "Reserviert2": "0x00"
            }
        },
        {
            "RDI": "0x0555",
            "Name": "Function configuration Connectivity",
            "Value": {
                "Funktion WLAN": "0x01",
                "Externe WLAN Antenne": "0x00",
                "WIFI Hotspot 2,4 GHz": "0x01",
                "WIFI Hotspot 5 GHz": "0x01",
                "WLAN Client Modus 2,4 GHz": "0x01",
                "WLAN Client Modus 5 GHz": "0x01",
                "App-Connect über Wifi": "0x00",
                "Online Medien": "0x01",
                "Baidu CarLife": "0x01",
                "Google Android Auto": "0x00",
                "Apple Car Play": "0x01",
                "Mirror Link": "0x00",
                "Mirror Link Country Code": "0x03",
                "MirrorLink RGB": "0x01",
                "VIWI Funktion": "0x01",
                "VIWI Access Mode": "0x01",
                "Bluetooth-Sichtbarkeit (Werkseinstellung)": "0x02",
                "Bluetooth Verfügbarkeit": "0x02",
                "Messaging über Map": "0x01",
                "Messaging Pagewise Scrolling": "0x01",
                "Kalender über CTN": "0x01",
                "Routen von WLAN APs zu CCU": "0x00",
                "Verbindungskontrolle WLAN Tethering über Diagnose": "0x01",
                "Bluetooth Multimediafunktionalität": "0x01",
                "Bluetooth Telefon": "0x01",
                "Bluetooth Audio": "0x01",
                "Bluetooth drahtlose Kopfhörer": "0x01",
                "Baidu CarLife iOS": "0x01",
                "Reserviert1": "0x00",
                "Reserviert2": "0x00",
                "Reserviert3": "0x00"
            }
        },
        {
            "RDI": "0x0556",
            "Name": "Function configuration HMI",
            "Value": {
                "Skin Codierung": "0x01",
                "Fahrzeugbild": "0x00",
                "Bordbuch": "0x01",
                "Speller": "0x00",
                "Initialer HMI Disclaimer": "0x00",
                "Legal HMI Disclaimer": "0x00",
                "Hilfekontext 0": "0x01",
                "Hilfekontext 1": "0x01",
                "Hilfekontext 2": "0x01",
                "Hilfekontext 3": "0x01",
                "Hilfekontext 4": "0x01",
                "Hilfekontext 5": "0x01",
                "Hilfekontext 6": "0x01",
                "Hilfekontext 7": "0x01",
                "Hilfekontext 8": "0x01",
                "Hilfekontext 9": "0x01",
                "Popup wenn GPS-Dienste verwendet werden": "0x00",
                "Reserviert1": "0x00",
                "Reserviert2": "0x00"
            }
        },
        {
            "RDI": "0x0557",
            "Name": "Function configuration Media",
            "Value": {
                "Funktion Import Multimediadaten": "0x00",
                "Funktion Ripping Multimediadaten": "0x00",
                "Gracenote Online Coverarts": "0x00",
                "Gracenote Online Other": "0x00",
                "Gracenote Local Coverarts": "0x01",
                "Gracenote Local Other": "0x01",
                "USB": "0x03",
                "AUX IN": "0x00",
                "Picture Viewer": "0x00",
                "Automatischer App Start auf Kundengerät": "0x01",
                "Online Media (MonD)": "0x00",
                "Online TV": "0x00",
                "Externes CD Laufwerk": "0x00",
                "External TV-Tuner": "0x00",
                "Reserviert2": "0x00",
                "Reserviert1": "0x00"
            }
        },
        {
            "RDI": "0x0558",
            "Name": "Function configuration Navigation",
            "Value": {
                "Ländervariante Funktion Navigation": "0x11",
                "Funktion Navigation": "0x01",
                "GNNS-Antenne": "0x01",
                "Verkehrszeichenanzeige (VZA)": "0x01",
                "Verkehrszeichen Online (VZO)": "0x01",
                "Prädiktive Streckendaten (PSD)": "0x01",
                "Advanced Range Display (Spiegelei Karte)": "0x01",
                "TPEG": "0x00",
                "Lokale Gefahren Info (LGI)": "0x00",
                "Map Style": "0x01",
                "Verkehrsinformation / Traffic": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0559",
            "Name": "Function configuration Radio",
            "Value": {
                "Station Logo Region DB": "0x46",
                "Bandeinstellung FM Tuner": "0x05",
                "Bandeinstellung AM Tuner": "0x00",
                "Bandeinstellung DAB Tuner Band 1": "0x00",
                "HD FM Antennenstrategie": "0x00",
                "2.FM Antenne": "0x00",
                "DAB-Antenne Modus 1": "0x00",
                "AM/FM/DAB Antenne": "0x00",
                "AF Aktivierungsmodus": "0x00",
                "FM HD HMI Switch Default Wert": "0x00",
                "AM HD HMI Switch Default Wert": "0x00",
                "DAB Alarm": "0x00",
                "FM PTY31 Alarm": "0x00",
                "AM Sperre": "0x00",
                "DRM30 MF Band": "0x00",
                "DRM+ Band 2 FM": "0x00",
                "Mehrfacheingangsschalter": "0x00",
                "RDS HMI Switch Sichtbarkeit": "0x00",
                "RDS HMI Switch Default Wert": "0x00",
                "AF HMI Switch Default Wert": "0x01",
                "RadioText+": "0x01",
                "PI Ignorierung": "0x01",
                "Hybrid Radio zusätzliche Onlinedaten": "0x00",
                "Hybrid Radio Reichweitenvergrößerer": "0x00",
                "Online Radio": "0x00",
                "FM Radio Profile": "0x00",
                "Aktivierung SDARS Band": "0x00",
                "Konfiguration SDARS Typ": "0x00",
                "Reserviert2": "0x00",
                "Reserviert1": "0x00"
            }
        },
        {
            "RDI": "0x055A",
            "Name": "Function configuration Speech",
            "Value": {
                "Ländervariante": "0x05",
                "SDS Region Flag": "0x05"
            }
        },
        {
            "RDI": "0x055B",
            "Name": "Function configuration SW/Update",
            "Value": {
                "Update Over The Air (UOTA)": "0x01",
                "Update Over The Air (UOTA_2)": "0x00",
                "Uota Onboard Tester": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x055C",
            "Name": "Function configuration Bauteil",
            "Value": {
                "RVC Videoeingang": "0x02",
                "Zweite Anzeigeeinheit über LVDS angeschlossen": "0x00",
                "Display Ausfahrgeschwindigkeit": "0x00",
                "Pilot Parking": "0x00",
                "Aussetzung zum RAM": "0x00",
                "Web App Plattform Side loading": "0x01",
                "Reset type hardware reset": "0x00"
            }
        },
        {
            "RDI": "0x0560",
            "Name": "IPv4 address of Subnet 1 (L2TP tunnel) on MIB",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xC9",
                "Segment 4": "0x02"
            }
        },
        {
            "RDI": "0x0561",
            "Name": "IPv4 address of Subnet 1 (L2TP tunnel) on CCU ",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xC9",
                "Segment 4": "0x01"
            }
        },
        {
            "RDI": "0x0562",
            "Name": "IPv4 address of Subnet 2 (L2TP tunnel) on MIB",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xCA",
                "Segment 4": "0x02"
            }
        },
        {
            "RDI": "0x0563",
            "Name": "IPv4 address of Subnet 2 (L2TP tunnel) on CCU",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xCA",
                "Segment 4": "0x01"
            }
        },
        {
            "RDI": "0x0564",
            "Name": "IPv4 address of the WLAN AP",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xBD",
                "Segment 4": "0x01"
            }
        },
        {
            "RDI": "0x0565",
            "Name": "IPv6 address of Subnet 1 (L2TP tunnel) on MIB",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x00 0x01"
            }
        },
        {
            "RDI": "0x0566",
            "Name": "IPv6 address of Subnet 1 (L2TP tunnel) on CCU",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x00 0x01"
            }
        },
        {
            "RDI": "0x0567",
            "Name": "IPv6 address of Subnet 2 (L2TP tunnel) on MIB",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x00 0x02"
            }
        },
        {
            "RDI": "0x0568",
            "Name": "IPv6 address of Subnet 2 (L2TP tunnel) on CCU",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x00 0x02"
            }
        },
        {
            "RDI": "0x0569",
            "Name": "IPv6 address of the WLAN AP",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x01 0x03"
            }
        },
        {
            "RDI": "0x056A",
            "Name": "WLAN AP local net DHCP lease time",
            "Value": {
                "Gültigkeitsdauer": "0x48"
            }
        },
        {
            "RDI": "0x056F",
            "Name": "Function Configuration A2B",
            "Value": {
                "Topologie": "0x01",
                "Infotainment Unit": "0x01",
                "MIC MOD Hinten links": "0x00",
                "MIC MOD Hinten rechts": "0x00",
                "Connectivity Unit": "0x00",
                "Mic Module Dach": "0x01",
                "Mic Module Anzeige": "0x00",
                "Infotainment Mic Unit": "0x00",
                "Reserviert": "0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0570",
            "Name": "A2B data streams",
            "Value": {
                "Anzahl Mikrofonwandler Frontmodulknoten": "0x03",
                "Anzahl Mikrofonwandler linker Rückseitenmodulknoten": "0x00",
                "Anzahl Mikrofonwandler rechter Rückseitenmodulknoten": "0x00",
                "Notfallauswahl Microfonwandler": "0x03",
                "Multi Center Lautsprecher über Connectivity Unit": "0x01",
                "Reserviert": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0571",
            "Name": "Function configuration PSO",
            "Value": {
                "PSO Funktion": "0x00",
                "IAA Function": "0x01",
                "Reserviert": "0x00 0x00"
            }
        },
        {
            "RDI": "0x0573",
            "Name": "IPv6 address of Subnet 4 (L2TP tunnel) on MIB",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x00 0x02"
            }
        },
        {
            "RDI": "0x0574",
            "Name": "IPv6 address of Subnet 4 (L2TP tunnel) on CCU",
            "Value": {
                "Segment 1": "0xFD 0x30",
                "Segment 2": "0xE0 0x8E",
                "Segment 3": "0xC0 0x31",
                "Segment 4": "0x00 0x02"
            }
        },
        {
            "RDI": "0x0575",
            "Name": "IPv4 address of Subnet 4 (L2TP tunnel) on MIB",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xCA",
                "Segment 4": "0x02"
            }
        },
        {
            "RDI": "0x0576",
            "Name": "IPv4 address of Subnet 4 (L2TP tunnel) on CCU",
            "Value": {
                "Segment 1": "0x0A",
                "Segment 2": "0xAD",
                "Segment 3": "0xCA",
                "Segment 4": "0x01"
            }
        },
        {
            "RDI": "0x0902",
            "Name": "Activation of development messages",
            "Value": {
                "Entwicklerbotschaftsgruppe 1 (Infotainment CAN)": "0x00",
                "Entwicklerbotschaftsgruppe 2 (MIB CAN)": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0909",
            "Name": "Info call number 2 (roaming)",
            "Value": {
                "Rufnummer": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x090A",
            "Name": "Service call number 2 (roaming)",
            "Value": {
                "Rufnummer": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x090B",
            "Name": "Info call number 1",
            "Value": {
                "Rufnummer": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x090C",
            "Name": "Service call number 1",
            "Value": {
                "Rufnummer": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0958",
            "Name": "FM Mono Stereo settings",
            "Value": {
                "Untere HF Stereo Schwelle": "0x18",
                "Maximale NF Stereo Kanalabtrennung": "0x20",
                "Hysterese Zeit für Wechsel Mono / Stereo": "0x96"
            }
        },
        {
            "RDI": "0x0981",
            "Name": "Activation for external usb",
            "Value": {
                "USB Buchse 1": "0x01",
                "Reserviert1": "0x00",
                "USB Buchse 2": "0x01",
                "Reserviert2": "0x00",
                "USB Buchse 3": "0x01",
                "Reserviert3": "0x00",
                "USB Buchse 4": "0x01",
                "Reserviert4": "0x00"
            }
        },
        {
            "RDI": "0x0986",
            "Name": "OnlineServices HMI_Availability",
            "Value": {
                "OnlineServices HMI Verfügbarkeit": "0x01"
            }
        },
        {
            "RDI": "0x09CB",
            "Name": "Media country code HMI",
            "Value": {
                "Verkaufsland": "0x43 0x4E"
            }
        },
        {
            "RDI": "0x09D3",
            "Name": "Function configuration ethernet",
            "Value": {
                "Aktivierung Ethernet Zweig 1": "0x01",
                "Aktivierung Ethernet Zweig 2": "0x02",
                "Aktivierung Ethernet Zweig 3": "0x02",
                "Aktivierung Ethernet Zweig 4": "0x00",
                "Reserved": "0x00"
            }
        },
        {
            "RDI": "0x09EB",
            "Name": "HMI Function Blocking Table",
            "Value": {
                "Tuner 0": "0x00",
                "Tuner 1": "0x00",
                "Tuner 2": "0x00",
                "Tuner 3": "0x00",
                "Tuner 4": "0x00",
                "Tuner 5": "0x00",
                "Tuner 6": "0x00",
                "Tuner 7": "0x00",
                "Tuner 8": "0x00",
                "Tuner 9": "0x00",
                "Tuner 10": "0x00",
                "Tuner 11": "0x00",
                "Tuner 12": "0x00",
                "Tuner 13": "0x00",
                "Tuner 14": "0x00",
                "Tuner 15": "0x00",
                "Media 0": "0x00",
                "Media 1": "0x00",
                "Media 2": "0x00",
                "Media 3": "0x00",
                "Media 4": "0x00",
                "Media 5": "0x00",
                "Media 6": "0x00",
                "Media 7": "0x00",
                "Media 8": "0x00",
                "Media 9": "0x00",
                "Media 10": "0x00",
                "Media 11": "0x00",
                "Media 12": "0x00",
                "Media 13": "0x00",
                "Media 14": "0x00",
                "Media 15": "0x00",
                "Media 16": "0x00",
                "Media 17": "0x00",
                "Media 18": "0x00",
                "Media 19": "0x00",
                "Media 20": "0x00",
                "Media 21": "0x00",
                "Media 22": "0x00",
                "Media 23": "0x00",
                "Telefon 0": "0x00",
                "Telefon 1": "0x00",
                "Telefon 2": "0x00",
                "Telefon 3": "0x00",
                "Telefon 4": "0x00",
                "Telefon 5": "0x00",
                "Telefon 6": "0x00",
                "Telefon 7": "0x00",
                "Telefon 8": "0x00",
                "Telefon 9": "0x00",
                "Telefon 10": "0x00",
                "Telefon 11": "0x00",
                "Telefon 12": "0x00",
                "Telefon 13": "0x00",
                "Telefon 14": "0x00",
                "Telefon 15": "0x00",
                "Navigation 0": "0x00",
                "Navigation 1": "0x00",
                "Navigation 2": "0x00",
                "Navigation 3": "0x00",
                "Navigation 4": "0x00",
                "Navigation 5": "0x00",
                "Navigation 6": "0x00",
                "Navigation 7": "0x00",
                "Navigation 8": "0x00",
                "Navigation 9": "0x00",
                "Navigation 10": "0x00",
                "Navigation 11": "0x00",
                "Navigation 12": "0x00",
                "Navigation 13": "0x00",
                "Navigation 14": "0x00",
                "Navigation 15": "0x00",
                "Navigation 16": "0x00",
                "Navigation 17": "0x00",
                "Navigation 18": "0x00",
                "Navigation 19": "0x00",
                "Navigation 20": "0x00",
                "Navigation 21": "0x00",
                "Navigation 22": "0x00",
                "Navigation 23": "0x00",
                "Navigation 24": "0x00",
                "Navigation 25": "0x00",
                "Navigation 26": "0x00",
                "Navigation 27": "0x00",
                "Navigation 28": "0x00",
                "Navigation 29": "0x00",
                "Navigation 30": "0x00",
                "Navigation 31": "0x00",
                "Navigation 32": "0x00",
                "Navigation 33": "0x00",
                "Navigation 34": "0x00",
                "Navigation 35": "0x00",
                "Navigation 36": "0x00",
                "Navigation 37": "0x00",
                "Navigation 38": "0x00",
                "Navigation 39": "0x00",
                "Car 0": "0x00",
                "Car 1": "0x00",
                "Car 2": "0x00",
                "Car 3": "0x00",
                "Car 4": "0x00",
                "Car 5": "0x00",
                "Car 6": "0x00",
                "Car 7": "0x00",
                "Car 8": "0x00",
                "Car 9": "0x00",
                "Car 10": "0x00",
                "Car 11": "0x00",
                "Car 12": "0x00",
                "Car 13": "0x00",
                "Car 14": "0x00",
                "Car 15": "0x00",
                "Car 16": "0x00",
                "Car 17": "0x00",
                "Car 18": "0x00",
                "Car 19": "0x00",
                "Car 20": "0x00",
                "Car 21": "0x00",
                "Car 22": "0x00",
                "Car 23": "0x00",
                "MISC 0": "0x00",
                "MISC 1": "0x00",
                "MISC 2": "0x00",
                "MISC 3": "0x00",
                "MISC 4": "0x00",
                "MISC 5": "0x00",
                "MISC 6": "0x00",
                "MISC 7": "0x00",
                "MISC 8": "0x00",
                "MISC 9": "0x00",
                "MISC 10": "0x00",
                "MISC 11": "0x00",
                "MISC 12": "0x00",
                "MISC 13": "0x00",
                "MISC 14": "0x00",
                "MISC 15": "0x00",
                "MISC 16": "0x00",
                "MISC 17": "0x00",
                "MISC 18": "0x00",
                "MISC 19": "0x00",
                "MISC 20": "0x00",
                "MISC 21": "0x00",
                "MISC 22": "0x00",
                "MISC 23": "0x00",
                "MISC 24": "0x00",
                "MISC 25": "0x00",
                "MISC 26": "0x00",
                "MISC 27": "0x00",
                "MISC 28": "0x00",
                "MISC 29": "0x00",
                "MISC 30": "0x00",
                "MISC 31": "0x00",
                "MISC 32": "0x00",
                "MISC 33": "0x00",
                "MISC 34": "0x00",
                "MISC 35": "0x00",
                "MISC 36": "0x00",
                "MISC 37": "0x00",
                "MISC 38": "0x00",
                "MISC 39": "0x00",
                "MISC 40": "0x00",
                "MISC 41": "0x00",
                "MISC 42": "0x00",
                "MISC 43": "0x00",
                "MISC 44": "0x00",
                "MISC 45": "0x00",
                "MISC 46": "0x00",
                "MISC 47": "0x00",
                "Hilfe 0": "0x00",
                "Hilfe 1": "0x00",
                "Hilfe 2": "0x00",
                "Hilfe 3": "0x00",
                "Hilfe 4": "0x00",
                "Hilfe 5": "0x00",
                "Hilfe 6": "0x00",
                "Hilfe 7": "0x00",
                "Hilfe 8": "0x00",
                "Hilfe 9": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0A08",
            "Name": "Bluetooth audio codecs",
            "Value": {
                "Audio Codecs": "0x01"
            }
        },
        {
            "RDI": "0x0B02",
            "Name": "Emergency Call 1",
            "Value": {
                "Rufnummer": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0B03",
            "Name": "Emergency Call 1 (roaming)",
            "Value": {
                "Rufnummer": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0B12",
            "Name": "Summer time shift method",
            "Value": {
                "Sommerzeitberechnung": "0x00"
            }
        },
        {
            "RDI": "0x0B13",
            "Name": "Fan operation",
            "Value": {
                "Kühlung": "0x01"
            }
        },
        {
            "RDI": "0x0B1B",
            "Name": "Car function adaptations",
            "Value": {
                "ACC: Menüanzeige": "0x01",
                "ACC: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "ACC: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "ACC: Bedienung nur im Stillstand möglich": "0x00",
                "ACC: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Ambientebeleuchtung: Menüanzeige": "0x01",
                "Ambientebeleuchtung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Ambientebeleuchtung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Ambientebeleuchtung: Bedienung nur im Stillstand möglich": "0x00",
                "Ambientebeleuchtung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Einparkhilfe: Menüanzeige": "0x01",
                "Einparkhilfe: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Einparkhilfe: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Einparkhilfe: Bedienung nur im Stillstand möglich": "0x00",
                "Einparkhilfe: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "AWV: Menüanzeige": "0x01",
                "AWV: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "AWV: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "AWV: Bedienung nur im Stillstand möglich": "0x00",
                "AWV: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Lane Departure Warning: Menüanzeige": "0x01",
                "Lane Departure Warning: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Lane Departure Warning: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Lane Departure Warning: Bedienung nur im Stillstand möglich": "0x00",
                "Lane Departure Warning: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Spurwechselassistent: Menüanzeige": "0x01",
                "Spurwechselassistent: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Spurwechselassistent: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Spurwechselassistent: Bedienung nur im Stillstand möglich": "0x00",
                "Spurwechselassistent: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Außenbeleuchtung: Menüanzeige": "0x01",
                "Außenbeleuchtung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Außenbeleuchtung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Außenbeleuchtung: Bedienung nur im Stillstand möglich": "0x00",
                "Außenbeleuchtung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Fenster: Menüanzeige": "0x01",
                "Fenster: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Fenster: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Fenster: Bedienung nur im Stillstand möglich": "0x00",
                "Fenster: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Klimaeinstellung: Menüanzeige": "0x01",
                "Klimaeinstellung : Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Klimaeinstellung : Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Klimaeinstellung : Bedienung nur im Stillstand möglich": "0x00",
                "Klimaeinstellung : Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Standheizung: Menüanzeige": "0x01",
                "Standheizung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Standheizung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Standheizung: Bedienung nur im Stillstand möglich": "0x00",
                "Standheizung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Bordcomputer: Menüanzeige": "0x01",
                "Bordcomputer: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Bordcomputer: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Bordcomputer: Bedienung nur im Stillstand möglich": "0x00",
                "Bordcomputer: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Reifendruckkontrolle: Menüanzeige": "0x01",
                "Reifendruckkontrolle: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Reifendruckkontrolle: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Reifendruckkontrolle: Bedienung nur im Stillstand möglich": "0x00",
                "Reifendruckkontrolle: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Scheibenwischer: Menüanzeige": "0x01",
                "Scheibenwischer: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Scheibenwischer: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Scheibenwischer: Bedienung nur im Stillstand möglich": "0x00",
                "Scheibenwischer: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Serviceintervallanzeige: Menüanzeige": "0x01",
                "Serviceintervallanzeige: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Serviceintervallanzeige: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Serviceintervallanzeige: Bedienung nur im Stillstand möglich": "0x00",
                "Serviceintervallanzeige: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Sitzeinstellung: Menüanzeige": "0x01",
                "Sitzeinstellung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Sitzeinstellung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Sitzeinstellung: Bedienung nur im Stillstand möglich": "0x00",
                "Sitzeinstellung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Zentralverriegelung: Menüanzeige": "0x01",
                "Zentralverriegelung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Zentralverriegelung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Zentralverriegelung: Bedienung nur im Stillstand möglich": "0x00",
                "Zentralverriegelung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Kompass: Menüanzeige": "0x01",
                "Kompass: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Kompass: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Kompass: Bedienung nur im Stillstand möglich": "0x00",
                "Kompass: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Charisma: Menüanzeige": "0x01",
                "Charisma: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Charisma: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Charisma: Bedienung nur im Stillstand möglich": "0x00",
                "Charisma: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Ölstandsanzeige: Menüanzeige": "0x01",
                "Ölstandsanzeige: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Ölstandsanzeige: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Ölstandsanzeige: Bedienung nur im Stillstand möglich": "0x00",
                "Ölstandsanzeige: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "VIN: Menüanzeige": "0x01",
                "VIN: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "VIN: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "VIN: Bedienung nur im Stillstand möglich": "0x00",
                "VIN: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Uhrzeit: Menüanzeige": "0x01",
                "Uhrzeit: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Uhrzeit: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Uhrzeit: Bedienung nur im Stillstand möglich": "0x00",
                "Uhrzeit: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Luftdämpfer / Dämpfer: Menüanzeige": "0x01",
                "Luftdämpfer / Dämpfer: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Luftdämpfer / Dämpfer: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Luftdämpfer / Dämpfer: Bedienung nur im Stillstand möglich": "0x00",
                "Luftdämpfer / Dämpfer: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Headup-Display: Menüanzeige": "0x01",
                "Headup-Display: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Headup-Display: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Headup-Display: Bedienung nur im Stillstand möglich": "0x00",
                "Headup-Display: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Zentraler Einheitenmaster: Menüanzeige": "0x01",
                "Zentraler Einheitenmaster: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Zentraler Einheitenmaster: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Zentraler Einheitenmaster: Bedienung nur im Stillstand möglich": "0x00",
                "Zentraler Einheitenmaster: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Hybrid: Menüanzeige": "0x01",
                "Hybrid: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Hybrid: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Hybrid: Bedienung nur im Stillstand möglich": "0x00",
                "Hybrid: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "UDGO (Universal Garage Door Opener): Menüanzeige": "0x00",
                "UDGO (Universal Garage Door Opener): Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "UDGO (Universal Garage Door Opener): Bedienung bei v > V_Threshold_high möglich": "0x00",
                "UDGO (Universal Garage Door Opener): Bedienung nur im Stillstand möglich": "0x00",
                "UDGO (Universal Garage Door Opener): Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "NightVision: Menüanzeige": "0x01",
                "NightVision: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "NightVision: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "NightVision: Bedienung nur im Stillstand möglich": "0x00",
                "NightVision: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "SideView: Menüanzeige": "0x01",
                "SideView: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "SideView: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "SideView: Bedienung nur im Stillstand möglich": "0x00",
                "SideView: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Reversibler Gurtstraffer: Menüanzeige": "0x00",
                "Reversibler Gurtstraffer: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Reversibler Gurtstraffer: Bedienung bei v > V_Threshold_high möglich": "0x00",
                "Reversibler Gurtstraffer: Bedienung nur im Stillstand möglich": "0x00",
                "Reversibler Gurtstraffer: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "MFL Jokerfunktion: Menüanzeige": "0x01",
                "MFL Jokerfunktion: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "MFL Jokerfunktion: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "MFL Jokerfunktion: Bedienung nur im Stillstand möglich": "0x00",
                "MFL Jokerfunktion: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Verkehrszeichenerkennung: Menüanzeige": "0x01",
                "Verkehrszeichenerkennung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Verkehrszeichenerkennung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Verkehrszeichenerkennung: Bedienung nur im Stillstand möglich": "0x00",
                "Verkehrszeichenerkennung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Aufmerksamkeitserkennung: Menüanzeige": "0x01",
                "Aufmerksamkeitserkennung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Aufmerksamkeitserkennung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Aufmerksamkeitserkennung: Bedienung nur im Stillstand möglich": "0x00",
                "Aufmerksamkeitserkennung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Angelernte Schlüssel: Menüanzeige": "0x01",
                "Angelernte Schlüssel: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Angelernte Schlüssel: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Angelernte Schlüssel: Bedienung nur im Stillstand möglich": "0x00",
                "Angelernte Schlüssel: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Spiegel: Menüanzeige": "0x01",
                "Spiegel: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Spiegel: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Spiegel: Bedienung nur im Stillstand möglich": "0x00",
                "Spiegel: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Fahrschulmodus: Menüanzeige": "0x01",
                "Fahrschulmodus: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Fahrschulmodus: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Fahrschulmodus: Bedienung nur im Stillstand möglich": "0x00",
                "Fahrschulmodus: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Müdigkeitserkennung: Menüanzeige": "0x01",
                "Müdigkeitserkennung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Müdigkeitserkennung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Müdigkeitserkennung: Bedienung nur im Stillstand möglich": "0x00",
                "Müdigkeitserkennung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "BCME (BordComputer mit Effizienzanzeige / Eco-HMI): Menüanzeige": "0x01",
                "BCME (BordComputer mit Effizienzanzeige / Eco-HMI): Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "BCME (BordComputer mit Effizienzanzeige / Eco-HMI): Bedienung bei v > V_Threshold_high möglich": "0x01",
                "BCME (BordComputer mit Effizienzanzeige / Eco-HMI): Bedienung nur im Stillstand möglich": "0x00",
                "BCME (BordComputer mit Effizienzanzeige / Eco-HMI): Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Fahrverhalten (User Eco Rating): Menüanzeige": "0x01",
                "Fahrverhalten (User Eco Rating): Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Fahrverhalten (User Eco Rating): Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Fahrverhalten (User Eco Rating): Bedienung nur im Stillstand möglich": "0x00",
                "Fahrverhalten (User Eco Rating): Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Bremse: Menüanzeige": "0x01",
                "Bremse: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Bremse: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Bremse: Bedienung nur im Stillstand möglich": "0x00",
                "Bremse: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Start/Stopp Gründe: Menüanzeige": "0x00",
                "Start/Stopp Gründe: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Start/Stopp Gründe: Bedienung bei v > V_Threshold_high möglich": "0x00",
                "Start/Stopp Gründe: Bedienung nur im Stillstand möglich": "0x00",
                "Start/Stopp Gründe: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Neigungswinkelanzeige: Menüanzeige": "0x01",
                "Neigungswinkelanzeige: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Neigungswinkelanzeige: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Neigungswinkelanzeige: Bedienung nur im Stillstand möglich": "0x00",
                "Neigungswinkelanzeige: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Batteriemanagement: Menüanzeige": "0x01",
                "Batteriemanagement: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Batteriemanagement: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Batteriemanagement: Bedienung nur im Stillstand möglich": "0x00",
                "Batteriemanagement: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "RearSeatEntertainment: Menüanzeige": "0x01",
                "RearSeatEntertainment: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "RearSeatEntertainment: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "RearSeatEntertainment: Bedienung nur im Stillstand möglich": "0x00",
                "RearSeatEntertainment: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Spezialfunktionen: Menüanzeige": "0x01",
                "Spezialfunktionen: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Spezialfunktionen: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Spezialfunktionen: Bedienung nur im Stillstand möglich": "0x00",
                "Spezialfunktionen: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Anhängerassistent: Menüanzeige": "0x01",
                "Anhängerassistent: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Anhängerassistent: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Anhängerassistent: Bedienung nur im Stillstand möglich": "0x00",
                "Anhängerassistent: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "TV-Tuner (BAP): Menüanzeige": "0x00",
                "TV-Tuner (BAP): Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "TV-Tuner (BAP): Bedienung auch bei v > V_Threshold_high möglich": "0x00",
                "TV-Tuner (BAP): Bedienung nur im Stillstand möglich": "0x00",
                "TV-Tuner (BAP): Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Standklimatisierung: Menüanzeige": "0x01",
                "Standklimatisierung: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Standklimatisierung: Bedienung auch bei v > V_Threshold_high möglich": "0x01",
                "Standklimatisierung: Bedienung nur im Stillstand möglich": "0x00",
                "Standklimatisierung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "PedestrianAssist: Menüanzeige": "0x01",
                "PedestrianAssist: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "PedestrianAssist: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "PedestrianAssist: Bedienung nur im Stillstand möglich": "0x00",
                "PedestrianAssist: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Sitzpneumatik: Menüanzeige": "0x01",
                "Sitzpneumatik: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Sitzpneumatik: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Sitzpneumatik: Bedienung nur im Stillstand möglich": "0x00",
                "Sitzpneumatik: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Kurvenwarner: Menüanzeige": "0x01",
                "Kurvenwarner: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Kurvenwarner: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Kurvenwarner: Bedienung nur im Stillstand möglich": "0x00",
                "Kurvenwarner: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "eCall: Menüanzeige": "0x00",
                "eCall: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "eCall: Bedienung bei v > V_Threshold_high möglich": "0x00",
                "eCall: Bedienung nur im Stillstand möglich": "0x00",
                "eCall: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "ENI: Menüanzeige": "0x01",
                "ENI: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "ENI: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "ENI: Bedienung nur im Stillstand möglich": "0x00",
                "ENI: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "SportHMI: Menüanzeige": "0x01",
                "SportHMI: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "SportHMI: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "SportHMI: Bedienung nur im Stillstand möglich": "0x00",
                "SportHMI: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Adblue: Menüanzeige": "0x01",
                "Adblue: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Adblue: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Adblue: Bedienung nur im Stillstand möglich": "0x00",
                "Adblue: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Spoiler: Menüanzeige": "0x01",
                "Spoiler: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Spoiler: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Spoiler: Bedienung nur im Stillstand möglich": "0x00",
                "Spoiler: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Efficiency Assist: Menüanzeige": "0x01",
                "Efficiency Assist: Bedienung auch bei Klemme 15 = AUS möglich": "0x00",
                "Efficiency Assist: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Efficiency Assist: Bedienung nur im Stillstand möglich": "0x00",
                "Efficiency Assist: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Display Configuration: Menüanzeige": "0x01",
                "Display Configuration: Bedienung auch bei Klemme 15 = Aus möglich": "0x01",
                "Display Configuration: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Display Configuration: Bedienung nur im Stillstand möglich": "0x01",
                "Display Configuration: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x01",
                "Soundcontrol: Menüanzeige": "0x01",
                "Soundcontrol: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Soundcontrol: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Soundcontrol: Bedienung nur im Stillstand möglich": "0x00",
                "Soundcontrol: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Standlüftung: Menüanzeige": "0x01",
                "Standlüftung: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Standlüftung: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Standlüftung: Bedienung nur im Stillstand möglich": "0x00",
                "Standlüftung: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Kreuzungsassistent: Menüanzeige": "0x01",
                "Kreuzungsassistent: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Kreuzungsassistent: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Kreuzungsassistent: Bedienung nur im Stillstand möglich": "0x00",
                "Kreuzungsassistent: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Verbindungsmanager: Menüanzeige": "0x01",
                "Verbindungsmanager: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Verbindungsmanager: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Verbindungsmanager: Bedienung nur im Stillstand möglich": "0x00",
                "Verbindungsmanager: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Wireless Charging: Menüanzeige": "0x01",
                "Wireless Charging: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Wireless Charging: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Wireless Charging: Bedienung nur im Stillstand möglich": "0x00",
                "Wireless Charging: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Statistik: Menüanzeige": "0x01",
                "Statistik: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Statistik: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Statistik: Bedienung nur im Stillstand möglich": "0x00",
                "Statistik: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Schiebedach: Menüanzeige": "0x01",
                "Schiebedach: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Schiebedach: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Schiebedach: Bedienung nur im Stillstand möglich": "0x00",
                "Schiebedach: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "FAS-Profile: Menüanzeige": "0x01",
                "FAS-Profile: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "FAS-Profile: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "FAS-Profile: Bedienung nur im Stillstand möglich": "0x00",
                "FAS-Profile: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "DAF (Daten für automatisiertes Fahren): Menüanzeige": "0x00",
                "DAF (Daten für automatisiertes Fahren): Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "DAF (Daten für automatisiertes Fahren): Bedienung bei v > V_Threshold_high möglich": "0x00",
                "DAF (Daten für automatisiertes Fahren): Bedienung nur im Stillstand möglich": "0x00",
                "DAF (Daten für automatisiertes Fahren): Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Mobilgerätetaste: Menüanzeige": "0x01",
                "Mobilgerätetaste: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Mobilgerätetaste: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Mobilgerätetaste: Bedienung nur im Stillstand möglich": "0x00",
                "Mobilgerätetaste: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "IAA_PSO: Menüanzeige": "0x01",
                "IAA_PSO: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "IAA_PSO: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "IAA_PSO: Bedienung nur im Stillstand möglich": "0x00",
                "IAA_PSO: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Mascot: Menüanzeige": "0x01",
                "Mascot: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Mascot: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Mascot: Bedienung nur im Stillstand möglich": "0x00",
                "Mascot: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "VAS: Menüanzeige": "0x01",
                "VAS: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "VAS: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "VAS: Bedienung nur im Stillstand möglich": "0x00",
                "VAS: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "PaCo: Menüanzeige": "0x01",
                "PaCo: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "PaCo: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "PaCo: Bedienung nur im Stillstand möglich": "0x00",
                "PaCo: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "EngineFunctions: Menüanzeige": "0x01",
                "EngineFunctions: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "EngineFunctions: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "EngineFunctions: Bedienung nur im Stillstand möglich": "0x00",
                "EngineFunctions: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "Reserviert72": "0x00",
                "Car2X: Menüanzeige": "0x01",
                "Car2X: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "Car2X: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "Car2X: Bedienung nur im Stillstand möglich": "0x00",
                "Car2X: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "ITM: Menuanzeige": "0x01",
                "ITM: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "ITM: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "ITM: Bedienung nur im Stillstand möglich": "0x00",
                "ITM: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "SoundControl2: Menüanzeige": "0x01",
                "SoundControl2: Bedienung auch bei Klemme 15 = Aus möglich": "0x00",
                "SoundControl2: Bedienung bei v > V_Threshold_high möglich": "0x01",
                "SoundControl2: Bedienung nur im Stillstand möglich": "0x00",
                "SoundControl2: Bedienung nur nach Anzeige eines Disclaimers möglich": "0x00",
                "FOD: Menu display": "0x00",
                "FOD: Operation with Klemme 15 OFF possible": "0x00",
                "FOD: Operation with v > V_Threshold_high possible": "0x00",
                "FOD: Operation only in the idle state possible": "0x00",
                "FOD: Operation only after displayed disclaimer possible": "0x00",
                "Reserviert72": "0x00",
                "Reserviert1": "0x00",
                "Reserviert2": "0x00",
                "Reserviert3": "0x00",
                "Reserviert4": "0x00",
                "Reserviert5": "0x00",
                "Reserviert6": "0x00",
                "Reserviert7": "0x00",
                "Reserviert8": "0x00",
                "Reserviert9": "0x00",
                "Reserviert10": "0x00",
                "Reserviert11": "0x00",
                "Reserviert12": "0x00",
                "Reserviert13": "0x00",
                "Reserviert14": "0x00",
                "Reserviert15": "0x00",
                "Reserviert16": "0x00",
                "Reserviert17": "0x00",
                "Reserviert18": "0x00",
                "Reserviert19": "0x00",
                "Reserviert20": "0x00",
                "Reserviert21": "0x00",
                "Reserviert22": "0x00",
                "Reserviert23": "0x00",
                "Reserviert24": "0x00",
                "Reserviert25": "0x00",
                "Reserviert26": "0x00",
                "Reserviert27": "0x00",
                "Reserviert28": "0x00",
                "Reserviert29": "0x00",
                "Reserviert30": "0x00",
                "Reserviert31": "0x00",
                "Reserviert32": "0x00",
                "Reserviert33": "0x00",
                "Reserviert34": "0x00",
                "Reserviert35": "0x00",
                "Reserviert36": "0x00",
                "Reserviert37": "0x00",
                "Reserviert38": "0x00",
                "Reserviert39": "0x00",
                "Reserviert40": "0x00",
                "Reserviert41": "0x00",
                "Reserviert42": "0x00",
                "Reserviert43": "0x00",
                "Reserviert44": "0x00",
                "Reserviert45": "0x00",
                "Reserviert46": "0x00",
                "Reserviert47": "0x00",
                "Reserviert48": "0x00",
                "Reserviert49": "0x00",
                "Reserviert50": "0x00",
                "Reserviert51": "0x00",
                "Reserviert52": "0x00",
                "Reserviert53": "0x00",
                "Reserviert54": "0x00",
                "Reserviert55": "0x00",
                "Reserviert56": "0x00",
                "Reserviert57": "0x00",
                "Reserviert58": "0x00",
                "Reserviert59": "0x00",
                "Reserviert60": "0x00",
                "Reserviert61": "0x00",
                "Reserviert62": "0x00",
                "Reserviert63": "0x00",
                "Reserviert64": "0x00",
                "Reserviert65": "0x00",
                "Reserviert66": "0x00",
                "Reserviert67": "0x00",
                "Reserviert68": "0x00",
                "Reserviert69": "0x00",
                "Reserviert70": "0x00",
                "Reserviert71": "0x00",
                "Reserviert73": "0x00",
                "Reserviert74": "0x00",
                "Reserviert75": "0x00",
                "Reserviert76": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
            }
        },
        {
            "RDI": "0x0B1D",
            "Name": "Car Function List BAP",
            "Value": {
                "Reserviert1": "0x00",
                "Klima (Master, 0x01) Verfügbarkeit": "0x01",
                "Klima (Master, 0x01) Buszuordnung": "0x02",
                "Klima (Slave, 0x02) Verfügbarkeit": "0x01",
                "Klima (Slave, 0x02) Buszuordnung": "0x02",
                "Standheizung (0x03) Verfügbarkeit": "0x01",
                "Standheizung (0x03) Buszuordnung": "0x02",
                "Headup-Display (0x04) Verfügbarkeit": "0x01",
                "Headup-Display (0x04) Buszuordnung": "0x02",
                "ACC (0x05) Verfügbarkeit": "0x01",
                "ACC (0x05) Buszuordnung": "0x03",
                "Luftfederung / Dämpfung (0x06) Verfügbarkeit": "0x00",
                "Luftfederung / Dämpfung (0x06) Buszuordnung": "0x04",
                "Reifendruckkontrolle (0x07) Verfügbarkeit": "0x01",
                "Reifendruckkontrolle (0x07) Buszuordnung": "0x03",
                "Innenlicht (0x08) Verfügbarkeit": "0x01",
                "Innenlicht (0x08) Buszuordnung": "0x02",
                "Außenlicht (0x09) Verfügbarkeit": "0x01",
                "Außenlicht (0x09) Buszuordnung": "0x02",
                "Einparkhilfe (0x0A) Verfügbarkeit": "0x01",
                "Einparkhilfe (0x0A) Buszuordnung": "0x06",
                "VPS (0x0B) Verfügbarkeit": "0x01",
                "VPS (0x0B) Buszuordnung": "0x26",
                "Scheibenwischer / Komfort (0xC) Verfügbarkeit": "0x01",
                "Scheibenwischer / Komfort (0xC) Buszuordnung": "0x02",
                "Zentralverriegelung (0x0D) Verfügbarkeit": "0x01",
                "Zentralverriegelung (0x0D) Buszuordnung": "0x02",
                "Spiegel (0x0E) Verfügbarkeit": "0x01",
                "Spiegel (0x0E) Buszuordnung": "0x02",
                "Bordcomputer / MFA (0x0F) Verfügbarkeit": "0x01",
                "Bordcomputer / MFA (0x0F) Buszuordnung": "0x23",
                "Fahrersitz (0x10) Verfügbarkeit": "0x01",
                "Fahrersitz (0x10) Buszuordnung": "0x02",
                "Uhrzeit (0x11) Verfügbarkeit": "0x01",
                "Uhrzeit (0x11) Buszuordnung": "0x02",
                "Serviceintervallanzeige (0x12) Verfügbarkeit": "0x01",
                "Serviceintervallanzeige (0x12) Buszuordnung": "0x02",
                "Einheitenmaster (0x13) Verfügbarkeit": "0x01",
                "Einheitenmaster (0x13) Buszuordnung": "0x02",
                "UGDO (Universal Garage Door Opener) (0x14) Verfügbarkeit": "0x00",
                "UGDO (Universal Garage Door Opener) (0x14) Buszuordnung": "0x06",
                "Kompass (0x15) Verfügbarkeit": "0x00",
                "Kompass (0x15) Buszuordnung": "0x00",
                "Klima (Slave 2, 0x16) Verfügbarkeit": "0x00",
                "Klima (Slave 2, 0x16) Buszuordnung": "0x23",
                "Charisma (0x17) Verfügbarkeit": "0x01",
                "Charisma (0x17) Buszuordnung": "0x02",
                "NightVision (0x18) Verfügbarkeit": "0x00",
                "NightVision (0x18) Buszuordnung": "0x00",
                "LDW / HCA (Spurhalteassistent, 0x19) Verfügbarkeit": "0x01",
                "LDW / HCA (Spurhalteassistent, 0x19) Buszuordnung": "0x03",
                "SWA (Spurwechselassistent, 0x1A) Verfügbarkeit": "0x01",
                "SWA (Spurwechselassistent, 0x1A) Buszuordnung": "0x03",
                "AWV (Anhaltewegverkürzung, 0x1B) Verfügbarkeit": "0x01",
                "AWV (Anhaltewegverkürzung, 0x1B) Buszuordnung": "0x06",
                "Reserviert2": "0x00",
                "Reserviert3": "0x00",
                "Hybrid (0x1D) Verfügbarkeit": "0x00",
                "Hybrid (0x1D) Buszuordnung": "0x01",
                "SideView (0x1E) Verfügbarkeit": "0x00",
                "SideView (0x1E) Buszuordnung": "0x00",
                "Reversibler Gurtstraffer (0x1F) Verfügbarkeit": "0x01",
                "Reversibler Gurtstraffer (0x1F) Buszuordnung": "0x01",
                "Beifahrersitz (0x20) Verfügbarkeit": "0x00",
                "Beifahrersitz (0x20) Buszuordnung": "0x23",
                "Verkehrszeichenerkennung (0x21) Verfügbarkeit": "0x01",
                "Verkehrszeichenerkennung (0x21) Buszuordnung": "0x03",
                "Müdigkeitserkennung (0x22) Verfügbarkeit": "0x01",
                "Müdigkeitserkennung (0x22) Buszuordnung": "0x02",
                "BCmE (0x23) Verfügbarkeit": "0x01",
                "BCmE (0x23) Buszuordnung": "0x02",
                "Neigungswinkelanzeige (0x24) Verfügbarkeit": "0x01",
                "Neigungswinkelanzeige (0x24) Buszuordnung": "0x23",
                "Batteriemanagement (0x25) Verfügbarkeit": "0x00",
                "Batteriemanagement (0x25) Buszuordnung": "0x01",
                "Bremse (0x26) Verfügbarkeit": "0x01",
                "Bremse (0x26) Buszuordnung": "0x02",
                "Start/Stopp Gründe (0x27) Verfügbarkeit": "0x01",
                "Start/Stopp Gründe (0x27) Buszuordnung": "0x02",
                "Reserviert4": "0x00",
                "Reserviert5": "0x00 0x00 0x00",
                "TV-Tuner (BAP) (0x2C) Verfügbarkeit": "0x00",
                "TV-Tuner (BAP) (0x2C) Buszuordnung": "0x00",
                "Amplifier (0x2D) Verfügbarkeit": "0x00",
                "Amplifier (0x2D) Buszuordnung": "0x24",
                "RearSeatEntertainment (0x2E) Verfügbarkeit": "0x00",
                "RearSeatEntertainment (0x2E) Buszuordnung": "0x23",
                "Reserviert6": "0x00",
                "Reserviert7": "0x00 0x00 0x00",
                "eCall (0x33) Verfügbarkeit": "0x00",
                "eCall (0x33) Buszuordnung": "0x23",
                "MFL Jokerfunktion (0x34) Verfügbarkeit": "0x00",
                "MFL Jokerfunktion (0x34) Buszuordnung": "0x02",
                "Spezialfunktionen (0x35) Verfügbarkeit": "0x00",
                "Spezialfunktionen (0x35) Buszuordnung": "0x23",
                "Anhängerassistent (0x36) Verfügbarkeit": "0x00",
                "Anhängerassistent (0x36) Buszuordnung": "0x00",
                "ENI (0x37) Verfügbarkeit": "0x00",
                "ENI (0x37) Buszuordnung": "0x23",
                "Reserviert8": "0x00",
                "Reserviert9": "0x00",
                "Range Data (0x39) Verfügbarkeit": "0x00",
                "Range Data (0x39) Buszuordnung": "0x02",
                "Pedestrian Assist (0x3A) Verfügbarkeit": "0x01",
                "Pedestrian Assist (0x3A) Buszuordnung": "0x03",
                "Sitzpneumatik (0x3B) Verfügbarkeit": "0x00",
                "Sitzpneumatik (0x3B) Buszuordnung": "0x23",
                "Efficiency Assist (0x3C) Verfügbarkeit": "0x01",
                "Efficiency Assist (0x3C) Buszuordnung": "0x02",
                "Reserviert10": "0x00",
                "Reserviert11": "0x00",
                "Sitzmemory Fahrer hinten (0x3E) Verfügbarkeit": "0x00",
                "Sitzmemory Fahrer hinten (0x3E) Buszuordnung": "0x23",
                "Sitzmemory Beifahrer hinten (0x3F) Verfügbarkeit": "0x00",
                "Sitzmemory Beifahrer hinten (0x3F) Buszuordnung": "0x23",
                "Spoiler (0x40) Verfügbarkeit": "0x00",
                "Spoiler (0x40) Buszuordnung": "0x00",
                "FrontTrafficAssist (0x41) Verfügbarkeit": "0x00",
                "FrontTrafficAssist (0x41) Buszuordnung": "0x00",
                "ClimateMaster (0x42) Verfügbarkeit": "0x01",
                "ClimateMaster (0x42) Buszuordnung": "0x02",
                "Reserviert12": "0x00",
                "Reserviert13": "0x00",
                "Soundcontrol  (0x44) Verfügbarkeit": "0x00",
                "Soundcontrol  (0x44) Buszuordnung": "0x00",
                "Display Configuration (0x45) Verfügbarkeit": "0x01",
                "Display Configuration (0x45) Buszuordnung": "0x02",
                "Reserviert14": "0x00",
                "Reserviert15": "0x00",
                "ConnectionManager (0x47) Verfügbarkeit": "0x00",
                "ConnectionManager (0x47) Buszuordnung": "0x00",
                "WirelessCharging (0x48) Verfügbarkeit": "0x01",
                "WirelessCharging (0x48) Buszuordnung": "0x02",
                "Reserviert16": "0x00",
                "Reserviert17": "0x00",
                "Statistic (0x4A) Verfügbarkeit": "0x00",
                "Statistic (0x4A) Buszuordnung": "0x00",
                "SunRoof_Front (0x4B) Verfügbarkeit": "0x01",
                "SunRoof_Front (0x4B) Buszuordnung": "0x02",
                "SunRoof_Rear (0x4C) Verfügbarkeit": "0x01",
                "SunRoof_Rear (0x4C) Buszuordnung": "0x02",
                "FAS_Profile (0x4D) Verfügbarkeit": "0x01",
                "FAS_Profile (0x4D) Buszuordnung": "0x02",
                "RemoteServices (0x4E) Verfügbarkeit": "0x01",
                "RemoteServices (0x4E)  Buszuordnung": "0x02",
                "InfotainmentSettings (0x50) Verfügbarkeit": "0x00",
                "InfotainmentSettings (0x50)  Buszuordnung": "0x00",
                "DAF (Daten für automatisiertes Fahren) (0x51) Verfügbarkeit": "0x00",
                "DAF (Daten für automatisiertes Fahren) (0x51) Buszuordnung": "0x00",
                "IAA_PSO (0x52) Verfügbarkeit": "0x01",
                "IAA_PSO (0x52) Buszuordnung": "0x23",
                "Mascot (0x53) Verfügbarkeit": "0x00",
                "Mascot (0x53) Buszuordnung": "0x00",
                "VAS (0x54) Verfügbarkeit": "0x00",
                "VAS (0x54) Buszuordnung": "0x00",
                "PaCo (0x55) Verfügbarkeit": "0x01",
                "PaCo (0x55) Buszuordnung": "0x02",
                "Reserviert20": "0x00 0x00 0x00 0x00 0x00 0x00 0x00",
                "EngineFunctions (0x5D) Verfügbarkeit": "0x00",
                "EngineFunctions (0x5D) Buszuordnung": "0x00",
                "Reserviert18": "0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00",
                "Reserviert21": "0x00 0x00 0x00",
                "Car2X (0x61) Availability": "0x00",
                "Car2X (0x61) Bus assignment": "0x00",
                "Reserviert22": "0x00 0x00 0x00",
                "ITM (0x65) Availability": "0x00",
                "ITM (0x65) Bus assignment": "0x00",
                "SoundControl2 (0x66) Availability": "0x00",
                "SoundControl2 (0x66) Bus assignment": "0x00",
                "Reserviert19": "0x00"
            }
        },
        {
            "RDI": "0x0B26",
            "Name": "Headup display configuration",
            "Value": {
                "Kreuzungsdetailkarte - Übertragungsart": "0x00",
                "Kreuzungsdetailkarte - Komprimierungsart": "0x00",
                "Kreuzungsdetailkarte - Auflösung": "0x00"
            }
        },

        {
            "RDI": "0x0B2F",
            "Name": "Multi media data transfer",
            "Value": {
                "Datenträger": "0x00",
                "Optisches Laufwerk": "0x00",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0B33",
            "Name": "Bluetooth deactivation",
            "Value": {
                "Status": "0x01"
            }
        },
        {
            "RDI": "0x0B37",
            "Name": "Bluetooth sniff mode",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0B39",
            "Name": "Audio management input gain offset",
            "Value": {
                "TV Tuner": "0x80",
                "Am Fm Tuner - FM Band": "0x80",
                "Am Fm Tuner - AM Band": "0x80",
                "DAB Tuner": "0x80",
                "SDARS Tuner": "0x80",
                "TI Tuner": "0x80",
                "AUX IN": "0x80",
                "AUX Adapter": "0x80",
                "CD-Audio": "0x80",
                "DVD": "0x80",
                "MediaFilePlayer(MFP)": "0x80",
                "Bluetooth Audio(A2DP)": "0x80",
                "FM Tuner TA": "0x80",
                "Bluray": "0x80",
                "HDMI": "0x80",
                "Online Tuner": "0x80",
                "Airplay": "0x80",
                "Universal Plug and Play": "0x80",
                "Cloud": "0x80",
                "Personal Tuner": "0x80",
                "Piepton": "0x80",
                "Warnton": "0x80",
                "Touchscreenton": "0x80",
                "Nachrichtenton": "0x80",
                "DMB on ExBox": "0x80",
                "Mirrorlink": "0x80",
                "Navigation Anleitung": "0x80",
                "Speech Control System": "0x80",
                "Phone Voice": "0x80",
                "Klingelton Media FilePlayer": "0x80",
                "OutBand Phone Klingelton": "0x80",
                "Handsfree": "0x80",
                "TV_AV-IN": "0x80",
                "Reserviert": "0x00"
            }
        },

        {
            "RDI": "0x0B43",
            "Name": "WLAN modul activation",
            "Value": {
                "Status": "0x01",
                "Reserviert": "0x00"
            }
        },
        {
            "RDI": "0x0B48",
            "Name": "Startup Screen Sticker (HMI)",
            "Value": {
                "Startbildschirm Sticker (HMI) Parameter": "0x00 0x00"
            }
        },
        {
            "RDI": "0x0B49",
            "Name": "Media country code",
            "Value": {
                "Verkaufsland": "0x43 0x4E"
            }
        },
        {
            "RDI": "0x0B5A",
            "Name": "Dashboard display configuration",
            "Value": {
                "Navigationskarte - Übertragungsart": "0x01",
                "Navigationskarte - Komprimierungsart": "0x01",
                "Navigationskarte - Auflösung": "0x01",
                "Kreuzungsdetailkarte - Übertragungsart": "0x00",
                "Reserviert": "0x00",
                "Kreuzungsdetailkarte - Auflösung": "0x01",
                "Coverart": "0x01",
                "Stationart": "0x01",
                "Callpicture": "0x01",
                "Dynamisches Icon": "0x01",
                "Map Switch": "0x00",
                "Reserviert2": "0x00"
            }
        },
        {
            "RDI": "0x0E38",
            "Name": "Navigation GNSS receiver setting",
            "Value": {
                "Default-Hardware Empfang": "0x00",
                "GPS": "0x01",
                "Galileo": "0x00",
                "GLONASS": "0x00",
                "Kompass": "0x00",
                "Externes GPS 1": "0x00",
                "Externes GPS 2": "0x00",
                "BEIDOU": "0x00",
                "GNSS Aktualisierungsfrequenz": "0x00",
                "Reserviert2": "0x00"
            }
        },
        {
            "RDI": "0x1021",
            "Name": "BAP debug mode release",
            "Value": {
                "BAP Debug Mode": "0x00"
            }
        },
        {
            "RDI": "0x243F",
            "Name": "Developer testmode",
            "Value": {
                "Parameter Entwicklermenü": "0x01"
            }
        },
        {
            "RDI": "0x2442",
            "Name": "Mobile phone voice control availability",
            "Value": {
                "Apple Gerät": "0x01",
                "Sonstige Geräte": "0x01",
                "Reserviert": "0x00"
            }
        }
    ]
}



class Sub(HU):
    init_dict = {
        'p_read_script1': [{'expect': 'password'}, {'sendline': 'root'}, {'expect': 'root@'}, {'sendline': 'cd /tmp/'},
                           {'expect': '/tmp'}]}

    @staticmethod
    def create_json_file(json_data, ns="0x01000000"):
        """

        :param json_data:
        :param ns: like 0x01000000
        :return: completed json_data
        """
        RDI_list = jsonpath.jsonpath(json_data, "$..RDI")
        """
        >> ['0x04FB', '0x04FC', '0x04FE', '0x0505', '0x050E', '0x050F']
        """
        for key in RDI_list:
            if key == "0x7213":
                print('we found it')
            Sub.init_dict['p_read_script1'].append(
                {"sendline": "tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns, key)})
            # print("type of %s is" % key, type(key))
            Sub.init_dict['p_read_script1'].append(
                # {"sendline": "load: ns: {0} key: {1} slot: 0 status: 0".format(ns[3:], str(int(key,16)))})
                {"expect": "load: ns: {0} key: {1} slot: 0 ".format(ns[3:], str(int(key, 16)))})
        Sub.init_dict['p_read_script1'].append({'sendline': 'sync'})
        Sub.init_dict['p_read_script1'].append({'sendline': 'exit'})
        return Sub.init_dict


class setGetKey(Sub):
    ns_0x04000000 = ['29185', '29187', '29188', '29190', '29193', '29195', '29196', '29197', '29200', '29201', '29202', '29203', '29206']
    ns_0x01000100 = ['2843']
    ns_0x01000000 = ['1276']
    @staticmethod
    def create_json_file(json_data, ns="0x01000000"):
        RDI_list = jsonpath.jsonpath(json_data, "$..RDI")
        for key in RDI_list:
            setGetKey.init_dict['p_read_script1'].append(
                {"sendline": "tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns, key)})
            # print("type of %s is" % key, type(key))
            # """Set the final expect command"""
            with open('logs_0908.txt', 'r') as file:
                for line in file:
                    # print('type of %s: %s' %(key,type(key)))
                    if line.startswith('load') and line.find(str(int(key,16))) != -1:
                        setGetKey.init_dict['p_read_script1'].append({"expect": line.rstrip('\n')})
        # Sub.init_dict['p_read_script1'].append(
        #      {"sendline": "load: ns: {0} key: {1} slot: 0 status: 0".format(ns[3:], str(int(key,16)))})
        #      {"expect": "load: ns: {0} key: {1} slot: 0 ".format(ns[3:], str(int(key, 16)))})
        setGetKey.init_dict['p_read_script1'].append({'sendline': 'sync'})
        setGetKey.init_dict['p_read_script1'].append({'sendline': 'exit'})
        # rename key in dictionary
        setGetKey.init_dict['p_setGetKey_script1'] = setGetKey.init_dict.pop('p_read_script1')
        return setGetKey.init_dict

    @staticmethod
    def get_json_info(json_file_name, jsonPathDesc):
        """
        :param json_file_name:
        :param jsonPathDesc:
        :return: dict(json's data)
        """
        import json, jsonpath
        # with open(os.getcwd() + '/json_sets/' + "p_script1.json") as json_file:
        with open(os.getcwd() + '/json_sets/' + json_file_name) as json_file:
            data = json.load(json_file)
            res = jsonpath.jsonpath(data, jsonPathDesc)
        return res

    @staticmethod
    def adv_doPexpect(p_command, json_name, jsonpath_command):
        with open("Getkey_logs_0908.txt", 'w') as my_log_file:
            setGetKey.greenFont(setGetKey.repr_message("Start to pexpect...."))
            p = pexpect.spawn(command=p_command, logfile=my_log_file, encoding='utf-8', timeout=30)
            # json_list = HU.get_json_info("p_script1.json", "$.p_script1.*")
            json_list = setGetKey.get_json_info(json_name, jsonpath_command)
            for i in json_list:
                # print(i)
                setGetKey.pAction(list(i.items())[0], p)
            p.close()
            # return HU.greenFont(HU.repr_message("Success to copy file to HU"))
            return setGetKey.greenFont(setGetKey.repr_message("Successful"))


if __name__ == '__main__':

    # data = json.load(json_file)
    # print(A.create_json_file())
    # data = json.load(A.create_json_file())
    # json_read_script1 = json.dumps(, indent=4, separators=(", ", " : "))
    # print(json_read_script1)
    # sys.exit()

    # '/bin/bash -c "ssh root@192.168.1.4 | grep load: > logs_0908.txt'
    #

    """
    test code
    """
    #
    # RDI_list = jsonpath.jsonpath(json_data, "$..RDI")
    # # print(len(RDI_list))
    # # print(RDI_list)
    # a = [int(x,16) for x in RDI_list]
    # with open('json_sets/json_setData_script1.json') as file:
    #     setData_list = json.load(file)
    # # print(setData_list)
    # b = [int(x, 16) for x in setData_list]
    # # "0x%s" % str(hex(int(key))).upper()[2:]
    # for i in set(a)^set(b):
    #     print("0x%s" % str(hex(int(i))).upper()[2:])
    #
    # sys.exit()
    """
    uncomment below before exec
    Part1. collect the Getkey raw data in first.
    """
    # A = Sub()
    # print(A.__class__)
    # json.dump(A.create_json_file(json_data, ns="0x01000000"),
    #           open(os.getcwd() + '/json_sets/json_read_script1.json', 'w'), ensure_ascii=False,
    #           indent=4, separators=(", ", " : "))
    #
    # print(A.adv_doPexpect(p_command="ssh root@192.168.1.4", json_name="json_read_script1.json",
    #                       jsonpath_command="$.{0}.*".format("p_read_script1")))
    # print(A.greenFont(A.repr_message("Part1. collect the Getkey raw data in first.")))
    # sys.exit()
    """
    Part2. creat json_setGetKey_script1.json by former part1 exec. 
    """

    B = setGetKey()
    json.dump(B.create_json_file(json_data, ns="0x01000000"),
              open(os.getcwd() + '/json_sets/json_setGetKey_script1.json', 'w'), ensure_ascii=False,
              indent=4, separators=(", ", " : "))

    print(B.adv_doPexpect(p_command="ssh root@192.168.1.4", json_name="json_setGetKey_script1.json",
                          jsonpath_command="$.{0}.*".format("p_setGetKey_script1")))
    print(B.greenFont(B.repr_message(" Part2. creat json_setGetKey_script1.json by former part1 exec..")))

    sys.exit()
    """
    sys.exit()
    """

    RDI_list = jsonpath.jsonpath(json_data, "$..RDI")
    print(RDI_list)

    # json_p_script1 = json.dumps(p_read_script1, indent=4, separators=(", ", " : "))
    print(json_p_script1)
    print(json.loads(json_p_script1))

    # json_p_script1 = json.dumps(files_checksum_script, indent=4, separators=(", ", " : "))
    # json.dump(files_checksum_script, open(os.getcwd() + '/json_sets/p_check_script1.json', 'w'), ensure_ascii=False, indent=4,
    #           separators=(", ", " : "))

    sys.exit()


    def transfer_files(cls, RDI_List):
        for i in RDI_List:
            # cls.doPexpect(cls.copy_file_to_HU(i))
            print(cls.adv_doPexpect(cls.copy_file_to_HU(i), "p_script1.json", "$.p_script1.*"))
            # print(cls.copy_file_to_HU(i))


    transfer_files(A, fileList)

    fileList = os.listdir(os.getcwd() + "/tools")


    def transfer_files(cls, fileList):
        for i in fileList:
            # cls.doPexpect(cls.copy_file_to_HU(i))
            print(cls.adv_doPexpect(cls.copy_file_to_HU(i), "p_script1.json", "$.p_script1.*"))
            # print(cls.copy_file_to_HU(i))


    transfer_files(A, fileList)
    p_command = "ssh root@192.168.1.4"
    print(A.adv_doPexpect(p_command, "p_check_script1.json", jsonpath_command="$.p_check_script1.*"))
