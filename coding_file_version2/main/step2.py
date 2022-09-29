"""
python3.5
"""
import json
import os, sys
import pprint
import time

import jsonpath
import pexpect

from step1 import S1,JSON
import copy


class S2(S1,JSON):
    def __init__(self):
        S1.__init__(self)
        JSON.__init__(self, json_list=[], json_dict={})
        self.json_dict = {}
        self.codingFiles_dir = ""
        self.nsKey_dict_list = []

    def set_codingFiles(self,path):
        self.codingFiles_dir = self.project_dir + path


    def set_nsKey_dict(self, fileName):
        """
        only read first two columns, which are column 1 and column 2
        :param fileName:
        :return: dict{column2 : column1}
        """
        with open(self.codingFiles_dir + "/" + fileName, 'r') as file, open(self.log_name, "w") as logs:
            file = file.readlines()
            column_name_list = file[0].split()
            print(column_name_list[:3])
            condition = "yes"
            # sys.exit()
            # file = file.readlines()[2:]  # way1 :  # skip the first two line.
            for line in file[1:]:
                if line != "\n":
                    logs.write(str(dict(zip(column_name_list[:3],[x for x in line.split()[:3]]))) + '\n')
                    self.nsKey_dict_list.append(dict(zip(column_name_list[:3], [x for x in line.split()[:3]])))
            # pprint.pprint(self.nsKey_dict_list)

    @staticmethod
    def saveAsFile(file_path, file_name,json_data):
        json.dump(json_data, open(file_path + "/" + file_name, 'w'), ensure_ascii=False,
                  indent=4, separators=(", ", " : "))

    def add_send_expect(self, strS, strE, str_ns, str_key):
        # if not self.json_dict.get("expect",None) and not self.json_dict.get("sendline", None):
        newDict = {}
        newDict["ns"] = str_ns
        newDict["key"] = str_key
        newDict["sendline"] = strS
        newDict["expect"] = strE
        self.json_list.append(newDict)

    def set_pexpect_command(self, json_path, json_file, log_path):
        with open("{0}/{1}".format(json_path, json_file + ".json"), encoding="utf-8") as json_data, \
                open(log_path, 'a')as logs:
            # with open("{0}/{1}".format(json_path, json_file + ".json"), encoding="utf-8") as json_data:
            data = json.load(json_data)
            #     res = jsonpath.jsonpath(data, "$.body..expect")
            #     print("{0}:\n{1}",("res",res))

            spawn_command = jsonpath.jsonpath(data, "$.head..spawn_command")[0]
            logs.write(spawn_command + "\n")
            # print("{0}:\t{1}".format("spawn_command",spawn_command))
            # print("Logs : ", logs)
            if not False:
                logs.write(
                    "pexpect.spawn(command={0}, , logfile={1}, encoding={2}, timeout={3})\n".format(spawn_command, logs,
                                                                                                    "utf-8", "20"))
                try:
                    # p = pexpect.spawn(command=spawn_command, logfile=sys.stdout, encoding='utf-8', timeout=10)
                    p = pexpect.spawn(command=spawn_command, logfile=logs, encoding='utf-8', timeout=10)
                    spawn_command_expect = jsonpath.jsonpath(data, "$.head..spawn_command_expect")[0]
                    # print("type of {0} is {1}".format("spawn_command_expect",type(spawn_command_expect)))
                    logs.write("p.expect({0})\n".format(spawn_command_expect))
                    p.expect(spawn_command_expect)
                    # sys.exit()
                    # print(jsonpath.jsonpath(data, "$.head[?(@.expect)]"))
                    for ele_dict in (
                    jsonpath.jsonpath(data, "$.head[?(@.sendline)]"), jsonpath.jsonpath(data, "$.body[?(@.sendline)]"), \
                    jsonpath.jsonpath(data, "$.tail[?(@.sendline)]")):
                        for i in ele_dict:
                            # print("{0}:\t{1}".format("i", i))
                            # S1.pAction_v2(i,cls= p, logFile=sys.stdout)
                            S1.pAction_v2(i, cls=p)
                except pexpect.TIMEOUT:
                    # raise TimeoutError("timeout no match")
                    print(S1.repr_message("pexpect.TIMEOUT"))

    # @staticmethod
    # def save_like_a_json(jsonData, fileName='ns1000000.json', localPath=os.getcwd() + '/json_sets/'):
    #     return json.dump(jsonData, open(localPath + fileName, 'w'), ensure_ascii=False,
    #                      indent=4, separators=(", ", " : "))
