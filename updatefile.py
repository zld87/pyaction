import os
import xlrd,xlwt
from xlutils.copy import copy
import openpyxl

#修改文件名称
#os.renames(os.path.join(os.getcwd(),'testreq.py'),'updatefile.py')

workbook=openpyxl.load_workbook("/Users/zhouliudong/Desktop/JKSTACK OKR-2021Q2.xlsx")
print(workbook.get_sheet_names())

for i in workbook.get_sheet_names():
    if i =="测试部-功能测试":
        pass
    else:
        print(workbook.get_sheet_by_name(i))
        workbook.remove_sheet(workbook.get_sheet_by_name(i))

workbook.save("/Users/zhouliudong/Desktop/周浏栋_Q2.xlsx")




