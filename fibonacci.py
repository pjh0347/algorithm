# coding: utf8

'''
Finding Fibonacci numbers

0 1 1 2 3 5 8 13 21 34 55 89
0 1 2 3 4 5 6 7  8  9  10 11

time complexity : O(n)
'''

import time


def fibonacciForLoop(n):
	a, b = 0, 1
	for i in xrange(n-1):
		a, b = b, a+b
	return b

def fibonacciDynamic(n):
	fib = [0] * (n + 2)
	fib[1] = 1
	for i in xrange(2, n+1):
		fib[i] = fib[i-1] + fib[i-2]
	return fib[n]

def fibonacciRecursion(n):
	if n <= 1:
		return n
	return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

if __name__ == '__main__':

	n = 35

	s = time.time()
	print fibonacciForLoop(n)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print fibonacciDynamic(n)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print fibonacciRecursion(n)
	e = time.time()
	print "elapsed : ", e-s

