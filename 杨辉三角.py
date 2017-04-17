#!/usr/bin/end python3
#-*- coding:utf-8 -*-

def triangles():
	a = [1]
	while 1:
		yield a
		a.append(0)
		a=[a[i] + a[i - 1] for i in range(len(a))]

t = triangles()
n = 0
for x in t:
	print(x)
	n = n + 1
	if n == 10:
		break