#!/usr/bin/python
# coding=utf-8
import os
import json
from json import JSONEncoder

import InfoParser


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class CategoryResponse:
    def __init__(self, pics):
        self.pic_list = pics


parser = InfoParser.PicParser(os.path.join(os.path.abspath('.'), "pictures.xlsx"))
parser.parse()
pic_info_list = parser.picList

pic_dic = {}
for pic_info in pic_info_list:
    if pic_info.category in pic_dic:
        pic_dic[pic_info.category].append(pic_info)
    else:
        pic_list = [pic_info]
        pic_dic[pic_info.category] = pic_list

dir_root = os.path.abspath("../docs/request/categories")
for key, pic_list in pic_dic.items():
    response = CategoryResponse(pic_list)
    fp = file(os.path.join(dir_root, key + '.json'), 'w')
    fp.write("")
    print key
    print json.dump(obj=response, cls=MyEncoder, fp=fp, indent=4)
