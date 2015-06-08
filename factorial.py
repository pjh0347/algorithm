# coding: utf8

'''
factorial

n! = n(n-1)(n-2)...3*2*1

'''

import time
import math

def recursion(n):
	if n <= 0:
		return 1
	else:
		return n * recursion(n-1)

def tailRecursion(n):
	def loop(n, output):
		if n <= 0:
			return output
		else:
			return loop(n-1, n*output)
	return loop(n, 1)

def whileLoop(n):
	output = 1
	while n > 0:
		output = n * output
		n -= 1
	return output

def mathModule(n):
	return math.factorial(n)

if __name__ == '__main__':

	n = 3

	s = time.time()
	print recursion(n)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print tailRecursion(n)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print whileLoop(n)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print mathModule(n)
	e = time.time()
	print "elapsed : ", e-s

