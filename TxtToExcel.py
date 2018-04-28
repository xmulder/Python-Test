#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import datetime
import time
import os
import sys
import xlwt

def txtToXls(TxtFilename,XlsName):
    print ("Starting converting xls......")
    
    #打开一个txt文件,该txt文件为utf-8编码
    f=open(TxtFilename,encoding='utf-8')
    
    #创建一个excel
    x=0
    y=0
    xlsTemp=xlwt.Workbook()
    styleHead=xlwt.XFStyle()
    styleBody=xlwt.XFStyle() 
    
    #设置字体
    fontSet=xlwt.Font()
    fontSet.bold=True
    fontSet.underline=True
    fontSet.height=12*20
    
    #居中设置
    align=xlwt.Alignment()
    align.horz=xlwt.Alignment.HORZ_CENTER
    align.wrap=xlwt.Alignment.WRAP_AT_RIGHT
    
    #设置单元格宽度
    border=xlwt.Borders()
    border.left=xlwt.Borders.THIN
    border.right=xlwt.Borders.THIN
    border.top=xlwt.Borders.THIN
    border.bottom=xlwt.Borders.THIN
    
    #应用字体到第一行标题栏风格
    styleHead.font=fontSet
    styleHead.alignment=align
    styleHead.borders=border
    
    #应用到表格数据部分的风格
    styleBody.borders=border
    styleBody.alignment.wrap=1
    styleBody.font.height=11*20

    
    #创建第一个表,名为"Banzou"
    sheetTemp=xlsTemp.add_sheet("BanZou",cell_overwrite_ok=True)
    sheetTemp.write(0,0,'UID',styleHead)
    sheetTemp.write(0,1,'KID',styleHead)
    sheetTemp.write(0,2,'Auther',styleHead)
    
    #设置单元格宽度
    for i in range(0,3):
        if i==2:
            sheetTemp.col(i).width=10000
        else:
            sheetTemp.col(i).width=3333
        
    #用while循环来一行一行写入txt文本到excel表中
    while True:
        a=1
        b=0
        
        #readline函数表示从txt文本中一行行的读取
        LineTemp=f.readline()
        if not LineTemp:
            break
        for i in LineTemp.split(' ',2):
            item=i.strip()
            sheetTemp.write(x+1,y,item,styleBody)
            y=y+1
        x=x+1
        y=0
    
    
    f.close()
    xlsTemp.save(XlsName+'.xls')      
       
if __name__=="__main__":
    TxtFilename=sys.argv[1]
    XlsName=sys.argv[2]
    txtToXls(TxtFilename,XlsName)