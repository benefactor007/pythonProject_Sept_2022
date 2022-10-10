"""
pls use python3 or above. This program is based on Python3.5
"""

from peri_step1 import P_step1
import os,sys,pexpect,json,jsonpath
import future_fstrings



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
        self.json_folder = self.project_folder + os.sep

    def setProjectDir(self, path):
        self.project_folder = path + os.sep

    def setJsonDir(self, path):
        self.json_folder =

if __name__ == '__main__':
    step2 = P_step2()
    Getkey_fileName = "rawData_GetKey_0929.json"
    print(f"os.getcwd() >> {os.getcwd()}")
    step2.setProjectDir(os.path.split(os.getcwd())[0])
    print(f"step2.project_folder is {step2.project_folder}")

    # print(f'os.getcwd(Getkey_fileName) >> {os.getcwd(Getkey_fileName)}')
    step2 = P_step1()
    # step2.get_json_info("")
