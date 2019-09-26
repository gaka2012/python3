# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:31:02 2019

@author: 12248
本程序用来将FM转换成msatsi程序所要用的的数据格式
原始数据格式为      lon lat strike dip rake
生成的数据格式为     x   y   dip direction dip rake 
                   x,y是根据经纬度生成的，几乎是一致的。
"""
from interval import Interval

fa=open('FM.txt','r') 
a1=fa.readlines()
fa.close()

for line1 in a1:
    part=line1.split()
    lon=float(part[0]) #1获得经纬度
    lat=float(part[1])
    #2分区得到的x，y就是分区后的结果
    for i in range(27,30): #纬度范围是27-30  所有数据都在这一范围内，没有正好在边界的，所以不用考虑边界问题。
        zoom2=Interval(i,i+1,upper_closed=False)#左边是闭区间，右边是开区间
        if lat in zoom2:
            y=i
    for j in range(103,107):#经度范围是103-107
        zoom1=Interval(j,j+1,upper_closed=False)
        if lon in zoom1:
            x=j
    #3将strike转换成dip direction
    if float(part[3])+90<=360 :                   
        part[3]=str(float(part[3])+90)
    elif float (part[3])+90>360:
        part[3]=str(float(part[3])-270)
    #4将结果写入文件
    fa=open('result.txt','a+')
    fa.write(str(x)+' '+str(y)+' '+part[3]+' '+part[4]+' '+part[5]+'\n')
    fa.close()

                                                               #interval用法示例
###############################################################################
'''
from interval import Interval
zoom1=Interval(2,5) #默认是闭合区间
zoom2=Interval(2,5,lower_closed=False) #设置左边的区间是开区间 upper_closed  
zoom3=Interval(2,5,closed=False) #直接设置上下都是开区间
print (2 in zoom1)
print (2 in zoom2)
i=2
zoo4=Interval(i,i+1)
print (2.5 in zoo4)
'''


                    