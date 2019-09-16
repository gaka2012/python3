#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
import subprocess
import threading
from multiprocessing import Pool

def test1(dep):

    subprocess.call('cd ~/software/gcap;cap.pl -C0.05/0.16/0.05/0.08 -D1.2/0.8/0.2 -F -L0.6 -H0.05 -I10/0.1 -J0./0./0./0 -S5/10/0 -T30/70 -Mcn_%s/4.2 -X0 -R0/360/0/90/-180/180 -P0.3 20190426171912' %(dep),shell=True)
    
parameter=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start=time.time()
pool=Pool(5)
rl=pool.map(test1,parameter)
pool.close()
pool.join()
end=time.time()
inter=end-start
print (inter)

# 71.61318731307983
