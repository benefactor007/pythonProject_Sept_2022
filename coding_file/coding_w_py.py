#!/usr/bin/python3.5
import jsonpath as jsonpath

car_func_list_BAP = "00 42 42 42 42 43 04 43 42 42 46 66 42 42 42 63 42 42 42 42 06 00 23 42 00 43 43 46 00 01 00 41 23 43 42 42 63 01 42 42 00 00 00 00 00 24 23 00 00 00 00 23 02 23 00 23 00 02 43 23 42 00 23 23 00 00 42 00 00 42 00 00 42 00 00 42 42 42 42 00 00 00 63 00 00 42 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"


# print(hex(68))
# print(int(0x04))
# print(hex(4))


def greenFont(str):
    return "\033[32m" + str + "\033[0m"


def repr_message(message: str):
    padding_len = '%' + str(int(len(message) / 2) + 35) + 's'
    return "=" * 70 + "\n" + padding_len % message + "\n" + "=" * 70 + "\n"


def read_cfg(fileName=None):
    fileName = 'part_coding.txt'
    with open(fileName, 'r') as file:
        for line in file:
            print(line)
        # print(file.readline())


# data = '''
#     {"RDI": "0x0B1D","Name": "Car Function List BAP"}'''

json_data = """
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
}
        """
json_adaption = {
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
        }
    ]
}

if __name__ == '__main__':
    import json
    import demjson
    # use jsonpath
    import jsonpath

    # from jsonpath import jsonpath
    RDI = jsonpath.jsonpath(json_adaption, '$..RDI')
    print(RDI)
    ret = jsonpath.jsonpath(json_adaption, '$.Adaptions[*].Value')
    print(len(ret))
    for i in ret:
        print(i.values())
        print(len(i.values()))
        # "Name": "Car Function List BAP"
    sub_value = jsonpath.jsonpath(json_adaption, '$.Adaptions[?(@.Name == "Car Function List BAP")].RDI')
    print(sub_value)

    a = jsonpath.jsonpath(json_adaption, '$.Adaptions[?(@.RDI == "0x0B1D")].Value')
    # print(type(a[0]))
    print('='*66)
    print(a[0])
    print('=' * 66)
    print('type of a', type(a))
    print(a[0]['Reserviert1'])
    print([x.keys() for x in a])
    car_func_list = [x for x in a[0].keys()]
    print(car_func_list)
    import re
    temp = []
    for i in range(len(car_func_list)):
        # temp = car_func_list[i]
        if not re.search('0x[A-Z0-9]{2}', car_func_list[i]) or not re.search('0x[A-Z0-9]{2}', car_func_list[i + 1]):
            print('>>' + a[0][car_func_list[i]] + '<<')
            for i in a[0][car_func_list[i]].split():
                print(temp.append(i))
            # temp.append(a[0][car_func_list[i]])
        else:
            if re.search('0x[A-Z0-9]{2}', car_func_list[i]).group() == re.search('0x[A-Z0-9]{2}', car_func_list[i+1]).group():
                # print('yes')
                # print(a[0][car_func_list[i]] + '\n' + a[0][car_func_list[i+1]])
                print(a[0][car_func_list[i]] + ' '+ a[0][car_func_list[i + 1]])
                temp.append(a[0][car_func_list[i]] + ' '+ a[0][car_func_list[i + 1]])
    print(temp)
    print(len(temp))
    # print(a)
    # print(ret[0].values())

    # End here

    # load_data = json.loads(json_adaption)
    # data = load_data['Adaptions']
    # ret = []
    # for i in data:
    #     ret.append(jsonpath.jsonpath(i, '$..RDI'))
    # print(ret)

    # load_data = json.loads(json_adaption)
    # # data = load_data.get("Adaptions")
    # data = load_data['Adaptions']
    # result = []
    # for i in data:
    #     # result.append(i.get("Value"))
    #     result.append(jsonpath.jsonpath(i,'$..Value.*'))
    # print(result)

# if __name__ == '__main__':
#     print("".join(car_func_list_BAP.split()))
#     # read_cfg()
#     import json
#     import re
#     datadict = json.loads(data)
#     # print(datadict)
#     print(type(datadict))
#     # print(datadict.keys('Value').keys('Reifendruckkontrolle (0x07) Verfügbarkeit'))
#     print([i for i in datadict.keys()])
#     print(datadict['Value']['Klima (Master, 0x01) Verfügbarkeit'])
#     print([i for i in datadict['Value'].keys()])
#     valueList = [i for i in datadict['Value'].keys()]
#     newdict = sorted(datadict['Value'].keys())
#     print(newdict)
#     # for i in valueList:
#     #     print(i)
#     #     new_i = re.search('0x[A-Z0-9]{2}',i).group()
#     #     print(new_i)
#     #     datadict['Value'][new_i] = datadict['Value'][i]
#     print([i for i in datadict['Value'].keys()])
#
#
#     def json_tran_list(str_json):
#         list = json.loads(str_json)
#         return list
#
#     print(json_tran_list(data))
#
#     # print([datadict['Value'][x] for x in ([i for i in datadict['Value'].keys()])])
