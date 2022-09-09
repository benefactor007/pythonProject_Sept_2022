#!/usr/bin/python3.5
import pexpect

from sub_action import Sub

import os, sys, json

class data_analysis(Sub):
    data_dict = {}
    errorKey_list = []
    files_login_script = {'p_login_script1':
        [
            {'expect': 'password'},
            {'sendline': 'root'},
            {'expect': 'root@'},
            {'sendline': "cd /tmp/"},
            {'expect': "/tmp"},
            {'sendline': 'sync'},
            {'sendline': 'exit'},
        ]
    }
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
#     @staticmethod
#     def adv_doPexpect(p_command, json_name, jsonpath_command):
#         with open("logs_0909.txt", 'w') as my_log_file:
#             p = pexpect.spawn(command=p_command, logfile=my_log_file, encoding='utf-8', timeout=60)
#             # json_list = HU.get_json_info("p_script1.json", "$.p_script1.*")
#             json_list = new_sub.get_json_info(json_name, jsonpath_command)
#             for i in json_list:
#                 print(i)
#                 new_sub.pAction(list(i.items())[0], p)
#                 # print("%s pass"%(i))
#             p.close()
#             # return HU.greenFont(HU.repr_message("Success to copy file to HU"))
#             return new_sub.greenFont(new_sub.repr_message("Successful"))


if __name__ == '__main__':
    data_analysis.catch_loads("logs.txt")
    # print(data_analysis.data_dict)
    print(data_analysis.errorKey_list)
    print("len: %s" % len(data_analysis.errorKey_list))
    for i in data_analysis.errorKey_list:
        # print("0x%s" % str(hex(int(i))).upper()[2:])
        print(str(hex(int(i))).upper()[2:])
    json.dump(data_analysis.data_dict,
              open(os.getcwd() + '/json_sets/json_setData_script1_v3.json', 'w'), ensure_ascii=False,
              indent=4, separators=(", ", " : "))

    # p_command = "ssh root@192.168.1.4"
    # with open("find_key_1276_v2.txt", 'w') as my_log_file:
    #     p = pexpect.spawn(command=p_command, logfile=my_log_file, encoding='utf-8', timeout=60)
    #     p.expect("password")
    #     p.sendline("root")
    #     p.expect("root@")
    #     p.sendline("cd /tmp/")
    #     p.expect("/tmp")
    #     for i in range(1,1000000,100):
    #         p.sendline("tsd.persistence.client.mib3.app.GetKey --ns 0x{0} --key 0x04FC".format(i))
    #         p.expect("load:")
    #     p.sendline("sync")
    #     p.sendline("exit")
