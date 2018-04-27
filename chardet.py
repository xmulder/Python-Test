#!/usr/bin/python
# -*- coding: UTF-8 -*-
#利用chardet库来检测txt文件的编码,在命令行下执行python chardet.py XXX.txt

import chardet
import sys

def fileCodeTest(filename):
    file=open(filename,'rb')
    result=chardet.detect(file.read())
    return result
    
if __name__=="__main__":
    filename=sys.argv[1]
    codetest=fileCodeTest(filename)
    print (codetest)   
