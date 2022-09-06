#!/usr/bin/python3.5

from coding_0906 import set_random_dict
import json

dict1 = set_random_dict()

if __name__ == '__main__':
    print(dict1)
    print(json.dumps(dict1, indent=4, separators=(", ", " = ")))
