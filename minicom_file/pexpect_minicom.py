import pexpect
import sys
import time

minicom_script = {'minicom_script1':[
    {'expect': 'Welcome to minicom'},

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


class Minicom:
    @staticmethod
    def doPexpect(p_command):
        # with open("minicom_log.txt", 'w') as my_log_file:
        p_minicom = pexpect.spawn(command=p_command, logfile=sys.stdout, encoding='utf-8', timeout=30)
        # json_list = HU.get_json_info("p_script1.json", "$.p_script1.*")
        p_minicom.expect("password")
        p_minicom.sendline("jpcc")
        p_minicom.expect("Welcome to minicom")
        time.sleep(2)
        p_minicom.sendline("PWC:")
        p_minicom.sendline("cS 1 88")
        p_minicom.sendcontrol("a")
        # p_minicom.sendcontrol("m")
        p_minicom.sendline("x")
        p_minicom.sendcontrol("m")
        # if p_minicom ==
        # p_minicom.close()
        p_minicom.expect(pexpect.EOF)
        print("eof")
        # return HU.greenFont(HU.repr_message("Success to copy file to HU"))
        return "Successful"


if __name__ == '__main__':
    X=Minicom()
    print(X.doPexpect("sudo minicom"))