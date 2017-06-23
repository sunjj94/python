#!/usr/bin/env python3
#-*- coding:utf-8 -*-

product = {'1' : ['物品A',826],
           '2' : ['物品B',658],
           '3' : ['物品C',456],
           '4' : ['物品D',210]}

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

def buy(salary):
    num = input("\n请输入欲购买的产品编号:(按q退出)")
    flag = 0
    while 1:
        if (not num.isdigit() and (num == 'Q' or num == 'q')):            
            return num
        else:
            for k,v in product.items():
                if (k == num):
                    flag = 1
                    for x in v:
                        price = x
                    break
            if (not flag):
                num = input("编号输入有误，请重输(按q退出)：")
                flag = 0
            if (flag):                
                if (price > int(salary)):
                    num = input("您的余额不足！请重输(按q退出)：")
                    flag = 0
                else:
                    break
    return num

def add(salary):
    buy_list = []
    buy_dict = {}
    while int(salary) > 0:
        num = buy(salary)
        if (not num.isdigit() and (num == 'Q' or num == 'q')):
            print("已成功退出！")
            print("\n您此次购买的产品列表为：")
            for k,v in buy_dict.items():
                print("%2s %8s" % (k, v))
            print("\n您的余额为：%s" % salary)
            break
        else:
            buy_list.append(num)
            n = 0
            for i in buy_list:
                f = 0
                for k,v in product.items():
                    if (i == k):
                        for x in v:
                            if (not f):
                                p_name = x
                                f = 1
                        n = n + 1
                        buy_dict.setdefault(n, p_name)                       
            salary = int(salary) - x
            print("\n您的余额为： %s" % salary)
    return buy_dict
        

salary = input("请输入您的工资：")
while 1:
    if ((not salary.isdigit()) or (int(salary) <= 0)):
        salary = input("输入工资有误，请重输：")
    else:
        break
    
product_list()
add(salary)

            


