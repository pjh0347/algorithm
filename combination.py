# coding: utf8

'''
combination

       nPr         n!
nCr = ----- = ----------
       r!      r!(n-r)!

'''

import time
import itertools

def forLoop(l):
	output = []
	for i in range(0, len(l)):
		for j in range(i+1, len(l)):
			output.append( (l[i], l[j]) )
	return output

def recursion(l, n):
	if n == 0:
		return [()]
	output = []
	for i, v in enumerate(l):
		for j in recursion(l[i+1:], n-1):
			output.append( (v,) + j )
	#print '\t' * n, n, 'of', l, '=', output
	return output

def itertool(l, n):
	return list(itertools.combinations(l, n))

if __name__ == '__main__':

	l = [1, 2, 3, 4, 5]
	n = 2

	s = time.time()
	print forLoop(l)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print recursion(l, n)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print itertool(l, n)
	e = time.time()
	print "elapsed : ", e-s

