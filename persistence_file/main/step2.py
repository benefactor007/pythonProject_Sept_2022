"""
pls use python3 or above. This program is based on Python3.5
"""

from peri_step1 import P_step1
import os,sys,pexpect,json,jsonpath



# My file: rawData_GetKey_0929.json
""" 
    "error_key_data_list" : [
        {
            "status" : " 8 ", 
            "ns" : "0x1000000", 
            "key" : "0x0501", 
            "data" : " "
        }, 
        ],

   "key_data_list" : [
        {
            "ns" : "0x1000000", 
            "key" : "0x0B39", 
            "data" : " 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 0 "
        }, 
        ]
"""

class P_step2(P_step1):
    def __init__(self):
        P_step1.__init__(self)
        self.project_folder = ""
        self.json_folder = ""



    def setProjectDir(self, path):
        self.project_folder = path



    def setJsonDir(self, json_folder):
        self.json_folder = self.project_folder + os.sep +json_folder

    def check_folder_exist(self, folder_name):
        if self.project_folder:
            if os.path.isdir(self.project_folder + os.sep + folder_name):
                print(f"{folder_name} is under the project directory")
            else:
                print(f"{folder_name} is not under the project directory\n"
                      f"Now, creating a new directory which named as {folder_name}")
                os.mkdir(self.project_folder + os.sep + folder_name)
        else:
            print(f"self.project_folder is {self.project_folder}\n"
                  f"pls define your project directory!!!")




    # @staticmethod
    def get_json_info(self,json_name, jsonPathDesc, codingFormat=None):
        """
      :param json_file_name:
      :param jsonPathDesc:
      :return: dict(json's data)
      """
        import json, jsonpath
        json_file_path = self.json_folder + os.sep + json_name
        print(f"{json_file_path} is a file: {os.path.isfile(json_file_path)}")
        with open(json_file_path, encoding=codingFormat) as json_file:
            data = json.load(json_file)
            res = jsonpath.jsonpath(data, jsonPathDesc)
        return res

if __name__ == '__main__':
    step2 = P_step2()
    step2.setProjectDir(os.path.split(os.getcwd())[0])
    step2.check_folder_exist("json")
    step2.check_folder_exist("trash")
    step2.setJsonDir("json")
    print(step2.get_json_info("rawData_GetKey_0929.json", "$..[?(@.status == '8').key]"))


    sys.exit()
    Getkey_fileName = "rawData_GetKey_0929.json"
    print(f'os.getcwd() >> {os.getcwd()}')
    step2.setProjectDir(os.path.split(os.getcwd())[0])
    print(f"step2.project_folder is {step2.project_folder}")

    # print(f'os.getcwd(Getkey_fileName) >> {os.getcwd(Getkey_fileName)}')
    # step2.get_json_info("")
