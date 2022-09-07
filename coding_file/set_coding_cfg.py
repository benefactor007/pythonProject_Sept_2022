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
        import json, jsonpath
        # with open(os.getcwd() + '/json_sets/' + "p_script1.json") as json_file:
        with open(os.getcwd() + '/json_sets/' + json_file_name) as json_file:
            data = json.load(json_file)
            res = jsonpath.jsonpath(data, jsonPathDesc)
        return res

    @staticmethod
    def pAction(Jlist, cls=None):
        if Jlist[0] == "expect":
            # print(Jlist[1])
            cls.expect(Jlist[1])
        elif Jlist[0] == "sendline":
            # print(Jlist[1])
            cls.sendline(Jlist[1])

    @staticmethod
    def adv_doPexpect(p_command, json_name, jsonpath_command):
        with open("logs.txt", 'w') as my_log_file:
            p = pexpect.spawn(command=p_command, logfile=my_log_file, encoding='utf-8', timeout=30)
            # json_list = HU.get_json_info("p_script1.json", "$.p_script1.*")
            json_list = HU.get_json_info(json_name, jsonpath_command)
            for i in json_list:
                # print(i)
                HU.pAction(list(i.items())[0], p)
            p.close()
            # return HU.greenFont(HU.repr_message("Success to copy file to HU"))
            return HU.greenFont(HU.repr_message("Successful"))


# class coding(HU):c
#     @staticmethod
#     def doCoding():

p_script1 = {"p_script1": [{"expect": "password"}, {"sendline": "root"}, {"expect": "100%"}]}

if __name__ == '__main__':

    """
    json data Template:
     {'p_script1': [{'expect': 'password'}, {'sendline': 'root'}, {'expect': '100%'}]}
    569efa06c166a5db02a062bbf1275b8fff09c5d5  ./tsd.persistence.client.mib3.app.InitPersistence
    585c1e51587cd7ecd8678171557af6c132d994a6  ./tsd.persistence.client.mib3.app.CallReset
    4e9d90211063684bf2ce56b3f9bf94cefc141fa4  ./tsd.persistence.client.mib3.app.SetKey
    880152e334d675794bea1f3616d1c94c147c1962  ./tsd.persistence.client.mib3.app.GetKey
    """
    files_checksum_script = {'p_check_script1':
        [
            {'expect': 'password'},
            {'sendline': 'root'},
            {'expect': 'root@'},
            {'sendline': "cd /tmp/"},
            {'expect': "/tmp"},
            {'sendline': "find . -name \"tsd.persistence*\" -exec sha1sum {} + |LC_ALL=C sort"},
            {'expect': "4e9d90211063684bf2ce56b3f9bf94cefc141fa4"},
            {'expect': "569efa06c166a5db02a062bbf1275b8fff09c5d5"},
            {'expect': "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},
            {'expect': ""},
            {'sendline': 'sync'},
            {'sendline': 'exit'},
        ]
    }
    #da39a3ee5e6b4b0d3255bfef95601890afd80709

    # json_p_script1 = json.dumps(files_checksum_script, indent=4, separators=(", ", " : "))
    # json.dump(files_checksum_script, open(os.getcwd() + '/json_sets/p_check_script1.json', 'w'), ensure_ascii=False, indent=4,
    #           separators=(", ", " : "))
    """
    linux command:
    1. lsattr
    2. chattr +i [files]
    """
    # sys.exit()

    # fileList = os.listdir(os.getcwd() + "/json_sets")
    # with open(os.getcwd() + '/json_sets/' + fileList[0]) as json_file:
    #     data = json.load(json_file)
    #     # res = jsonpath.jsonpath(data, jsonPathDesc)
    # # json = json.loads(fileList[0])
    # print(data)

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
    # fileList = ["tsd.persistence.client.mib3.app.GetKey", "tsd.persistence.client.mib3.app.SetKey",
    #             "tsd.persistence.client.mib3.app.CallReset", "tsd.persistence.client.mib3.app.InitPersistence"]
    # print(os.listdir(os.getcwd() + "/tools"))

    # print(fileList)



    fileList = os.listdir(os.getcwd() + "/tools")
    def transfer_files(cls, fileList):
        for i in fileList:
            # cls.doPexpect(cls.copy_file_to_HU(i))
            print(cls.adv_doPexpect(cls.copy_file_to_HU(i), "p_script1.json", "$.p_script1.*"))
            # print(cls.copy_file_to_HU(i))
    transfer_files(HU, fileList)
    p_command = "ssh root@192.168.1.4"
    print(HU.adv_doPexpect(p_command,"p_check_script1.json", jsonpath_command = "$.p_check_script1.*"))

    sys.exit()
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.GetKey")
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.SetKey")
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.CallReset")
    # obj.copy_file_to_HU("tsd.persistence.client.mib3.app.InitPersistence")
    # print(HU.sum_files)
    # print(HU.greenFont(HU.repr_message("Success to copy file to HU")))
