#!/usr/bin/python
# -*- coding:UTF-8 -*-
import threading
import time

'''
def run(n):
    print("task", n,threading.current_thread())
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)
'''

'''
def run(n):
    for i in range(n):
        print (i,threading.current_thread())

start=time.clock() #开始事件，与下面的end相呼应，相减后就是程序的运行时间。

t_list=[]
for i in range(2):
    t=threading.Thread(target=run,args=(1000,))
    t.start()
    t_list.append(t) #之所以添加打列表是为了下面的for循环好写。
for arg in t_list:   
    t.join()        #join使得子线程完成之后再运行主线程。阻塞主线程

end=time.clock()
t=end-start
print("Runtime is :",t,threading.current_thread()) #输出当前线程，如果是主线程旧输出MainThread
'''

'''
from multiprocessing import Pool
def work(x):
    for i in range(x):
        print (i)
start=time.clock()
pool = Pool(processes=4) # 4个线程
x = [1,2,3,4,5,6]
results = pool.map(work, x)
end=time.clock()
print (end-start)
'''

'''
本程序用来测试多线程，当子函数run中的time.sleep没有被注释掉时，单发执行本程序耗时6秒，多线程耗时2s
当time.sleep被注释掉之后，单发执行本程序耗时0.0001秒，多线程耗时0.13秒。主要是因为当运行至time.sleep时，
time.sleep并不消耗CPU，因此可以进行线程的切换，极大的减少了运行时间。但是，普通的运行，比如计算是消耗CPU的
这是多线程是没有多大意义的，只有不消耗CPU的操作，比如读写文件时，多线程才是有意义的。
'''
import time
from multiprocessing import Pool
def run(fn):
  
  #fn: 函数参数是数据列表的一个元素
  #time.sleep(1)
  return fn*fn
  
testFL = [1,2,3,4,5,6]  
print ('shunxu:') #顺序执行(也就是串行执行，单进程)
s = time.time()
for fn in testFL:
  run(fn)

e1 = time.time()
print ("顺序执行时间：", (e1 - s))

print ('concurrent:') #创建多个进程，并行执行
pool = Pool(5)  #创建拥有5个进程数量的进程池
  #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
rl =pool.map(run, testFL) 
pool.close()#关闭进程池，不再接受新的进程
pool.join()#主进程阻塞等待子进程的退出
e2 = time.time()
print ("并行执行时间：", (e2-e1))
print (rl)

#以下程序使用多线程多参数调用程序
#############################################################################################
import time
import subprocess
import numpy as np
import threading
from multiprocessing import Pool


def mulfilter(item):
    (name2,filterwindow1,longt,tup1,t1,t2)=item #这一步也是必不可少的
    subprocess.call('cd /home/zhangzhipeng/software/filterpicker/picker;./picker_func_test mer1.sac /home/zhangzhipeng/software/filterpicker/picker/result/%s  %s %s %s %s %s' %(name2,filterwindow1,longt,tup1,t1,t2),shell=True)
   
#parameter=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #单个参数的多线程参数输入。
#parameter=[(1,300,300,31,14,10),(2,300,300,31,14,10.5),(3,300,300,31,14.5,10),(4,300,300,31,14.5,10.5)]#多个参数的多线程参数输入。
#注意是列表中有元组。
list1=[1,300,300,31,14,10]
list2=[2,300,300,31,14,10.5]
list3=[3,300,300,31,14.5,10]
list4=[4,300,300,31,14.5,10.5] 
parameter=[]
parameter.append(tuple(list1)) #将列表转换成元组。
parameter.append(tuple(list2))
parameter.append(tuple(list3))
parameter.append(tuple(list4))
start=time.time()
pool=Pool(4)
rl=pool.map(mulfilter,parameter)
pool.close()
pool.join()
end=time.time()
inter=end-start
print (inter)













