#!/usr/bin/env
#-*- coding:UTF-8 -*-
'''
Created on 2017年8月30日

@author: Administrator
'''

def listnum():
    n=0
    for n in range(0 , 5):
        print 'N的值：',n
    return;    

listnum() 

try:
    1 / 0
except Exception as e:
    '''异常的父类，可以捕获所有的异常'''
    print "0不能被除"
else:
    '''保护不抛出异常的代码'''
    print "没有异常"
finally:
    print "最后总是要执行我"