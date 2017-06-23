#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
编写登陆接口需求：
    1、输入用户名和密码；
    2、认证成功后显示欢迎信息；
    3、输错三次后锁定。
'''


UserMsg = {'User1' : '123',
           'User2' : '456',
           'User3' : '789'}

i = 0
flag = 0
while (i < 3 and (not flag)):
    username = input("请输入用户名：")
    userpwd = input("请输入密码：")
    i = i + 1
    for k, v in UserMsg.items():
        if (username == k and userpwd == v):
            print (k)
            print("登陆成功！")
            print()
            flag = 1
            break  
    if (not flag):
        print("登陆信息有误，请重输！")
        print()

if (not flag):
    print("多次输入失败，已锁定")
    print()
            
