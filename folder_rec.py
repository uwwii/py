import os
from os import listdir
from os import path
import sys
import json


def rec_folder():
    #limit = sys.setrecursionlimit(4)
    name = 'C:\\Users\\Пользователь\\Desktop\\folder_r\\'
    path = os.listdir(name)
    make_dict = {name: path}
    list = []
    for path in make_dict:
        make_path = name + path
        if os.path.isfile(make_path):
            list.append(path)
        else:
            list.append({path: rec_folder()})
    return list


print(rec_folder())












