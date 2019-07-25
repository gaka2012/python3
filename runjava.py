#!/usr/bin/python
# -*-coding:UTF-8 -*-
'''
测试程序，用来调用当前路径下的java程序，输入的参数是1,3,5.最后在shell上显示出来。
'''


import subprocess

arg1=1
arg2=3
arg3=5
subprocess.call('java HelloWorld %d %d %d' %(arg1,arg2,arg3),shell=True)
