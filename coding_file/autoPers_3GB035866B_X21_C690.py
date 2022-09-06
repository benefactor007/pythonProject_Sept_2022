#! /usr/bin/env python3.5
import binascii
import sys
import hashlib

import pexpect
from auto_write_otp_v20220516 import *

write_status = False


def str_to_hexStr(str_info):
    return binascii.hexlify(str_info.encode('utf-8')).decode('utf-8')


def str_to_hexStr_v2(char):
    # print([x for x in '3GB035866A'])
    # print([str_to_hexStr(i) for i in [x for x in char]])
    # print(' '.join(['33', '47', '42', '30', '33', '35', '38', '36', '36', '41']))
    return ' '.join([str_to_hexStr(i) for i in [x for x in char]])


def copy_file_to_HU(file_path: str):
    ip = "192.168.1.4"
    # hu_zone = "/var/tmp/"
    hu_zone = "/tmp/"
    dest_path = "    root@192.168.1.4:" + hu_zone
    # dest_path = "    root@192.168.1.4:/tmp/"
    print("scp " + file_path + dest_path)
    # set timeout = -1
    p_command = "scp -r " + file_path + dest_path
    p1 = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=None)
    p1.expect("password")
    p1.sendline("root")
    p1.expect("100%")
    p1.close()
    print(greenFont("*" * 70 + "\n" + "%35s\n" % ('copy file to HU') + "*" * 70 + "\n"))


