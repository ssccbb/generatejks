# -*- coding: UTF-8 -*-

import random


# 随机包名
def random_package():
    _center_lenght = random.randint(4, 7)
    _end_lenght = random.randint(5, 8)

    _strlist = list(random.sample('zyxwvutsrqponmlkjihgfedcba', _center_lenght + _end_lenght))
    _strlist.insert(_center_lenght, ".")
    _full_packagename = "com." + "".join(_strlist)

    return _full_packagename


# 随机包名列表
def random_package_list(_size):
    print("need package size --> " + str(_size))
    _package_list = set()
    print("random package generating...")
    while len(_package_list) < _size:
        _new_package = random_package()
        if _new_package in _package_list:
            _new_package = random_package()
            pass
        _package_list.add(_new_package)
    print("random package generate compelete!")
    return _package_list
