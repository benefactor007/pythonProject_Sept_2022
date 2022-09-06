#!/usr/bin/python3.5
import os, pexpect, sys
import json, jsonpath




class HU:
    ip = "192.168.1.4"
    password = "root"
    dest_dic = "tmp"
    local_files_dic = "tools"
    sum_files = 0

    def __init__(self):
        HU.sum_files += 1

    # @staticmethod
    # def copy_file_to_HU(tools_name, password="root", ip="192.168.1.4", dest_dic="tmp"):
    #     print(os.getcwd()) # get the current path
    #     p_command = "scp -r " + os.getcwd() + "/" +tools_name + " " + password + ":" + ip + "/" + dest_dic + "/"
    #     print(p_command)
    @staticmethod
    def copy_file_to_HU(tools_name):
        # print(os.getcwd())  # get the current path
        tools_path = os.getcwd() + "/" + "tools"
        p_command = "scp -r " + tools_path + "/" + tools_name + " " + HU.password + "@" + HU.ip + ":/" + HU.dest_dic + "/"
        # print(p_command)
        return p_command

    @staticmethod
    def greenFont(str):
        return "\033[32m" + str + "\033[0m"

    @staticmethod
    def repr_message(message: str):
        padding_len = '%' + str(int(len(message) / 2) + 35) + 's'
        return "=" * 70 + "\n" + padding_len % message + "\n" + "=" * 70 + "\n"

    @staticmethod
    def doPexpect(p_command):
        p = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=30)
        p.expect("password")
        p.sendline(HU.password)
        p.expect("100%")
        p.close()
        return HU.greenFont(HU.repr_message("Success to copy file to HU"))

    @staticmethod
    def get_json_info(json_file_name, jsonPathDesc):
        """
        :param json_file_name:
        :param jsonPathDesc:
        :return: dict(json's data)
        """
        import json,jsonpath
        # with open(os.getcwd() + '/json_sets/' + "p_script1.json") as json_file:
        with open(os.getcwd() + '/json_sets/' + json_file_name) as json_file:
            data = json.load(json_file)
            res = jsonpath.jsonpath(data, jsonPathDesc)
        return res

    @staticmethod
    def pAction(Jlist, cls = None):
        if Jlist[0] == "expect":
            # print(Jlist[1])
            cls.expect(Jlist[1])
        elif Jlist[0] == "sendline":
            # print(Jlist[1])
            cls.sendline(Jlist[1])

    @staticmethod
    def adv_doPexpect(p_command, json_name):
        p = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=30)
        # json_list = HU.get_json_info("p_script1.json", "$.p_script1.*")
        json_list = HU.get_json_info(json_name, "$.p_script1.*")
        for i in json_list:
            HU.pAction(list(i.items())[0], p)
        p.close()
        return HU.greenFont(HU.repr_message("Success to copy file to HU"))


# class coding(HU):c
#     @staticmethod
#     def doCoding():

p_script1 = {"p_script1": [{"expect": "password"}, {"sendline": "root"}, {"expect": "100%"}]}



if __name__ == '__main__':


    # json_p_script1 = json.dumps(p_script1, indent=4, separators=(", ", " : "))
    # print(json_p_script1)
    # json.dump(p_script1, open(os.getcwd() + '/json_sets/p_script1.json', 'w'), ensure_ascii=False,indent=4, separators=(", ", " : "))
    """
    json_adaption, '$.Adaptions[?(@.RDI == "0x0B1D")].Value'
    """
    # with open(os.getcwd() + '/json_sets/' + "p_script1.json") as json_file:
    #     data = json.load(json_file)
    # print(type(data))
    # res = jsonpath.jsonpath(data, '$.p_script1.*')
    # # res = jsonpath.jsonpath(p_data1, '$.p_script.*')
    # print(res)

    # obj = HU()
    # action1 = obj.get_json_info("p_script1.json", "$.p_script1.*")
    # print(action1)
    # for i in action1:
    #     HU.pAction(list(i.items())[0])
    # obj.pAction(action1)
    # action1 = obj.get_json_info("p_script1.json","$.p_script1.*")
    # print(action1)
    # for i in action1:
    #     # print(list(i.keys())[0])
    #     # print(list(i.values())[0])
    #     print(type(list(i.items())))
    #     print(list(i.items())[0][0])
    #     print(list(i.items())[0][1])


    # sys.exit()

    # obj = HU()
    fileList = ["tsd.persistence.client.mib3.app.GetKey", "tsd.persistence.client.mib3.app.SetKey",
                "tsd.persistence.client.mib3.app.CallReset", "tsd.persistence.client.mib3.app.InitPersistence"]
    def transfer_files(cls, fileList):
        for i in fileList:
            # cls.doPexpect(cls.copy_file_to_HU(i))
            cls.adv_doPexpect(cls.copy_file_to_HU(i), "p_script1.json")
            # print(cls.copy_file_to_HU(i))
    transfer_files(HU, fileList)
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.GetKey")
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.SetKey")
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.CallReset")
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.InitPersistence")
    # print(HU.sum_files)
    # print(HU.greenFont(HU.repr_message("Success to copy file to HU")))
