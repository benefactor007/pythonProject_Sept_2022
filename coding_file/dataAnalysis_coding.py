#!/usr/bin/python3.5

from sub_action import Sub

import os, sys, json

class data_analysis(Sub):
    data_dict = {}
    @staticmethod
    def catch_loads(fileName = "logs.txt"):
        with open(fileName, 'r') as my_file:
            for line in my_file:
                if line.startswith("load"):
                    print("ns: %s" % line[line.index("ns: ")+4:line.index("key")-1])
                    key = line[line.index("key: ") + 5:line.index("slot") - 1]
                    print("key: %s" % key)
                    print("status: %s" % line[line.index("status: ") + 8:line.index("data") - 1])
                    data = line[line.index("data: ") + 5:]
                    print("data: %s" % data)
                    data_analysis.data_dict["0x%s" % str(hex(int(key))).upper()[2:]] = "0x" + "".join([x.upper() for x in data.split()])
#                   [x.upper() for x in b.split()]



if __name__ == '__main__':
    data_analysis.catch_loads()
    print(data_analysis.data_dict)
    json.dump(data_analysis.data_dict,
              open(os.getcwd() + '/json_sets/json_setData_script1.json', 'w'), ensure_ascii=False,
              indent=4, separators=(", ", " : "))