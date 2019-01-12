#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'zfb'
# time: 19-01-11 19:35:12
import pymysql
import config

sqlist = []
sqlist.append(
    'create table if not exists chinese(\
        id int(20) not null auto_increment,\
        content varchar(20) default null,\
        nametype int(2),\
        primary key(id)\
    )engine=InnoDB default charset=UTF8MB4'
)
sqlist.append(
    'create table if not exists idiom(\
        id int(20) not null auto_increment,\
        content varchar(20) default null,\
        primary key(id)\
    )engine=InnoDB default charset=UTF8MB4'
)
sqlist.append(
    'create table if not exists japanese(\
        id int(20) not null auto_increment,\
        content varchar(20) default null,\
        primary key(id)\
    )engine=InnoDB default charset=UTF8MB4'
)
sqlist.append(
    'create table if not exists english(\
        id int(20) not null auto_increment,\
        content varchar(25) default null,\
        primary key(id)\
    )engine=InnoDB default charset=UTF8MB4'
)


def initdatabase(dbname):
    try:
        db = pymysql.connect(host='localhost', user='root', password=config.SQLPWD, port=3306)
        cursor = db.cursor()
        # 先删除原有数据库，防止插入时产生冲突
        cursor.execute("drop database if exists {}".format(dbname))
        cursor.execute(
            "create database if not exists {} default character set UTF8MB4".format(dbname))
        cursor.close()
        db.close()
        print("创建数据库{}成功".format(dbname))
    except Exception as e:
        print(e)


def inittable():
    try:
        db = pymysql.connect(host='localhost', user='root', password=config.SQLPWD, db=config.DBNAME, port=3306, charset='utf8')
        cursor = db.cursor()
        for sql in sqlist:
            cursor.execute(sql)
        cursor.close()
        db.close()
        print("数据表创建成功")
    except Exception as e:
        print(e)
