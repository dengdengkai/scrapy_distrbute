#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="192.168.6.131", port=3306 , user="mysql", passwd="dk123456", db="youyuan", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
item = {'username': 'zhangsan', 'age': '18', 'header_url': 'header_url', 'images_url': 'i_l', 'content': '内容', \
       'place_from': '四川成都', 'education': '本科', 'hobby': '兴趣', 'source_url': 'source_url', \
       'source': 'source', 'time': '2018-2-20', 'spidername': 'youyuan'}
# 创建数据表SQL语句
cursor.execute(
    "insert into chengdu_18_25_mm (username, age, header_url, images_url, content, place_from, education, hobby, source_url, source, time, spidername) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    [item['username'], item['age'], item['header_url'], item['images_url'], item['content'],
     item['place_from'], item['education'], item['hobby'], item['source_url'], item['source'], item['time'],
     item['spidername']])
db.commit()

# 关闭数据库连接
db.close()
