# coding: utf8

'''
combination implementation
'''

import time
import itertools

def forLoop():
	l = [1, 2, 3, 4, 5]
	output = []
	for i in range(0, len(l)):
		for j in range(i+1, len(l)):
			output.append( (l[i], l[j]) )
	print output

def recursion():
	l = [1, 2, 3, 4, 5]
	n = 2
	def combination(l, n):
		if n == 0:
			return [()]
		r = []
		for i, v in enumerate(l):
			for j in combination(l[i+1:], n-1):
				r.append( (v,) + j )
		#print '\t' * n, n, 'of', l, '=', r
		return r
	print combination(l, n)

def itertool():
	l = [1, 2, 3, 4, 5]
	n = 2
	print list(itertools.combinations(l, n))

if __name__ == '__main__':

	s = time.time()
	forLoop()
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	recursion()
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	itertool()
	e = time.time()
	print "elapsed : ", e-s

