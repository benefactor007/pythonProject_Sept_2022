""""
Use Python3.5
"""
import json
import pprint
import sys, os
import time

import jsonpath
import pexpect


class JSON:

    def __init__(self, json_list=[], json_dict={}):
        self.json_list = json_list
        self.json_dict = json_dict
        self.user = "root"
        self.ip = "192.168.1.4"

    def add_send_expect(self, strS, strE, str_ns="", str_key="", str_data=""):
        # if not self.json_dict.get("expect",None) and not self.json_dict.get("sendline", None):
        newDict = {}
        newDict["ns"] = str_ns
        newDict["key"] = str_key
        newDict["sendline"] = strS
        newDict["expect"] = strE
        newDict["data"] = str_data
        self.json_list.append(newDict)

    def combineAsJson_v2(self):
        haed_dict = {
            "{0}".format("head"): [
                {"spawn_command": "ssh {0}@{1}".format(self.user, self.ip), 'spawn_command_expect': 'password'},
                {'sendline': 'root', 'expect': 'root@'},
                {'sendline': 'cd /tmp/', 'expect': '/tmp'}
            ]
        }
        tail_dict = {'{0}'.format("tail"): [{"sendline": "sync", "expect": "vw-infotainment"},
                                            {"sendline": "exit", "expect": "Connection to 192.168.1.4 closed"}]}
        self.json_dict["body"] = self.json_list
        self.json_dict.update(haed_dict)
        self.json_dict.update(tail_dict)
        # self.json_dict[elementName].update(tail_dict)

    @staticmethod
    def saveAsFile(file_path, file_name, json_data):
        json.dump(json_data, open(file_path + "/" + file_name, 'w'), ensure_ascii=False,
                  indent=4, separators=(", ", " : "))

    # @staticmethod
    # def save_like_a_json(jsonData, fileName='ns1000000.json', localPath=os.getcwd() + '/json_sets/'):
    #     return json.dump(jsonData, open(localPath + fileName, 'w'), ensure_ascii=False,
    #                      indent=4, separators=(", ", " : "))

    def __str__(self):
        return "{0}\n{1}".format(self.json_list, self.json_dict)
        # return self.json_dict


