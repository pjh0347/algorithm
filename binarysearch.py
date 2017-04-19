# coding: utf8

'''
Binary Search

time complexity : O(log n)
'''

import time
import bisect

def binarySearchForLoop(alist, x):
	begin = 0
	end = len(alist) - 1
	found = False
	pos = None

	while ( begin <= end ) and ( not found ):
		mid = ( begin + end ) // 2

		if alist[mid] == x:
			found = True
			pos = mid
		else:
			if x < alist[mid]:
				end = mid - 1
				pos = mid
			else:
				begin = mid + 1
				pos = begin

	return found, pos

if __name__ == '__main__':

	alist = [0, 1, 2, 8, 13, 17, 19, 32, 41]
	x = 42

	s = time.time()
	print binarySearchForLoop(alist, x)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	print bisect.bisect(alist, x)
	e = time.time()
	print "elapsed : ", e-s

