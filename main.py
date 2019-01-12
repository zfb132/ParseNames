#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 19-01-10 23:58:14
import time
import pymysql
import config
import SQLHelper

# 中国人名字
CNNAMES = './src/Chinese_Names_Corpus（120W）.txt'
# 古代中国人名字
CNANAMES = './src/Ancient_Names_Corpus（25W）.txt'
# 中国成语
CNIDIOM = './src/ChengYu_Corpus（5W）.txt'
# 日本人名字
JPNAMES = './src/Japanese_Names_Corpus（18W）.txt'
# 英国人名字
ENNAMES = './src/English_Names_Corpus（2W）.txt'
# 英国人名翻译
EN2CNNAMES = './src/English_Cn_Name_Corpus（48W）.txt'


def loaddata(sql, cursor):
    # load data local infile './names.txt' into table chinesename
    # fields terminated by '\t' lines terminated by '\r\n' ignore 1 lines;
    # 各属性以\t分割，每条记录以\r\n分割，忽略第一行数据
    # 设置允许load命令
    cursor.execute('SET @@GLOBAL.local_infile:=1;')
    # 开始信息插入到数据库
    try:
        print(sql)
        cursor.execute(sql)
        cursor.execute("commit")
    except Exception as e:
        print(repr(e))


def getdata():
    db = pymysql.connect(host='localhost', user='root',
                         password=config.SQLPWD, db=config.DBNAME,
                         port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute('select * from chinese limit 100')
    result = cursor.fetchall()
    print(result)


def main():
    SQLHelper.initdatabase(config.DBNAME)
    SQLHelper.inittable()
    db = pymysql.connect(host='localhost', user='root',
                         password=config.SQLPWD, db=config.DBNAME,
                         port=3306, charset='utf8', local_infile=True)
    cursor = db.cursor()
    templist = [(CNNAMES, 0), (CNANAMES, 1), (EN2CNNAMES, 2)]
    # 1. 单条插入最慢
    # 2. 多条插入后再提交事务稍快
    # 3. load data最快
    # 注意：有的系统上面要以\r\n分割行，有的系统要以\n分割行
    for name in templist:
        sql = "load data local infile '{}' into table chinese " \
              "lines terminated by '\\r\\n' ignore 3 lines (content) set nametype={};" \
            .format(name[0], name[1])
        loaddata(sql, cursor)
    templist = [(CNIDIOM, 'idiom'), (JPNAMES, 'japanese'), (ENNAMES, 'english')]
    for name in templist:
        sql = "load data local infile '{}' into table {} " \
              "lines terminated by '\\r\\n' ignore 3 lines (content) ;" \
            .format(name[0], name[1])
        loaddata(sql, cursor)
    cursor.close()
    db.close()


if __name__ == '__main__':
    time_start = time.time()
    main()
    # getdata()
    time_end = time.time()
    print('运行时间{}'.format(time_end - time_start))

'''
import os
import time
import ctypes
import threading  # 导入进程

NUM_THREAD = 4
COUNT = 0
lock = threading.Lock()
fd = open('./src/Chinese_Names_Corpus（120W）.txt', 'r')

def preprocess(filename, nametype):
    tempname = filename.replace('.txt', '-1.txt')
    fd = open(tempname, 'a')
    with open(filename, 'r') as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            line = line.replace('\n', '') + "****{}\n".format(nametype)
            fd.write(line)
    fd.close()
    return tempname

def thread_func(data, i):
    global COUNT
    global lock
    try:
        lock.acquire()
        COUNT += i
        txt = next(fd)
        # print('当前线程id={}, 主线程id={}'.format(threading.get_ident(),threading.main_thread()))
        # print('当前线程id={}, 主线程id={}'.format(os.getpid(),os.getppid()))
        print('当前线程id={}'.format(ctypes.CDLL('libc.so.6').syscall(186)))
        print('{}'.format(txt))
    except EOFError as e:
        print('最后一行'+str(e))
    except Exception as e:
        # print('当前线程id={}, 主线程id={}'.format(threading.get_ident(),threading.main_thread()))
        # print('当前线程id={}, 主线程id={}'.format(os.getpid(),os.getppid()))
        print('当前线程id={}'.format(ctypes.CDLL('libc.so.6').syscall(186)))
        print('当前count={}, data={}'.format(COUNT, data[0]))
    finally:
        lock.release()


def gettotallines(filename):
    f = os.popen('wc -l {}'.format(filename), "r")
    totallines = f.read().split()[0]
    f.close()
    print(totallines)


def main():
    threads = []
    data = [1, 2, 3, 4]
    for i in range(NUM_THREAD):
        t = threading.Thread(target=thread_func, args=(data, i))
        threads.append(t)
    for i in range(NUM_THREAD):
        threads[i].start()
    for i in range(NUM_THREAD):
        threads[i].join()
    print("主进程{}启动{}个子线程".format(os.getpid(), NUM_THREAD))


if __name__ == '__main__':
    # init('./Chinese_Names_Corpus（120W）.txt')
    time_start = time.time()
    main()
    time_end = time.time()
    print('运行时间{}'.format(time_end - time_start))
'''
