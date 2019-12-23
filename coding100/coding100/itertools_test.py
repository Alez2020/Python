# -*-coding: utf-8 -*-
'''
Created on 2019年12月19日 下午7:41:10

@author: AMIKE
'''
import itertools

def Pi(n):
    # 奇数数列
    ns = itertools.count(1, 2)
    #取数列前n位
    m = itertools.takewhile(lambda x: x < 2*n, ns)
#     print(list(m))
    count = 1
    result = 0
    for x in m:
        result += 4 / x * (-1)**(count - 1)
        count += 1
    return result

print(Pi(10))
print(Pi(100))
print(Pi(1000))
print(Pi(10000))

assert 3.04 < Pi(10) < 3.05
assert 3.13 < Pi(100) < 3.14
assert 3.140 < Pi(1000) < 3.141
assert 3.1414 < Pi(10000) < 3.1415
print('ok')