def do_pexpect(**kwargs):
    ip = "192.168.1.4"
    global write_status
    assert 'serial_num' in kwargs, redFont(
        "\n" + "?" * 70 + "\n" + "%35s%s\n" % ('serial_num', ' is missing') + "?" * 70 + "\n")
    log_file = kwargs['serial_num'] + "_pers" + "_log_file" + '.txt'
    # hu_zone = "/var/tmp/"
    hu_zone = "/tmp/"
    with open(log_file, 'a') as my_log_file:
        p = pexpect.spawn("ssh root@" + ip, timeout=None, logfile=my_log_file, encoding='utf-8')
        # p.expect("login")
        # p.sendline("root")
        p.expect("password")
        p.sendline("root")
        print(repr_message(greenFont(kwargs['serial_num'])))
        # initial vkms
        # p.sendline("chmod +x vkms_init_pss.sh")
        # p.sendline("./vkms_init_pss.sh")
        # If HU is brand new, have to InitPersistence script
        p.sendline("chmod +x " + hu_zone + "tsd.persistence.client.mib3.app.InitPersistence")
        p.sendline(hu_zone + "tsd.persistence.client.mib3.app.InitPersistence")
        time.sleep(5)
        p.sendline("mount-read-write.sh")
        p.sendline("chmod +x " + hu_zone + "vkms_init_pss.sh")
        p.sendline(hu_zone + "vkms_init_pss.sh")
        try:
            p.expect("Finished", timeout=10)
            print(greenFont(repr_message("Initializing VKMS finished")))
            write_status = True
        except pexpect.TIMEOUT:
            write_status = False
            print(redFont(repr_message("VKMS error")))
        p.sendline("chmod +x " + hu_zone + "vkms_import_reset_dlc.sh")
        p.sendline(hu_zone + "vkms_import_reset_dlc.sh")
        try:
            p.expect("Finished", timeout=10)
            print(greenFont(repr_message("Importing VKMS Reset DLC finished")))
            write_status = True
        except pexpect.TIMEOUT:
            write_status = False
            print(redFont(repr_message("VKMS error")))

        p.sendline("chmod +x " + hu_zone + "tsd.persistence.client.mib3.app.SetKey")
        p.sendline(hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x80000008 --key 0x00  --val 0xe5")
        # Set serial_num
        p.sendline("mount-read-write.sh")
        if 'serial_num' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF18C  --val 0x" + str_to_hexStr(
                    kwargs['serial_num']).upper())
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('serial_num', ' no change') + "?" * 70 + "\n"))
        # # Set Fazit-id
        if 'fazit' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF17C  --val 0x" + str_to_hexStr(
                    kwargs['fazit']).upper())
        else:
            print(redFont("?" * 70 + "\n" + "%30s%s\n" % ('fazit', ' no change') + "?" * 70 + "\n"))
        # Set Hardware version >> X13 (SOP1.5)/(37W_SOP1.0)
        if 'hw_version' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF1A3  --val 0x" + str_to_hexStr(
                    kwargs['hw_version']).upper())
            try:
                p.expect("key: 61859 slot: 0 status: 0", timeout=5)
                print(greenFont(repr_message("Key(61859) has written")))
                write_status = True
            except pexpect.TIMEOUT:
                write_status = False
                print(redFont(repr_message("Something is going wrong")))
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('hw_version', ' no change') + "?" * 70 + "\n"))
        # Set Software version >> C420
        if 'sw_version' in kwargs:
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x3000000 --key 0xF189  --val 0x" + str_to_hexStr(
                    kwargs['sw_version']).upper())
            try:
                p.expect("key: 61833 slot: 0 status: 0", timeout=5)
                print(greenFont(repr_message("Key(61833) has written")))
                write_status = True
            except pexpect.TIMEOUT:
                write_status = False
                print(redFont(repr_message("Something is going wrong")))
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('sw_version', ' no change') + "?" * 70 + "\n"))
        # Set PartNum >> 3GB035866A
        if 'part_num' in kwargs:
            # Oct   Dec   Hex   Char
            # 040   32    20    SPACE
            # p.sendline(
            #     hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF187 --val 0x" + str_to_hexStr(
            #         kwargs['part_num']).upper())
            # p.sendline(
            #     hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF191 --val 0x" + str_to_hexStr(
            #         kwargs['part_num']).upper())
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF187 --val 0x" + str_to_hexStr(
                    kwargs['part_num']).upper() + '20')
            p.sendline(
                hu_zone + "tsd.persistence.client.mib3.app.SetKey --ns 0x03000000 --key 0xF191 --val 0x" + str_to_hexStr(
                    kwargs['part_num']).upper() + '20')
            try:
                # p.expect("key: 61841 slot: 0 status: 0", timeout=5)
                # key: 61841 slot: 0 status: 0 data: 33 47 42 30 33 35 38 36 36 44 20
                p.expect("key: 61831 slot: 0 status: 0 data: " + str_to_hexStr_v2(
                    kwargs['part_num']) + " 20", timeout=5)
                print(greenFont(repr_message("Key(61831):" + kwargs['part_num'] + "(space) has written")))
                p.expect("key: 61841 slot: 0 status: 0 data: " + str_to_hexStr_v2(
                    kwargs['part_num']) + " 20", timeout=5)
                print(greenFont(repr_message("Key(61841):" + kwargs['part_num'] + "(space) has written")))
                write_status = True
            except pexpect.TIMEOUT:
                write_status = False
                print(redFont(repr_message("Something is going wrong")))
        else:
            print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('part_num', ' no change') + "?" * 70 + "\n"))
        # check Android
        try:
            p.sendline(hu_zone + "tsd.persistence.client.mib3.app.GetKey --ns 0x01000000 --key 0x0512")
            i = p.expect(["load: ns: 1000000 key: 1298 slot: 0 status: 4 data:",
                          "load: ns: 1000000 key: 1298 slot: 0 status: 0 data: 40 0",
                          "load: ns: 1000000 key: 1298 slot: 0 status: 0 data: 80 0"])
            if i == 0:
                print(repr_message("Android was not set"))
            elif i == 2:
                print(greenFont(repr_message("BMos turns on")))
            else:
                print(greenFont(repr_message("Android turns on")))
        except (pexpect.TIMEOUT, pexpect.EOF):
            print(redFont(repr_message("Something is going wrong")))
        pexpect.EOF
        p.sendline("sync")
        p.sendline("exit")
        p.expect("closed")
        # p.expect(pexpect.EOF)
        # print("\033[32m" + "PASS" + "\033[0m")  # print Green font


