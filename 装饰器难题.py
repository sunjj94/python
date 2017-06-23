#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
def log1(text):
	def wrapper1(func):
		print('%s %s' % (text, func.__name__))
		return func
	return wrapper1

@log1('test')
def now1():
	print('now1 run')

@log1('execute')
def today1():
	print('today1 run')

print()
print('*****	test1	*****')
now1()
today1()

####################################################################

def log2(text):
	if isinstance(text,str):
		def decorate2(func):
			def wrapper2(*args, **kw):
				print('%s %s' % (text, func.__name__))
				return func(*args, **kw)
			return wrapper2
		return decorate2
	else:
		def wrapper2(*args, **kw):
			print('call %s' % text.__name__)
			return text
		return wrapper2

@log2
def now2():
	print('now2 run')

@log2('execute')
def today2():
	print('today2 run')

print()
print('*****	test2	*****')
today2()
now2()

####################################################################


def log(func):
	def wrapper(*args, **kw):
		print('call %s' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def now():
	print('now it is ')

now()
print()
####################################################################
'''
def log3(text):
        def decorate(func):
                def wrapper(*arg,**kw):
                        print('%s %s' % (text, func.__name__))
                        return func(*arg, **kw)
                return wrapper
        return decorate

@log3('call')
def now3():
        print('this is now3')

print()
now3()
print()
now3()
####################################################################
print('**************************************')

def log4(text):
        def wrapper(func):
                print('%s %s' % (text, func.__name__))
                return func
        return wrapper

@log4('execute')
def now4():
        print('this is now4')

print()
now4()
print()
now4()

#'''
