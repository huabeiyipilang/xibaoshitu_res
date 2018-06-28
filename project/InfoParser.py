# coding=utf-8
__author__ = 'carl'
import os
import sys
import xlrd


class PicInfo:
    def __init__(self, category, name, path):
        self.category = category
        self.name = name
        self.path = path

    def __str__(self):
        return self.category + " " + self.name + " " + self.path

    def __dict__(self):
        return {'category': self.category, 'name': self.name, 'path': self.path}


class PicParser:
    def __init__(self, file_path):
        self.filePath = file_path
        self.picList = []

    def parse(self):
        if not os.path.isfile(self.filePath):
            print 'File not found! :', self.filePath
            return
        reload(sys)
        sys.setdefaultencoding('utf-8')
        xlsx_file = xlrd.open_workbook(self.filePath)
        # 读取第一sheet
        info_sheet = xlsx_file.sheet_by_index(0)
        row = 1
        while row < len(info_sheet._cell_values):
            row_data = info_sheet.row_values(row)
            pic_url = row_data[2]
            end = pic_url.index('?')
            picInfo = PicInfo(row_data[0], row_data[1], pic_url[0:end])
            self.picList.append(picInfo)
            # print picInfo
            row = row + 1
