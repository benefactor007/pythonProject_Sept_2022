#!/usr/bin/python3.5
"""
Add on 9/8/2022, at 1:02 PM
"""
import time

import pexpect

from sub_action import Sub
import jsonpath, json, os, sys
import xlrd


class new_sub(Sub):
    key_Namehex_dict = {}

    @staticmethod
    def fileInfo_to_dict(fileName):
        """
        only read first two columns, which are column 1 and column 2
        :param fileName:
        :return: dict{column2 : column1}
        """
        new_sub.key_Namehex_dict = {}
        with open(os.getcwd() + "/files/" + fileName, 'r') as file:
            file = file.readlines()[1:]  # way1 :  # skip the first line.
            for line in file:
                # print(line.split())
                if line != "\n":
                    new_sub.key_Namehex_dict[line.split()[1]] = line.split()[0]
        return new_sub.key_Namehex_dict

    @staticmethod
    def get_json_info(json_file_name, jsonPathDesc, codingFormat=None):
        """
      :param json_file_name:
      :param jsonPathDesc:
      :return: dict(json's data)
      """
        import json, jsonpath
        # with open(os.getcwd() + '/json_sets/' + "p_script1.json") as json_file:
        with open(os.getcwd() + '/json_sets/' + json_file_name, encoding=codingFormat) as json_file:
            data = json.load(json_file)
            res = jsonpath.jsonpath(data, jsonPathDesc)
        return res

    @staticmethod
    def create_json_file(RDI_list):
        # RDI_list = jsonpath.jsonpath(json_data, "$..RDI")
        for key in RDI_list:
            new_sub.init_dict['p_read_script1'].append(
                {"sendline": "tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(
                    X.key_Namehex_dict.get(key), key)})
            # print("type of %s is" % key, type(key))
            # """Set the final expect command"""
            # with open('logs_0909.txt', 'w') as file:
            #     for line in file:
            #         # print('type of %s: %s' %(key,type(key)))
            #         if line.startswith('load') and line.find(str(int(key,16))) != -1:
            #             new_sub.init_dict['p_read_script1'].append({"expect": line.rstrip('\n')})
            Sub.init_dict['p_read_script1'].append({"expect": "load: ns: {0} key: {1} slot: 0 ".format(
                X.key_Namehex_dict.get(key)[2:], str(int(key, 16)))})
        #      {"sendline": "load: ns: {0} key: {1} slot: 0 status: 0".format(ns[3:], str(int(key,16)))})
        new_sub.init_dict['p_read_script1'].append({'sendline': 'sync'})
        new_sub.init_dict['p_read_script1'].append({'sendline': 'exit'})
        # rename key in dictionary
        new_sub.init_dict['p_setGetKey_script1'] = new_sub.init_dict.pop('p_read_script1')
        return new_sub.init_dict

    @staticmethod
    def deleteBlankLine(oldFile, newFile):
        """

      :param oldFile: "tempEdit.txt"
      :param newFile: "newTempEdit.txt"
      :return:
      """
        with open(os.getcwd() + '/files/' + oldFile, 'r') as fr, open(os.getcwd() + '/files/' + newFile, 'w',
                                                                      encoding='utf-8') as fd:
            for text in fr.readlines():
                if text.split() != []:
                    fd.write(text)
        print("Success to delete blank line!")

    @staticmethod
    def adv_doPexpect(p_command, json_name, jsonpath_command, log_name = "logs.txt"):  # add on 9/19/2022
        """

        :param p_command:
        :param json_name:
        :param jsonpath_command:
        :param log_name:
        :return:
        """
        # def adv_doPexpect(p_command, json_name, jsonpath_command):
        # with open("logs.txt", 'w') as my_log_file:
        with open(log_name, 'w') as my_log_file:  # add on 9/19/2022
            p = pexpect.spawn(command=p_command, logfile=my_log_file, encoding='utf-8', timeout=20)
            # json_list = HU.get_json_info("p_script1.json", "$.p_script1.*")
            json_list = new_sub.get_json_info(json_name, jsonpath_command)
            for i in json_list:
                print(i)
                try:
                    new_sub.pAction(list(i.items())[0], p)
                except pexpect.TIMEOUT:
                    print(p.before, p.after)
                # print("%s pass"%(i))
            p.expect(pexpect.EOF)  # Add in 9/19/2022
            p.close()
            # return HU.greenFont(HU.repr_message("Success to copy file to HU"))
            return new_sub.greenFont(new_sub.repr_message("Successful"))


