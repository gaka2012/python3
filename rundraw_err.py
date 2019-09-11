#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import subprocess

'''
#第三步，将draw_err.sh复制到每一个地震事件文件中，然后运行。
path1='/home/zhangzhipeng/software/gcap'
ls=os.listdir(path1)
for event1 in ls:
    if event1[0:2]=='20' and len(event1)==14:  #找到所有的事件的文件。
        subprocess.call('cd ~/software/gcap;cp draw_err.sh %s' %(event1),shell=True)
        #os.system('cd ~/software/gcap;cp draw_err.sh %s',%) #将draw_err.sh复制到每一个地震事件中，并运行。
        subprocess.call('cd ~/software/gcap;./draw_err.sh',shell=True)
'''


#第1步，找到每个事件中的out文件，读取其中的某项信息。
path1='/home/zhangzhipeng/software/gcap'
ls=os.listdir(path1)
for event1 in ls:
    if event1[0:2]=='20' and len(event1)==14:  #找到所有的事件的文件。
        minerr=1000
        maxerr=0
        for i in range(1,31):
            out=path1+'/'+event1+'/'+'cn_'+str(i)+'.out'                      
            fp1=open(out,'r')       #读取每一个out文件
            all1=fp1.readlines()
            fp1.close()
            j=0                     #加个计数器，只读第一行
            for line1 in all1:
                if j <1:
                    di=line1.split()
                    fp2=open('temp.txt','a+')
                    mag=float(di[9])*0.2  #调整震源球的大小，根据震级来调
                    fp2.write(str(i)+' '+di[11]+' '+str(i)+' '+di[5]+' '+di[6]+' '+di[7]+' '+str(mag)+' '+'0 0'+'\n')
                    fp2.close()
                    j+=1
                    if float(di[11])<minerr:
                        minerr=float(di[11])
                    if float(di[11])>maxerr:
                        maxerr=float(di[11]) 
        print (minerr,maxerr)#找到所有的误差中的最大和最小值，用于gmt画图。                        
        err_inc=(maxerr-minerr)/10.0  
        minerr=minerr-err_inc
        maxerr=maxerr+err_inc
        print (err_inc)
        #temp中存储着psmeca所需要的参数，包括深度，误差，深度，走向，倾角，滑动角，震级，0,0(震源球画在原始位置)
        fp2=open('temp.txt','r')
        all1=fp2.readlines()
        fp2.close()
        #写入gmt文件
        draw=open('draw_err.gmt','a+')
        draw.write('#!/bin/bash'+'\n')
        draw.write('R=0/31/'+str(minerr)+'/'+str(maxerr)+'\n')
        draw.write('J=X6.0i/6.0i'+'\n')
        draw.write('PS=0draw_err.ps'+'\n')
        draw.write('gmt psxy -R$R -J$J -T -K -P > $PS'+'\n')
        draw.write('gmt psbasemap -X1i -Y1.5i -R$R -J$J -K -O -B1:"depth(km)":/'+str(err_inc)+':"error":WSne >> $PS'+'\n')
        draw.write('gmt psmeca -R -JX -Sa2.0/-1 -G255/0/0  -E245/245/245 -P  -B -O temp.txt >> $PS'+'\n')
        draw.write('gmt psxy  -R -J -T -O >> $PS')
        draw.close() 
        #调用gmt文件
        subprocess.call('cd ~/software/gcap;chmod +x draw_err.gmt',shell=True)
        subprocess.call('cd ~/software/gcap;./draw_err.gmt',shell=True)
        #将ps文件移动到地震事件中，并删除不需要的其他东西。
        subprocess.call('cd ~/software/gcap;cp 0draw_err.ps %s' %(event1),shell=True)
        subprocess.call('cd ~/software/gcap;rm 0draw_err.ps draw_err.gmt temp.txt gmt.history',shell=True)
            
            
            
            
            
            
            
            
            
            
            
            
            
            

