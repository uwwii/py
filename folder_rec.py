import os
from os import listdir
from os import path
import sys
import json

name = 'C:\\Users\\Пользователь\\Desktop\\folder_r\\'
def rec_folder(name):
    path = os.listdir(name)
    make_dict = {name: []}
    for i in path:
        make_path = os.path.join(name, i)
        if os.path.isfile(make_path):
            make_dict[name].append(make_path)
        else:
            make_dict[name].append(rec_folder(make_path))
    return make_dict

print(rec_folder(name))












