# coding:utf-8

'''
greedy method example
'''

from multiprocessing import Pool
import pprint
import Queue

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
		n = int(lineList[idx])

		idx += 1
		l = lineList[idx].strip().split(' ')
		
		inputItem = {}
		inputItem['n'] = n
		inputItem['l'] = l

		inputList.append(inputItem)

	#print inputList

	return inputList

def solver(inputItem):
	n = inputItem['n']
	l = inputItem['l']

	q = Queue.PriorityQueue()
	ret = 0

	for item in l:
		q.put(int(item))

	while q.qsize() > 1:
		n1 = q.get()
		n2 = q.get()
		s = n1 + n2
		q.put(s)
		ret += s

	return str(ret)

def merger(outputList):
	return '\r\n'.join(outputList) + '\r\n'

if __name__ == '__main__':
	p = Problem(inputFile='strjoin.in',
				outputFile='strjoin.out',
				parser=parser,
				solver=solver,
				merger=merger,
				parallel=1)
	p.run()

