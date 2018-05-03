#!/usr/bin/python
# -*- coding: UTF-8 -*-
#利用chardet库来检测txt文件的编码,在命令行下执行python chardet.py XXX.txt

import chardet
import sys

def fileCodeTest(filename):
    #参数'rb'的意思是以二进制读模式打开文件
    file=open(filename,'rb')
    filetext=file.read()
    result=chardet.detect(filetext)
    return result
    file.close()
    
if __name__=="__main__":
    filename=sys.argv[1]
    codetest=fileCodeTest(filename)
    print (codetest)    