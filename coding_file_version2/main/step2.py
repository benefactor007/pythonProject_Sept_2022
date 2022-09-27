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
    HU.log_name += "/step2_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
    print("{0}:\t{1}".format("HU.log_dir", HU.log_name))
    # sys.exit()
    HU.set_codingFiles("/codingFiles")
    print(HU.codingFiles_dir)
    codingFiles_name = HU.codingFiles_dir +"/" + "VW_GP_CHN_v0.9.json"
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
    sys.exit()
    HU.get_json_info(HU.json_dir + "/" + "DataId.json", "")

    HU.json_list = HU.nsKey_dict_list
    HU.combineAsJson_v2()
    HU.saveAsFile(HU.json_dir, "DataId" + ".json")   # save as jsonFile
















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

