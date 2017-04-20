# coding: utf8

'''
Sorting Algorithms

Complexity       Time (worst)   Space (worst)
---------------------------------------------
bubble sort      O(n^2)         O(1)
selection sort   O(n^2)         O(1)
insertion sort   O(n^2)         O(1)
merge sort       O(n log n)     O(n)
quick sort       O(n^2)         O(log n)

'''

import time

def bubble_sort(alist):
	for i in xrange(len(alist)-1, 0, -1):
		for j in xrange(i):
			if alist[j] > alist[j+1]:
				tmp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = tmp
	return alist

def selection_sort(alist):
	for i in xrange(len(alist)-1, 0, -1):
		max_pos = i
		for j in xrange(i):
			if alist[j] > alist[max_pos]:
				max_pos = j
		tmp = alist[max_pos]
		alist[max_pos] = alist[i]
		alist[i] = tmp
	return alist

def insertion_sort(alist):
	for i in xrange(1, len(alist)):
		val = alist[i]
		pos = i - 1
		while ( pos >= 0 ) and ( val < alist[pos] ):
			alist[pos+1] = alist[pos]
			pos -= 1
		alist[pos+1] = val
	return alist

def merge_sort(alist):
	alist_len = len(alist)
	if alist_len > 1:
		mid = alist_len // 2
		left = merge_sort(alist[:mid])
		right = merge_sort(alist[mid:])
		i, j, k = 0, 0, 0
		left_len = len(left)
		right_len = len(right)
		while ( i < left_len ) and ( j < right_len ):
			if left[i] <= right[j]:
				alist[k] = left[i]
				i += 1
			else:
				alist[k] = right[j]
				j += 1
			k += 1
		while i < left_len:
			alist[k] = left[i]
			i += 1
			k += 1
		while j < right_len:
			alist[k] = right[j]
			j += 1
			k += 1
	return alist

def quick_sort(alist):
	alist_len = len(alist)
	if alist_len <= 1:
		return alist

	mid = alist_len // 2
	pivot = alist[mid]
	# TODO : list append 대신 다른 방식으로 처리해야 할 듯.
	less = []
	more = []
	equal = []
	for a in alist:
		if a < pivot:
			less.append(a)
		elif a > pivot:
			more.append(a)
		else:
			equal.append(a)

	return quick_sort(less) + equal + quick_sort(more)

if __name__ == '__main__':

	alist = [54,26,93,17,77,31,44,55,20]
	print alist

	s = time.time()
	alist = [54,26,93,17,77,31,44,55,20]
	print bubble_sort(alist)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	alist = [54,26,93,17,77,31,44,55,20]
	print selection_sort(alist)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	alist = [54,26,93,17,77,31,44,55,20]
	print insertion_sort(alist)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	alist = [54,26,93,17,77,31,44,55,20]
	print merge_sort(alist)
	e = time.time()
	print "elapsed : ", e-s

	s = time.time()
	alist = [54,26,93,17,77,31,44,55,20]
	print quick_sort(alist)
	e = time.time()
	print "elapsed : ", e-s