class P_step1(JSON):
    def __init__(self):
        JSON.__init__(self)
        self.project_dir = ""
        self.json_dir = ""
        self.tools_dir = ""
        self.log_name = ""
        self.log_mode = "w"
        self.processList = []
        self.json_dict = {}
        self.codingFiles_dir = ""
        self.nsKey_dict_list = []
        self.error_name = ""
        self.key_data_list = []
        self.error_key_data_list = []

    def setProjectDir(self, path):
        self.project_dir = path

    def setJsonDir(self, path):
        self.json_dir = self.project_dir + path

    def setToolsDir(self, path):
        self.tools_dir = self.project_dir + path

    def setLogDir(self, path):
        self.log_name = self.project_dir + path

    def set_codingFiles(self, path):
        self.codingFiles_dir = self.project_dir + path

    def setErrorDir(self, path):
        self.error_name = self.project_dir + path

    @staticmethod
    def get_json_info(json_file_name, jsonPathDesc, codingFormat=None):
        """
      :param json_file_name:
      :param jsonPathDesc:
      :return: dict(json's data)
      """
        import json, jsonpath
        # print(P_step1.repr_message(json_file_name))
        with open(json_file_name, encoding=codingFormat) as json_file:
            data = json.load(json_file)
            res = jsonpath.jsonpath(data, jsonPathDesc)
        return res

    @staticmethod
    def greenFont(str):
        return "\033[32m" + str + "\033[0m"

    @staticmethod
    def redFont(str):
        return "\033[31m" + str + "\033[0m"

    @staticmethod
    def repr_message(message: str):
        padding_len = '%' + str(int(len(message) / 2) + 35) + 's'
        return "\n" + "=" * 70 + "\n" + padding_len % message + "\n" + "=" * 70 + "\n"

    def set_nsKey_dict(self, fileName):
        """
        only read first two columns, which are column 1 and column 2
        :param fileName:
        :return: dict{column2 : column1}
        """
        with open(self.codingFiles_dir + "/" + fileName, 'r') as file, open(self.log_name, "w") as logs:
            file = file.readlines()
            column_name_list = file[0].split()
            print("{0}:\t{1}".format("column_name_list[:]", column_name_list[:]))
            condition = "yes"
            # sys.exit()
            # file = file.readlines()[2:]  # way1 :  # skip the first two line.
            for line in file[1:]:
                if line != "\n":
                    logs.write(str(dict(zip(column_name_list[:], [x for x in line.split()[:]]))) + '\n')
                    self.nsKey_dict_list.append(dict(zip(column_name_list[:], [x for x in line.split()[:]])))
            # pprint.pprint(self.nsKey_dict_list)

    def set_pexpect_command(self, json_path, json_file, log_path):
        with open("{0}/{1}".format(json_path, json_file), encoding="utf-8") as json_data, \
                open(log_path, 'a')as logs:
            data = json.load(json_data)
            spawn_command = jsonpath.jsonpath(data, "$.head..spawn_command")[0]
            logs.write(spawn_command + "\n")
            if not False:
                logs.write(
                    "pexpect.spawn(command={0}, , logfile={1}, encoding={2}, timeout={3})\n".format(spawn_command, logs,
                                                                                                    "utf-8", "20"))
                try:
                    p = pexpect.spawn(command=spawn_command, logfile=logs, encoding='utf-8', timeout=10)
                    spawn_command_expect = jsonpath.jsonpath(data, "$.head..spawn_command_expect")[0]
                    logs.write("p.expect({0})\n".format(spawn_command_expect))
                    p.expect(spawn_command_expect)
                    for ele_dict in (
                            jsonpath.jsonpath(data, "$.head[?(@.sendline)]"),
                            jsonpath.jsonpath(data, "$.body[?(@.sendline)]"), \
                            jsonpath.jsonpath(data, "$.tail[?(@.sendline)]")):
                        # pprint.pprint(ele_dict)
                        for i in ele_dict:
                            P_step1.pAction_v2(i, cls=p)
                except pexpect.TIMEOUT:
                    print(P_step1.repr_message("pexpect.TIMEOUT"))

    def set_pexpect_command_v2(self, json_path, json_file, log_path, error_path):
        with open("{0}/{1}".format(json_path, json_file), encoding="utf-8") as json_data, \
                open(log_path, 'a')as logs, open(error_path, 'a') as errors:
            data = json.load(json_data)
            spawn_command = jsonpath.jsonpath(data, "$.head..spawn_command")[0]
            logs.write(spawn_command + "\n")
            if not False:
                logs.write(
                    "pexpect.spawn(command={0}, , logfile={1}, encoding={2}, timeout={3})\n".format(spawn_command, logs,
                                                                                                    "utf-8", "20"))
                try:
                    p = pexpect.spawn(command=spawn_command, logfile=logs, encoding='utf-8', timeout=10)
                    spawn_command_expect = jsonpath.jsonpath(data, "$.head..spawn_command_expect")[0]
                    logs.write("p.expect({0})\n".format(spawn_command_expect))
                    p.expect(spawn_command_expect)
                    # for ele_dict in (
                    #         jsonpath.jsonpath(data, "$.head[?(@.sendline)]"),
                    #         jsonpath.jsonpath(data, "$.body[?(@.sendline)]"), \
                    #         jsonpath.jsonpath(data, "$.tail[?(@.sendline)]")):
                    ele_dict = jsonpath.jsonpath(data, "$.head[?(@.sendline)]")
                    for i in range(len(ele_dict)):
                        P_step1.pAction_v2(ele_dict[i], cls=p)
                    ele_dict = jsonpath.jsonpath(data, "$.body[?(@.sendline)]")
                    for i in range(len(ele_dict)):
                        if i > 0:
                            # print(ele_dict[i])
                            P_step1.pAction_v2(ele_dict[i], cls=p)
                            pre_key = ele_dict[i - 1].get("key", None)
                            pre_ns = ele_dict[i - 1].get("ns", None)
                            current_key = ele_dict[i].get("key", None)
                            # print("{0}:\t{1}".format("pre_key", pre_key))
                            # print("{0}:\t{1}".format("current_key", current_key))
                            a = p.before[:]
                            try:
                                # print(a)
                                if current_key and a.strip().startswith("status: 0"):
                                    pre_data = a[a.index("data:") + 5:a.index("\r")]
                                    # pre_data = a
                                    # print("{0}:\t{1}".format("pre_data", pre_data))
                                    # print("=" * 60)
                                    self.key_data_list.append(
                                        dict(zip(["ns", "key", "data"], [pre_ns, pre_key, pre_data])))
                                else:
                                    # errors.write("{0} error \n {1} \n".format("set_pexpect_command_v2", a))
                                    pre_status = a[a.index("status:") + 7:a.index("data")]
                                    print("{0}:\t{1}".format("pre_state", pre_status))
                                    pre_data = a[a.index("data:") + 5:a.index("\r")]
                                    print("{0}:\t{1}".format("pre_data", pre_data))
                                    self.error_key_data_list.append(dict(zip(["ns", "key", "data", "status"],
                                                                             [pre_ns, pre_key, pre_data,
                                                                              pre_status])))
                            except ValueError:
                                errors.write(
                                    "{0}\n{1} error \n {2} \n".format("ValueError", "set_pexpect_command_v2", a))
                                print(P_step1.repr_message(a))
                        else:
                            P_step1.pAction_v2(ele_dict[i], cls=p)
                            current_key = ele_dict[i].get("key", None)
                            print("{0}:\t{1}".format("current_key", current_key))
                    ele_dict = jsonpath.jsonpath(data, "$.tail[?(@.sendline)]")
                    for i in range(len(ele_dict)):
                        P_step1.pAction_v2(ele_dict[i], cls=p)
                except pexpect.TIMEOUT:
                    print(P_step1.repr_message("pexpect.TIMEOUT"))

    @staticmethod
    def pAction_v2(Jdist, cls=None, logFile=None):
        if Jdist.get("sendline", None) != None:
            cls.sendline(Jdist["sendline"])
            # print(P_step1.redFont(cls.before))
            # cls.buffer =""
        else:
            raise ValueError("sendline is not given")
        if Jdist.get("expect", None) != None:
            cls.expect(Jdist["expect"])
            print(P_step1.greenFont(cls.after))
            # a = cls.before[:]
            # try:
            #     # print("pexpect before of {0}:\t==>>{1}".format("a[a.index(\"data:\") + 5:])", \
            #     #                                                a[a.index("data:") + 5:a.index("\n")]))
            #     print(P_step1.greenFont(a))
            # except ValueError:
            #     print("we are here")
            #     pass
        else:
            cls.buffer = ""
            print("expect is not given, the sendline is {0}".format(Jdist.get("sendline", None)))