# def copy_file_to_HU_v2():
#     p_scp = pexpect.spawn("scp /home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh root@192.168.1.4:/tmp/", timeout=60, logfile=sys.stdout, encoding='utf-8')
#     p_scp.expect("password")
#     p_scp.sendline("root")
#     p_scp.expect("100%  117KB")
#     print(greenFont("*" * 70 + "\n" + "%35s\n" % ('copy file to HU') + "*" * 70 + "\n"))
#     p_scp.close()


def set_fazit_dict(keyNum=8):
    list1 = [x for x in range(1, keyNum)]
    list_svw = ['X9G-10103.05.2299990507', 'X9G-10103.05.2299990508', 'X9G-10103.05.2299990509',
                'X9G-10103.05.2299990510']
    list_faw = ['X9G-10203.05.2299990537', 'X9G-10203.05.2299990538', 'X9G-10203.05.2299990539',
                'X9G-10203.05.2299990540']
    return dict(zip(list1, list_svw + list_faw))


def copy_file_to_HU(file_path: str, dest_path: str = None):
    import hashlib
    """
    file_path: the copy file address
    dest_path: destination
    """
    ip = "192.168.1.4"
    # hu_zone = "/var/tmp/"
    hu_zone = "/tmp/"
    dest_path = "root@192.168.1.4:" + hu_zone
    print("cp " + file_path + " " + dest_path)
    # set timeout = -1
    p_command = "scp " + file_path + " " + dest_path
    p1 = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=None)
    p1.expect("password")
    p1.sendline("root")
    p1.expect("100%")
    time.sleep(1)
    p1.close()
    print(greenFont("*" * 70 + "\n" + "%35s\n" % ('copy file to HU') + "*" * 70 + "\n"))


def copy_file_to_HU_v2(file_path: str, dest_path: str = None):
    # file_path = "/home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh"
    # dest_path = "/media/jpcc/GP_navi_9000RC2"
    print("file", hash_file(file_path))
    p_command = "cp " + file_path + " " + dest_path
    p1 = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=None)
    # p1.expect("0916f4f69a8e4ed91efd307feeff10c5  /media/jpcc/GP_navi_9000RC2/vkms_init_pss.sh")
    # p1.send("sync")
    file_name = file_path.split('/')[len(file_path.split('/')) - 1]
    # dest_file = dest_path + "%s"%("/") + file_name
    dest_file = dest_path + "/" + file_name
    print("dest_file", hash_file(dest_file))


def hash_file(file_path: str, buf_size=32768):
    import hashlib
    # hashA = hashlib.sha256()           # get the hash algorithm
    hashA = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(buf_size)
            if not data:
                break
            hashA.update(data)
    # return 'SHA256: {0}'.format(sha256.hexdigest())
    return 'MD5: {0}'.format(hashA.hexdigest())


def checksum_HU_file(ip: str = None):
    import pexpect
    p_command = "ssh root@192.168.1.4"
    p_action = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=None)
    # p_action.logfile = sys.stdout
    # p_action.timeout = None
    # p_action.encoding = 'utf-8'
    i = p_action.expect(['password', pexpect.EOF, pexpect.TIMEOUT])
    if i == 0:
        p_action.sendline('root')
        # p_action.expect("root@mib-infotainment")
        p_action.expect("root@")
        p_action.sendline("cd /tmp/")
        p_action.expect("/tmp")
        p_action.sendline("for i in tsd.persistence.client.mib3.app.* vkms_i*;do md5sum $i;done")
        p_action.expect("496a4f978bc36289c9a7f07b286c70f0")
        p_action.expect("9eafcfb6bad8e051a115c2cfd8553b52")
        p_action.expect("4415e8ded07edd2b09f29e4a393acb8e")
        p_action.expect("0916f4f69a8e4ed91efd307feeff10c5")
        # check Getkey sha1_cheksum
        p_action.sendline("sha1sum tsd.persistence.client.mib3.app.GetKey")
        p_action.expect("880152e334d675794bea1f3616d1c94c147c1962")
        p_action.sendline("sync")
        p_action.sendline("exit")
        print("\n")
        print(greenFont("*" * 70 + "\n" + "%35s\n" % ('checksum is ok') + "*" * 70 + "\n"))
    elif i != 0:
        print(redFont("*" * 70 + "\n" + "%35s\n" % ('Error') + "*" * 70 + "\n"))
        print(p_action.before, p_action.after)
        return False
    p_action.close()
    return True


