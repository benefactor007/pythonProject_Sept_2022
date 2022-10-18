import binascii
import pprint
import time

from step2 import P_step2,Scp
import os, sys, pexpect, json, jsonpath



class FazitId(Scp):
    def __init__(self, fazit = "",serial = ""):
        Scp.__init__(self)
        self.fazit = fazit
        self.serial = serial
        self.fazit_ns = "0x3000000"
        self.fazit_key = "0xF17C"
        self.read_write_access_ns = "0x80000008"
        self.read_write_access_key = "0x00"
        self.serial_ns = "0x3000000"
        self.serial_key = "0xF18C"

    def add_send_expect(self, strS, strE):
        # if not self.json_dict.get("expect",None) and not self.json_dict.get("sendline", None):
        newDict = {}
        newDict["sendline"] = strS
        newDict["expect"] = strE
        self.json_list.append(newDict)

    def set_nsKey_dict(self, filePath):
        """
        only read first two columns, which are column 1 and column 2
        :param fileName:
        :return: dict{column2 : column1}
        """
        with open(filePath, 'r') as file, open(self.log_name, "w") as logs:
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

    def set_fazit(self):
        return binascii.hexlify(self.fazit.encode('utf-8')).decode('utf-8')

    def set_serial(self):
        return binascii.hexlify(self.fazit.encode('utf-8')).decode('utf-8')

if __name__ == '__main__':
    wFazit = FazitId("X9G-10203.05.2299990634")
    wFazit.setProjectDir(os.path.split(os.getcwd())[0])
    wFazit.setJsonDir("json")
    wFazit.setTrashDir("trash")
    wFazit.setToolDir("tools")
    wFazit.setErrorDir("errors")
    wFazit.setCodingDir("codingFiles")
    wFazit.setLogDir("logs")
    vital_folder_list = ["codingFiles", "errors", "json", "logs", "tools", "trash"]
    wFazit.setFileList(wFazit.tools_folder)
    wFazit.log_path = wFazit.logs_folder + os.sep + "trans_task_" + time.strftime("%Y%m%d_%H_%M_%S",
                                                                            time.localtime(
                                                                                time.time())) + ".txt"
    step2.error_path = step2.errors_folder + os.sep + time.strftime("%Y%m%d_%H_%M_%S",
                                                                    time.localtime(time.time())) + ".txt "
    # wFazit.transfer_files(wFazit.getFileList(wFazit.tools_folder))  # important, copy files to HU

    """
    Namespace_hex   Key         Namespace_purpose
    0x80000008      0x00        Open_read-write_access
    0x3000000       0xF18C      Set_serial-num
    0x3000000       0xF17C      Set_Fazit-id
    """
    wFazit.add_send_expect(
        strS="./tsd.persistence.client.mib3.app.SetKey --ns {0} --key {1} ".format(wFazit.read_write_access_ns,
                                                                                   wFazit.read_write_access_key),
        strE="store: ns: {0} key: {1} slot: 0".format(wFazit.read_write_access_ns, wFazit.read_write_access_key))
    wFazit.add_send_expect(strS="./tsd.persistence.client.mib3.app.SetKey --ns {0} --key {1} --value {2}".format(wFazit.fazit_ns, wFazit.fazit_key,wFazit.set_fazit()),
                               strE="store: ns: {0} key: {1} slot: 0".format(wFazit.fazit_ns,wFazit.fazit_key))
    wFazit.add_send_expect(
        strS="./tsd.persistence.client.mib3.app.SetKey --ns {0} --key {1} --value {2}".format(wFazit.serial_ns,
                                                                                              wFazit.serial_key,
                                                                                              wFazit.set_serial()),
        strE="store: ns: {0} key: {1} slot: 0".format(wFazit.serial_ns, wFazit.serial_key))
    wFazit.combineAsJson_v2()
    pexpect_exec_json = "Fazit_write.json"
    wFazit.saveAsFile(wFazit.json_folder, pexpect_exec_json, wFazit.json_dict)
    wFazit.set_pexpect_command_v2(wFazit.json_folder, pexpect_exec_json, wFazit.log_path, wFazit.error_path)