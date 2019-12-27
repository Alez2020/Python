# -*- coding:utf-8 -*-
'''
Created on 2019年5月27日 下午9:54:09

@author: AMIKE
'''
#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)