#!/usr/bin/python3.5

from sub_action import Sub

import os, sys, json

class data_analysis(Sub):
    data_dict = {}
    errorKey_list = []
    @staticmethod
    def catch_loads(fileName = "logs_0908.txt"):
        with open(fileName, 'r') as my_file:
            for line in my_file:
                if line.startswith("load"):
                    print(line.rstrip('\n'))
                    print("ns: %s" % line[line.index("ns: ")+4:line.index("key")-1])
                    key = line[line.index("key: ") + 5:line.index("slot") - 1]
                    print("key: %s" % key)
                    status = "status: %s" % line[line.index("status: ") + 8:line.index("data") - 1]
                    print("status: %s" % status)
                    print(data_analysis.repr_message(status))
                    if status == 'status: 8':
                        data_analysis.errorKey_list.append(key)
                    data = line[line.index("data: ") + 5:]
                    # .rstrip('\n')
                    print("data: %s" % data)
                    data_analysis.data_dict["0x%s" % str(hex(int(key))).upper()[2:]] = "0x" + "".join([x.upper() for x in data.split()])
#                   [x.upper() for x in b.split()]



if __name__ == '__main__':
    data_analysis.catch_loads("Getkey_logs_0908.txt")
    # print(data_analysis.data_dict)
    print(data_analysis.errorKey_list)
    print("len: %s" % len(data_analysis.errorKey_list))
    for i in data_analysis.errorKey_list:
        # print("0x%s" % str(hex(int(i))).upper()[2:])
        print(str(hex(int(i))).upper()[2:])
    # json.dump(data_analysis.data_dict,
    #           open(os.getcwd() + '/json_sets/json_setData_script1_v1.json', 'w'), ensure_ascii=False,
    #           indent=4, separators=(", ", " : "))