if __name__ == '__main__':
    HU = P_step1()
    HU.setProjectDir(os.path.dirname(os.getcwd()))
    HU.setJsonDir("/json")
    HU.set_codingFiles("/codingFiles")
    HU.setLogDir("/logs")
    HU.log_name += "/step2_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
    HU.setErrorDir("/errors")
    HU.error_name += "/error_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
    print(HU.codingFiles_dir)
    ####################################################################
    HU.set_nsKey_dict("RecordDataIdOverview_0927.txt")
    HU.setJsonDir("/json")
    print("{0}:\t{1}".format("HU.json_dir", HU.json_dir))
    jsonFile = "rawData_DataId_0929.json"
    # save a jsonFile which get from RecordDataIdOverview_0927 <<<<< Step 1
    HU.saveAsFile(HU.json_dir, jsonFile, HU.nsKey_dict_list)  # save as jsonFile
    rawDataFile = HU.json_dir + "/" + jsonFile
    ns_list = HU.get_json_info(rawDataFile, "$..Namespace_hex", codingFormat="utf_8_sig")
    key_list = HU.get_json_info(rawDataFile, "$..Key", codingFormat="utf_8_sig")
    for ns, key in zip(ns_list, key_list):
        if ns.startswith("0x") and key.startswith("0x"):
            HU.add_send_expect(strS="./tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns, key),
                               strE="load: ns: {0} key: {1} slot: 0".format(ns[2:], int(key, 16)), str_ns=ns,
                               str_key=key)
    HU.combineAsJson_v2()
    # save a jsonFile which has data, sendline,ns, key, expect   <<<<< Step 2
    HU.saveAsFile(HU.json_dir, "DataId_0929.json", HU.json_dict)  # save as jsonFile
    # run pexpect in HU
    HU.set_pexpect_command_v2(HU.json_dir, "DataId_0929.json", HU.log_name, HU.error_name)
    HU.json_dict = dict(zip(["key_data_list", "error_key_data_list"], [HU.key_data_list, HU.error_key_data_list]))
    # save a jsonFile which has error_key_data_list and key_data_list   <<<<< Step 3
    HU.saveAsFile(HU.json_dir, "rawData_GetKey_0929.json", HU.json_dict)

    #####################################################################################################
    # Get-key
    def Get_key():
        HU = P_step1()
        HU.setProjectDir(os.path.dirname(os.getcwd()))
        HU.setJsonDir("/json")
        HU.set_codingFiles("/codingFiles")
        HU.setLogDir("/logs")
        HU.log_name += "/step2_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
        HU.setErrorDir("/errors")
        HU.error_name += "/error_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
        print(HU.codingFiles_dir)

        def persistence_getkey():
            HU.set_nsKey_dict("persistenceOverview_0929.txt")
            HU.setJsonDir("/json")
            print("{0}:\t{1}".format("HU.json_dir", HU.json_dir))
            HU.saveAsFile(HU.json_dir, "rawData_persistence.json", HU.nsKey_dict_list)
            rawDataFile = HU.json_dir + "/" + "rawData_persistence.json"
            ns_list = HU.get_json_info(rawDataFile, "$..Namespace_hex", codingFormat="utf_8_sig")
            key_list = HU.get_json_info(rawDataFile, "$..Key", codingFormat="utf_8_sig")
            for ns, key in zip(ns_list, key_list):
                if ns.startswith("0x") and key.startswith("0x"):
                    HU.add_send_expect(
                        strS="./tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns, key) \
                        , strE="load: ns: {0} key: {1} slot: 0".format(ns[2:], int(key, 16)), \
                        str_ns=ns, str_key=key)
            HU.combineAsJson_v2()  # In this func, it sets the self.json_dict
            HU.saveAsFile(HU.json_dir, "persistence.json", HU.json_dict)
            HU.set_pexpect_command_v2(HU.json_dir, "persistence.json", HU.log_name, HU.error_name)

        return persistence_getkey


    # Get_key()()

    """
    exec. to create json file for persistence Getkey
    
    # print(HU.codingFiles_dir)
    # HU.set_nsKey_dict("persistenceOverview_0929.txt")
    # HU.setJsonDir("/json")
    # print("{0}:\t{1}".format("HU.json_dir", HU.json_dir))
    # HU.saveAsFile(HU.json_dir, "rawData_persistence.json", HU.nsKey_dict_list)
    # rawDataFile = HU.json_dir + "/" + "rawData_persistence.json"
    # ns_list = HU.get_json_info(rawDataFile, "$..Namespace_hex", codingFormat="utf_8_sig")
    # key_list = HU.get_json_info(rawDataFile, "$..Key", codingFormat="utf_8_sig")
    # for ns, key in zip(ns_list, key_list):
    #     if ns.startswith("0x") and key.startswith("0x"):
    #         HU.add_send_expect(strS="./tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns, key) \
    #                            , strE="load: ns: {0} key: {1} slot: 0".format(ns[2:], int(key, 16)), \
    #                            str_ns=ns, str_key=key)
    # HU.combineAsJson_v2()  # In this func, it sets the self.json_dict
    # HU.saveAsFile(HU.json_dir, "persistence.json", HU.json_dict)
    
    exec. to run pexpect commmand in HU
    
    # HU.set_pexpect_command_v2(HU.json_dir, "persistence.json", HU.log_name,HU.error_name)
    """


    def Get_all_key():
        HU = P_step1()
        HU.setProjectDir(os.path.dirname(os.getcwd()))
        HU.setJsonDir("/json")
        HU.set_codingFiles("/codingFiles")
        HU.setLogDir("/logs")
        HU.log_name += "/step2_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
        HU.setErrorDir("/errors")
        HU.error_name += "/error_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
        print(HU.codingFiles_dir)
        HU.set_pexpect_command_v2(HU.json_dir, "DataId.json", HU.log_name, HU.error_name)
        HU.json_dict = dict(zip(["key_data_list", "error_key_data_list"], [HU.key_data_list, HU.error_key_data_list]))
        HU.saveAsFile(HU.json_dir, "rawData_GetKey.json", HU.json_dict)

    # Get_all_key()
    def persistence_set_key():
        HU_set = P_step1()
        HU_set.setProjectDir(os.path.dirname(os.getcwd()))
        HU_set.setJsonDir("/json")
        HU_set.set_codingFiles("/codingFiles")
        HU_set.setLogDir("/logs")
        HU_set.log_name += "/step2_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
        HU_set.setErrorDir("/errors")
        HU_set.error_name += "/error_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
        print("{0}:\t{1}".format("HU_set.codingFiles_dir", HU_set.codingFiles_dir))
        # json_name = "persistence.json"
        HU_set.set_nsKey_dict("persistenceOverview_wData_0929.txt")
        HU_set.setJsonDir("/json")
        print("{0}:\t{1}".format("HU.json_dir", HU_set.json_dir))
        HU_set.saveAsFile(HU_set.json_dir, "rawData_persistence_wDat.json", HU_set.nsKey_dict_list)
        rawDataFile = HU_set.json_dir + "/" + "rawData_persistence_wDat.json"
        ns_list = HU_set.get_json_info(rawDataFile, "$..Namespace_hex", codingFormat="utf_8_sig")
        key_list = HU_set.get_json_info(rawDataFile, "$..Key", codingFormat="utf_8_sig")
        data_list = HU_set.get_json_info(rawDataFile, "$..Data", codingFormat="utf_8_sig")
        for ns, key, data in zip(ns_list, key_list,data_list):
            if ns.startswith("0x") and key.startswith("0x"):
                HU_set.add_send_expect(strS="./tsd.persistence.client.mib3.app.SetKey --ns {0} --key {1} --val 0x{2}".format(ns, key,data) \
                                   , strE="store: ns: {0} key: {1} slot: 0".format(ns[2:], int(key, 16)), \
                                   str_ns=ns, str_key=key, str_data = data)
        HU_set.combineAsJson_v2()  # In this func, it sets the self.json_dict
        HU_set.saveAsFile(HU_set.json_dir, "persistence_wDat.json", HU_set.json_dict)
        HU_set.set_pexpect_command_v2(HU_set.json_dir, "persistence_wDat.json", HU_set.log_name,HU_set.error_name)
        pprint.pprint(HU_set.key_data_list)