# class Sub_json(JSON):
#     Sub_json.
#     JSON.__init__(self, json_list=[], json_dict={})
#     pass


if __name__ == '__main__':
    HU = S2()
    HU.setProjectDir("/home/jpcc/PycharmProjects/pythonProject_Sept_2022/coding_file_version2")
    HU.setLogDir("/logs")
    HU.setJsonDir("/json")
    HU.log_name += "/step2_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
    print("{0}:\t{1}".format("HU.log_dir", HU.log_name))
    # sys.exit()
    HU.set_codingFiles("/codingFiles")
    print(HU.codingFiles_dir)
    codingFiles_name = HU.codingFiles_dir + "/" + "VW_GP_CHN_v0.9.json"
    # print(HU.get_json_info(codingFiles_name, "$.coding", codingFormat="utf_8_sig"))
    print(HU.get_json_info(codingFiles_name, "$.Adaptions..RDI", codingFormat="utf_8_sig"))
    print(HU.get_json_info(codingFiles_name, "$.Datasets..RDI", codingFormat="utf_8_sig"))


    # E_json = Sub_json()
    # Adaption_List = HU.get_json_info(codingFiles_name, "$.Adaptions..RDI", codingFormat="utf_8_sig")
    # for i in Adaption_List:
    #     # tsd.persistence.client.mib3.app.GetKey --ns 0x4000000 --key 0x7203
    #     E_json.add_send_expect("tsd.persistence.client.mib3.app.GetKey --ns 0x{0} --key {1}".format(i), "{0}  {1}".format(HU.getFilesSha1sum()[i], i))
    HU.set_nsKey_dict("RecordDataIdOverview_0927.txt")
    HU.setJsonDir("/json")
    print("{0}:\t{1}".format("HU.json_dir", HU.json_dir))
    HU.saveAsFile(HU.json_dir, "rawData_DataId" + ".json", HU.nsKey_dict_list)
    rawDataFile = HU.json_dir +"/" + "rawData_DataId.json"
    ns_list = HU.get_json_info(rawDataFile, "$..Namespace_hex", codingFormat="utf_8_sig")
    key_list = HU.get_json_info(rawDataFile, "$..Key", codingFormat="utf_8_sig")
    for ns,key in zip(ns_list,key_list):
        if ns.startswith("0x") and key.startswith("0x"):
            HU.add_send_expect(strS = "./tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns,key)\
                               ,strE = "load: ns: {0} key: {1} slot: 0".format(ns[2:], int(key,16)),\
                               str_ns = ns, str_key = key)

    HU.combineAsJson_v2()
    HU.saveAsFile(HU.json_dir, "DataId_0929" + ".json",  HU.json_dict)   # save as jsonFile











    # "$..RDI")
    # print(len(RDI_list))
    # print(RDI_list)
    # a = [int(x,16) for x in RDI_list]
    # with open('json_sets/json_setData_script1.json') as file:
    #     setData_list = json.load(file)
    # # print(setData_list)
    # b = [int(x, 16) for x in setData_list]
    # # "0x%s" % str(hex(int(key))).upper()[2:]
    # for i in set(a)^set(b):
    #     print("0x%s" % str(hex(int(i))).upper()[2:])
    # #

