# -*- coding: UTF-8 -*-
import os, config, shutil

_jks_file_ = config.__dir + "/jks"
_jks_info_ = "jksinfo.txt"


# 准备文件夹
def mkdir():
    delete()
    os.mkdir(_jks_file_)
    print("path(" + _jks_file_ + ") has creat!")
    print("need jks number -- " + str(config.__jks_number) + " -- ready to create path...")
    for num in range(config.__jks_number):
        os.mkdir(_jks_file_ + "/" + str(num + 1))
    print("listdir -- " + str(os.listdir(_jks_file_)))
    pass


# 创建jksinfo.txt
def creat_jksinfo():
    _need_jksinfo = config.__jks_info
    if not _need_jksinfo:
        print("do not need jksinfo.txt! skip")
        pass
    for path in os.listdir(_jks_file_):
        # 不存在会自动创建
        _file = open(_jks_file_ + "/" + path + "/" + _jks_info_, "w")
        # 清空文本文件内容
        _file.truncate()
        _file.close()
        print(_file)
    pass


# 递归删除文件夹
def delete():
    if os.path.exists(_jks_file_):
        # jks递归
        for _dir in os.listdir(_jks_file_):
            # 顺序递归
            for _child_file in os.listdir(_jks_file_ + "/" + _dir):
                # 删除jksinfo.txt & xxx.jks
                os.remove(_jks_file_ + "/" + _dir + "/" + _child_file)
            shutil.rmtree(_jks_file_ + "/" + _dir)
            pass
        shutil.rmtree(_jks_file_)
        print("path(" + _jks_file_ + ") already remove")
    pass


# 删除oldjks
def deleteOldJKS(_file):
    if os.path.exists(_file):
        os.remove(_file)
    pass


# 写入jksinfo
def writeJKSInfo(_jks_info, _jks_info_dir):
    print("start write file ..."+_jks_info_dir)
    if os.path.exists(_jks_info_dir):
        _jks_file = open(_jks_info_dir, "w")
        _jks_file.write(_jks_info)
        _jks_file.close()
        print("write done!")
        pass
    pass
