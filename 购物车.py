#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
需求:
    1. 启动程序后，让用户输入工资，然后打印商品列表
    2. 允许用户根据商品编号购买商品
    3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒 
    4. 可随时退出，退出时，打印已购买商品和余额

'''


product = {'1' : ['物品A',826],
           '2' : ['物品B',658],
           '3' : ['物品C',456],
           '4' : ['物品D',210]}

#列出商品列表函数
def product_list():    
    print("\n商品列表：")
    print("编号     物品    价格")
    for k,v in sorted(product.items()):
        f = 0
        for i in v:
            if (not f):
                p_name = i
                f = 1
        print("%2s %8s %8s" % (k,p_name,i))

#选择购买函数
def buy(salary):
    num = input("\n请输入欲购买的产品编号:(按q退出)")
    flag = 0 #flag为1表示编号有效，为0表示编号无效
    while 1:
        if (not num.isdigit() and (num == 'Q' or num == 'q')):#判断输入的是商品编号还是退出符
            return num
        else:
            for k,v in product.items():#判断输入的编号是否在列表内
                if (k == num):
                    flag = 1
                    for x in v:
                        price = x #记录下编号对应的价格
                    break
            if (not flag):
                num = input("编号输入有误，请重输(按q退出)：")
                flag = 0
            if (flag): #判断余额是否充足               
                if (price > int(salary)):
                    num = input("您的余额不足！请重输(按q退出)：")
                    flag = 0
                else:
                    break
    return num

#添加购物车函数
def add(salary):
    buy_list = []
    buy_dict = {}
    while int(salary) > 0:
        num = buy(salary)
        if (not num.isdigit() and (num == 'Q' or num == 'q')):#判断输入的是商品编号还是退出符
            print("已成功退出！")
            print("\n您此次购买的产品列表为：")
            for k,v in buy_dict.items():
                print("%2s %8s" % (k, v)) #输出购买清单
            print("\n您的余额为：%s" % salary) #输出余额
            break
        else:
            buy_list.append(num) #往购买清单中添加商品
            n = 0 #购买商品的序号
            for i in buy_list:
                f = 0 #标识购买编号是否在商品编号中找到
                for k,v in product.items():
                    if (i == k):#根据购买编号打印出购买清单
                        for x in v:
                            if (not f):
                                p_name = x
                                f = 1
                        n = n + 1
                        buy_dict.setdefault(n, p_name)#在字典中添加键值                       
            salary = int(salary) - x
            print("\n您的余额为： %s" % salary)
    return buy_dict
        
#主函数开始
salary = input("请输入您的工资：")
while 1:
    if ((not salary.isdigit()) or (int(salary) <= 0)):#判断工资是否是数字并且大于0
        salary = input("输入工资有误，请重输：")
    else:
        break
    
product_list()
add(salary)

            


