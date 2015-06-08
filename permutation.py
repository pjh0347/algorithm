# coding: utf8

'''
permutation

                                 n!
nPr = n(n-1)(n-2)...(n-r+1) = --------
                               (n-r)!

'''

import time
import itertools

def forLoop(l):
	output = []
	for i in range(0, len(l)):
		for j in range(0, len(l)):
			if i != j:
				output.append( (l[i], l[j]) )
	return output

def recursion(l, n):
	if n == 0:
		return [()]
	output = []
	for i, v in enumerate(l):
		for j in recursion(l[:i]+l[i+1:], n-1):
			output.append( (v,) + j )
	#print '\t' * n, n, 'of', l, '=', output
	return output

def itertool(l, n):
	return list(itertools.permutations(l, n))

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

