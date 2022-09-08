#!/usr/bin/python3.5
"""
Add on 9/8/2022, at 1:02 PM
"""

from sub_action import Sub
import jsonpath,json,os,sys

class new_sub(Sub):

    # init_dict = {
    #     'p_read_script1': [{'expect': 'password'}, {'sendline': 'root'}, {'expect': 'root@'}, {'sendline': 'cd /tmp/'},
    #                        {'expect': '/tmp'}]}
    ns_0x04000000 = ['29185', '29187', '29188', '29190', '29193', '29195', '29196', '29197', '29200', '29201', '29202',
                     '29203', '29206']
    ns_0x01000100 = ['2843']
    ns_0x01000000 = ['1276']



    @staticmethod
    def set_Getkey(json_data, ns="0x01000000"):
        """

        :param json_data:
        :param ns: like 0x01000000
        :return: completed json_data
        """
        RDI_list = jsonpath.jsonpath(json_data, "$..RDI")
        """
        >> ['0x04FB', '0x04FC', '0x04FE', '0x0505', '0x050E', '0x050F']
        """
        for key in RDI_list:
            if key == "0x7213":
                print('we found it')
            Sub.init_dict['p_read_script1'].append(
                {"sendline": "tsd.persistence.client.mib3.app.GetKey --ns {0} --key {1}".format(ns, key)})
            # print("type of %s is" % key, type(key))
            Sub.init_dict['p_read_script1'].append(
                # {"sendline": "load: ns: {0} key: {1} slot: 0 status: 0".format(ns[3:], str(int(key,16)))})
                {"expect": "load: ns: {0} key: {1} slot: 0 ".format(ns[3:], str(int(key, 16)))})
        Sub.init_dict['p_read_script1'].append({'sendline': 'sync'})
        Sub.init_dict['p_read_script1'].append({'sendline': 'exit'})
        return Sub.init_dict





if __name__ == '__main__':
    X = new_sub()
    print(X.init_dict)