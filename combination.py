# coding: utf8

# combination implementation by nested for loop

n = 5

for i in range(0, n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			for l in range(k+1, n):
				print i, j, k, l

