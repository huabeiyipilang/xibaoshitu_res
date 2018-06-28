#!/usr/bin/python
import os

import InfoParser
import sqlite3

dir_root = "/Users/carl/PycharmProjects/babylearnpic"
parser = InfoParser.PicParser(os.path.join(dir_root, "pictures.xlsx"))
parser.parse()
pic_info_list = parser.picList

db_path = os.path.join(dir_root, 'picinfo.db')
if os.path.isfile(db_path):
    os.remove(db_path)
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('''CREATE TABLE picinfo (
  id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  category char(128),
  name char(128),
  origin_url char(128)
);''')

insert_sql = 'INSERT INTO picinfo (category,name,origin_url) VALUES ("{0}", "{1}", "{2}");'

for pic_info in pic_info_list:
    c.execute(insert_sql.format(pic_info.category, pic_info.name, pic_info.path))
    print 'insert:', pic_info

conn.commit()
conn.close()