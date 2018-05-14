#-*- coding:utf-8 -*-
from datetime import datetime
import datetime
#找出当天时间是周几，然后计算与周末的时间差
today = datetime.datetime.now().weekday()
#print '今天星期：'+str(today+1)

index1 = 5-today
index2 = 6-today

if index1 ==0 :
    saturday = datetime.datetime.today().strftime('%Y-%m-%d')
else:
    saturday = (datetime.datetime.now()+datetime.timedelta(days = index1)).strftime('%Y-%m-%d')
#print ('saturday is :'+saturday)

if index2 ==0 :
    sunday = datetime.datetime.today().strftime('%Y-%m-%d')
else:
    sunday = (datetime.datetime.now()+datetime.timedelta(days = index2)).strftime('%Y-%m-%d')
#print ('sunday is :'+sunday)
