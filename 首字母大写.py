#!/usr/bin/end python3
#-*- coding:utf-8 -*-

from functools import reduce
def fun1(a,b):
	return a + b
def fun2(c):
	L3 = []
	j = 0
	for d in c:
		i = 0
		L1 = []
		for x in d:
			if i == 0:
				x = x.upper()
				L1.append(x.upper())
				i += 1
			else:
				x = x.lower()
				L1.append(x.lower())
		L2 = reduce(fun1,L1)
		L3.append(L2)
	print(L3)

c=['adam', 'LISA', 'barT']
fun2(c)