if __name__ == '__main__':

    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.InitPersistence")
    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.SetKey")
    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.GetKey")
    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/vkms_import_reset_dlc.sh")
    copy_file_to_HU("/home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh")
    # copy_file_to_HU_v2(file_path="/home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh", dest_path="/media/jpcc/GP_navi_9000RC2")
    print(checksum_HU_file())

    # IMPORTANT: uncomment the codes below before executing
    # p = pexpect.spawn(
    #     "scp /home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.InitPersistence    root@192.168.1.4:/tmp/",
    #     timeout=60, logfile=sys.stdout, encoding='utf-8')
    # p.expect("password")
    # p.sendline("root")
    # p.expect("100%")
    # p = pexpect.spawn(
    #     "scp /home/jpcc/Documents/modify_systeminfo/tsd.persistence.client.mib3.app.SetKey    root@192.168.1.4:/tmp/",
    #     timeout=60, logfile=sys.stdout, encoding='utf-8')
    # p.expect("password")
    # p.sendline("root")
    # p.expect("100%")
    # p = pexpect.spawn(
    #     "scp /home/jpcc/Documents/modify_systeminfo/vkms_import_reset_dlc.sh  root@192.168.1.4:/tmp/",
    #     timeout=60, logfile=sys.stdout, encoding='utf-8')
    # p.expect("password")
    # p.sendline("root")
    # p.expect("100%")
    # p = pexpect.spawn(
    #     "scp /home/jpcc/Documents/modify_systeminfo/vkms_init_pss.sh root@192.168.1.4:/tmp/",
    #     timeout=60, logfile=sys.stdout, encoding='utf-8')
    # p.expect("password")
    # p.sendline("root")
    # p.expect("100%")
    # import pprint

    # fazit_dict = set_fazit_dict()
    serialNum_0704 = input("Please input the serial num (i.e. 0701202200XX):")
    print(repr_message("Serial number: " + serialNum_0704))
    # fazitId_0712 = input("Please input the fazit id (i.e. X9G-101XX.XX.XX9999XXXX")
    # choice = input("Please select the fazit-id from the below list:\n" + pprint.pformat(fazit_dict))
    fazitId_0715 = input("Please select the fazit-id (i.e. X9G-10XXX.XX.XX9999XXXX:")
    # fazitId_0712 = fazit_dict[int(choice)]
    print(repr_message("Fazit id: " + fazitId_0715))
    # serialNum_0620 = 'VWX9GY0170935'
    # serialNum_0620 = '202206170014'
    # serialNum_0620 = 'VWX9GA88880014'
    # do_pexpect(serial_num=serialNum_0704, hw_version="X02", sw_version="C051", part_num="3JD035866")
    do_pexpect(serial_num=serialNum_0704, fazit=fazitId_0715, hw_version="X21", sw_version="C690",
               part_num="3GB035866B")
    # do_pexpect(serial_num=serialNum_0704, hw_version="X02")
    # do_pexpect(serial_num = serialNum, sw_version = 'C814')
    if write_status:
        print(greenFont("=" * 70 + "\n" + "%35s%s\n" % ('write_status:', write_status) + "=" * 70 + "\n"))
    else:
        print(redFont("?" * 70 + "\n" + "%35s%s\n" % ('write_status:', write_status) + "?" * 70 + "\n"))


    def str_to_hexStr(str_info):
        return binascii.hexlify(str_info.encode('utf-8')).decode('utf-8')
