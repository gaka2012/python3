#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
from datetime import *
import subprocess

#首先将weight.dat中大于250km的地震台站删除。
path1='/home/zhangzhipeng/software/gcap'
ls=os.listdir(path1)
for event1 in ls:
    if event1[0:2]=='20' and len(event1)==14:  #找到所有的事件的文件。
        weightname=path1+'/'+event1+'/'+'weight.dat'      
        fp1=open(weightname,'r') #打开每个事件中的weight.dat文件
        all1=fp1.readlines()   
        fp1.close()
        fpempty=open(weightname,'w+') #清空weight.dat
        fpempty.close()

        for line1 in all1:
            divi1=line1.split()
            distance1=int(divi1[1])
            if distance1>250 :   #如果震中距大于250km，则删除
                continue                                      #因为计算的格林函数大于10小于250
            elif distance1<10:   #如果震中距小于10km，则删除。
                continue
            else:
                fp2=open(weightname,'a+')
                fp2.write(line1)
                fp2.close()




#第二步，读取catalog中changning2009.txt中的震级作为参数。运行run_gcap.pl
catalog=open('changning2009.txt','r')
all1=catalog.readlines()
for line1 in all1:
    di=line1.split()
    bjtime=di[0][0:4]+di[0][5:7]+di[0][8:]+di[1][0:2]+di[1][3:5]+di[1][6:8]
    origin=datetime.strptime(bjtime,"%Y%m%d%H%M%S")
    gmttime=origin-timedelta(hours=8)
    eventname=gmttime.strftime("%Y%m%d%H%M%S") #将txt中时间减去8个小时
   # print (eventname,type(eventname)) eventname就是以gmt时间为标准的事件名称，可以带入反演
    #print (di[5])                     di[5]是震级，带入反演
    subprocess.call('cd ~/software/gcap;perl run_gcap.pl cn_1/%s %s 30 1' %(di[5],eventname),shell=True)
    #./run_gcap.pl cn_1/3.9 20090124080053 30 1