if __name__ == '__main__':

    X = new_sub()
    """
    func: send file and checksum, pls uncomment below
    """
    fileList = os.listdir(os.getcwd() + "/tools")


    def transfer_files(cls, fileList):
        for i in fileList:
            # cls.doPexpect(cls.copy_file_to_HU(i))
            print(cls.adv_doPexpect(cls.copy_file_to_HU(i), "p_script1.json", "$.p_script1.*"))
            time.sleep(1)
            # print(cls.copy_file_to_HU(i))


    transfer_files(X, fileList)
    p_command = "ssh root@192.168.1.4"
    print(X.adv_doPexpect(p_command, "p_check_script2.json", jsonpath_command="$.p_check_script2.*"))
    # change check p_check_script from 1 to 2.!!!!!!!!
    sys.exit()

    print(X.adv_doPexpect(p_command="ssh root@192.168.1.4", json_name="json_GetKey.json",
                          jsonpath_command="$.{0}.*".format("p_setGetKey_script1"), log_name="log_0919.txt"))
    print(X.greenFont(X.repr_message("Success to exec. Pexpect")))
    sys.exit()

    # print(X.init_dict)
    # print(os.getcwd()+"/files/")
    fileList = os.listdir(os.getcwd() + "/files")

    print(fileList)
    #  VW_GP_CHN_v0.6_exceptCodings.json
    # print(X.get_json_info("VW_GP_CHN_v0.6_exceptCodings.json", "$..RDI"))
    # json_path = os.getcwd() + '/json_sets/' + "VW_GP_CHN_v0.6_exceptCodings.json"
    # print(json_path)
    # print("/home/jpcc/PycharmProjects/pythonProject_Sept_2022/coding_file/json_sets/VW_GP_CHN_v0.6_exceptCodings.json")
    # with open(json_path,encoding = 'utf-8-sig') as json_file:
    #     data = json.load(json_file)
    # print(data)
    # json_path = os.getcwd() + '/json_sets/' + "p_script1.json"
    # print(json_path)
    # with open(json_path, encoding= None) as json_file:
    #   data = json.load(json_file)
    # print(data)
    # print(jsonpath.jsonpath(json_path,"$..RDI"))

    print(X.fileInfo_to_dict("RecordDataIdOverview.txt"))
    key_list = X.get_json_info("VW_GP_CHN_v0.6_exceptCodings.json", "$..RDI", codingFormat="utf-8-sig")

    # sys.exit()
    for i in key_list:
        # print(i)
        # print(X.key_Namehex_dict.get(i, "Not matched"))
        if X.key_Namehex_dict.get(i, "Not matched") == "Not matched":
            print("No match key is %s" % i)
    # sys.exit()

    X.deleteBlankLine("tempEdit.txt", "newTempEdit.txt")

    tempDict = {}
    with open(os.getcwd() + '/files/' + 'newTempEdit.txt', 'r') as f:
        f = f.readlines()
        for line in f[1:]:
            tempDict[line.strip()] = f[0].strip()

    print(tempDict)
    print("type of %s : %s" % ("X.key_Namehex_dict", type(X.key_Namehex_dict)))
    X.key_Namehex_dict.update(tempDict)

    for i in key_list:
        # print(i)
        # print(X.key_Namehex_dict.get(i, "Not matched"))
        if X.key_Namehex_dict.get(i, "Not matched") == "Not matched":
            raise Exception("We found an unmatched Key")
            # print("No match key is %s" % i)
    # a = json.dump(X.create_json_file(RDI_list=key_list),indent=4, separators=(", ", " : "))
    # a = json.dumps(X.create_json_file(RDI_list=key_list), indent=4, separators=(", ", " : "))
    # print(a)
    key_list.append("0x0600")
    print(X.key_Namehex_dict)
    json.dump(X.create_json_file(RDI_list=key_list),
              open(os.getcwd() + '/json_sets/json_GetKey.json', 'w'), ensure_ascii=False,
              indent=4, separators=(", ", " : "))
