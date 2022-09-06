#!/usr/bin/python3.5


adaption_data = {
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
    }
    ]
}

def set_random_dict(set_loopNum = 20):
# set_loopNum = 100
    import random, string, names
    # list1 = [x for x in range(set_loopNum)]
    # list2 = [y**2 for y in range(100)]
    list1 = [names.get_full_name() for i in range(set_loopNum)]
    list2 = [random.randint(1,10) for i in range(set_loopNum)]
    # print(list2)
    res_dict = dict(zip(list1, list2))
    return res_dict


def get_value(adaption_data,RDI:str):
    value = jsonpath.jsonpath(adaption_data, '$.Adaptions[*].Value')
    return list(jsonpath.jsonpath(adaption_data, '$.Adaptions[?(@.RDI == "'+ RDI +'")].Value')[0].values())


if __name__ == '__main__':
    import jsonpath
    import re
    # from jsonpath import jsonpath
    RDI = jsonpath.jsonpath(adaption_data, '$..RDI')
    print(RDI)
    for i in RDI:
        print(get_value(adaption_data,i))
    # print(get_value(adaption_data,'0x0505'))


    # ret = jsonpath.jsonpath(adaption_data, '$.Adaptions[*].Value')
    # ret = list(jsonpath.jsonpath(adaption_data, '$.Adaptions[?(@.RDI == "0x0505")].Value')[0].values())
    # print(len(ret))


    # for i in ret:
    #     if len(i) > 1:
    #         print('dict length is more than 1')
    #         print(i)

    # raw_value = [list(x.values()) if len(x) > 1 else list(x.values()) for x in ret]
    # for i in range(len(raw_value)):
    #     temp = ''
    #     for j in raw_value[i]:
    #         if re.findall('0x[A-Z0-9]', j):
    #             temp += '0'
    #     raw_value[i] = temp
    # print(raw_value)

    # print(len(set_random_dict()))
    # example_dict1 = set_random_dict()
    # print(example_dict1.keys())
    # res = ""
    # for i in example_dict1.keys():
    #     res = res + i
    # print(res)