# -*-coding: utf-8 -*-
'''
Created on 2019年12月18日 下午8:57:04

@author: AMIKE
'''
# Hmac算法：Keyed-Hashing for Message Authentication。
# 它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中

import hmac
import random

message = b'hello world'
key = b'secret'
hm = hmac.new(key, message, digestmod='MD5')
print(hm.hexdigest())

db = {}

def hmac_md5(key, msg):
    return hmac.new(key.encode('utf_8'), msg.encode('utf-8'), 'MD5').hexdigest()

class User():
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(1, 100)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

def register(username, password):
    if username not in db.keys():
        db[username] = User(username, password)
    else:
        print('username exist')

def logon(username, password):
    if username not in db.keys():
        print('user:%s not exist' % username)
    else:
        user = db[username]
        if user.password == hmac_md5(user.key, password):
            print('%s log in' %username)
        else:
            print('password error')

print('--------register begin----------')
register('Alice', '123456')
register('Alex', 'abc123')
register('Jerry', '999999')
print('--------register end----------')
print(db)
logon('Alice', '123456')
logon('Alex', 'abc123')
logon('Jerry', '999999')
logon('Alez', '123456')
logon('Alice', '456123')
