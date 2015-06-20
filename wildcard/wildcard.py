# coding:utf-8

from multiprocessing import Pool
import pprint

class Problem(object):

	def __init__(self, inputFile, outputFile, parser, solver, merger, parallel=1):
		object.__init__(self)
		self.inputFile = inputFile
		self.outputFile = outputFile
		self.parser = parser
		self.solver = solver
		self.merger = merger
		self.pool = Pool(processes=parallel)
	
	def run(self):
		inputData = self.read()
		inputList = self.parser(inputData)
		outputList = self.solve(inputList)
		outputData = self.merger(outputList)
		self.write(outputData)

	def read(self):
		f = open(self.inputFile)
		inputData = f.read()
		f.close()
		return inputData

	def write(self, outputData):
		f = open(self.outputFile, 'w')
		f.write(outputData)
		f.close()

	def solve(self, inputList):
		return self.pool.map(self.solver, inputList)

def parser(inputData):
	inputList = []

	lineList = inputData.splitlines()
	#print lineList

	idx = 0
	t = int(lineList[idx])

	for i in range(t):
		idx += 1
		w = lineList[idx].strip()

		idx += 1
		n = int(lineList[idx])

		l = []
		for j in range(n):
			idx += 1
			l.append( lineList[idx].strip() )
		
		inputItem = {}
		inputItem['w'] = w
		inputItem['n'] = n
		inputItem['l'] = l

		inputList.append(inputItem)

	print inputList

	return inputList

def recursion(w, s):
	global W, S, cache
	print "param : ", W, S, w, s

	if cache[w][s] != None:
		#print "cache"
		return cache[w][s]
	if w < len(W) and s < len(S) and (W[w] == '?' or W[w] == S[s]):
		#print "match"
		cache[w][s] = recursion(w+1, s+1)
		return cache[w][s]
	if w == len(W):
		#print "end"
		return s == len(S)
	if w < len(W) and W[w] == '*':
		#print "star"
		if recursion(w+1, s) or (s < len(S) and recursion(w, s+1)):
			cache[w][s] = True
			return cache[w][s]
	cache[w][s] = False
	#print "tail"
	return cache[w][s]

def solver(inputItem):
	global W, S, cache
	W = inputItem['w']
	n = inputItem['n']
	l = inputItem['l']
	matchList = []
	for item in l:
		S = item
		cache = [[None for j in range(len(S)+1)] for i in range(len(W)+1)]
		if recursion(0, 0):
			matchList.append(S)
		pprint.pprint(cache)
	matchList = sorted(matchList)
	return '\r\n'.join(matchList)

def merger(outputList):
	return '\r\n'.join(outputList) + '\r\n'

if __name__ == '__main__':
	p = Problem(inputFile='wildcard.in',
				outputFile='wildcard.out',
				parser=parser,
				solver=solver,
				merger=merger,
				parallel=1)
	p.run()

