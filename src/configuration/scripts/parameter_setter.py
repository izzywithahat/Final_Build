#!/usr/bin/env python
import rospy
import json
import os
from types import *

def parseJSON(path,json):
    for k in json:
        if type(json[k]) is DictType:
            for k2 in json[k]:
                parseJSON(path+"/"+k,json[k][k2])
        print(k)
        print(json)
        rospy.set_param(path+"/"+k,json[k])

def main():
    cwd = os.getcwd()
    path = os.path.join(cwd, 'src/configuration/global_config.json')
    config = json.load(open(path))
    parseJSON("/",config)



if __name__ == "__main__":
    main()
