"""
pls use python3 or above. This program is based on Python3.5
"""
import time

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
        self.codingFiles_folder = ""
        self.errors_folder = ""
        self.logs_folder = ""
        self.tools_folder = ""
        self.trash_folder = ""



    def setProjectDir(self, path):
        self.project_folder = path

    vital_folder_list = ["codingFiles", "errors", "json", "logs", "tools", "trash"]

    def setJsonDir(self, json_folder):
        self.json_folder = self.project_folder + os.sep + json_folder

    def setCodingDir(self, codingFiles_folder):
        self.codingFiles_folder = self.project_folder + os.sep + codingFiles_folder

    def setErrorDir(self, errors_folder):
        self.errors_folder = self.project_folder + os.sep + errors_folder

    def setLogDir(self, logs_folder):
        self.logs_folder = self.project_folder + os.sep + logs_folder

    def setToolDir(self, tools_folder):
        self.tools_folder = self.project_folder + os.sep + tools_folder

    def setTrashDir(self, trash_folder):
        self.trash_folder = self.project_folder + os.sep + trash_folder




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
    step2.setJsonDir("json")
    step2.setTrashDir("trash")
    step2.setToolDir("tools")
    step2.setErrorDir("errors")
    step2.setCodingDir("codingFiles")
    step2.setLogDir("logs")
    vital_folder_list = ["codingFiles", "errors", "json","logs","tools","trash"]
    for i in vital_folder_list:
        step2.check_folder_exist(i)

    print(step2.__init__.__code__.co_varnames)          #('self',)
    # print(dir(step2))
    print(vars(step2))
    for i,j in vars(step2).items():
        print(f"{i} : {j}")

    print(__file__)
    current_file_name = os.path.basename(__file__).split(".")[0]
    print(current_file_name)
    # set auto log file generation
    step2.log_path = ""
    step2.error_path = ""
    step2.log_path = step2.logs_folder + os.sep + current_file_name + "_" + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
    # step2.error_name = step2.errors_folder + os.sep + "error" + "_" time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + ".txt"
    step2.error_path = f"{step2.errors_folder + os.sep}error_{time.strftime('%Y%m%d_%H_%M_%S', time.localtime(time.time()))}.txt"
    print(f"step2.log_path is {step2.log_path}\n"
          f"step2.error_path is  {step2.error_path}")
    #### Here: pls assign the value here ####
    # pexpect_exec_json = "toGet_nsKey_1011.json"
    pexpect_exec_json = "toGet_nsKey_VW_GP_v09_1013.json"
    # pexpect_output_json = "rawData_toGet_nsKey_1011.json"
    pexpect_output_json = "rawData_toGet_nsKey_VW_GP_v09_1013.json"
    ##########################################

    step2.set_pexpect_command_v2(step2.json_folder, pexpect_exec_json, step2.log_path, step2.error_path)
    step2.json_dict = dict(zip(["key_data_list", "error_key_data_list"], [step2.key_data_list, step2.error_key_data_list]))
    step2.saveAsFile(step2.json_folder, pexpect_output_json, step2.json_dict)



    sys.exit()




    print(step2.get_json_info("rawData_GetKey_0929.json", "$..[?(@.status == '8').key]"))


    sys.exit()
    Getkey_fileName = "rawData_GetKey_0929.json"
    print(f'os.getcwd() >> {os.getcwd()}')
    step2.setProjectDir(os.path.split(os.getcwd())[0])
    print(f"step2.project_folder is {step2.project_folder}")

    # print(f'os.getcwd(Getkey_fileName) >> {os.getcwd(Getkey_fileName)}')
    # step2.get_json_info("")
