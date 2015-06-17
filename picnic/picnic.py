# coding:utf-8

from multiprocessing import Pool

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

	t = int(lineList[0])

	for i in range(t):
		inputItem = {}

		[n, m] = map(int, lineList[1+i*2].split(' '))
		#print "n : %d, m : %d" % (n, m)

		l = []
		a = map(int, lineList[2+i*2].split(' '))
		for j in range(m):
			l.append( tuple(sorted(a[j*2:j*2+2])) )
		l = sorted(l)
		#print "l : ", l
		
		inputItem['n'] = n
		inputItem['m'] = m
		inputItem['l'] = l

		inputList.append(inputItem)

	return inputList

def recursion(inputList, pairs, selected=[]):
	#print "param : ", inputList, pairs, selected
	if pairs == 0: return 1
	cnt = 0
	for (i, inputItem) in enumerate(inputList):
		if (inputItem[0] not in selected) and (inputItem[1] not in selected):
			cnt += recursion(inputList[i+1:], pairs-1, selected+[inputItem[0]]+[inputItem[1]])
	return cnt

def solver(inputItem):
	n = inputItem['n']
	m = inputItem['m']
	l = inputItem['l']
	cnt = recursion(inputList=l, pairs=n/2)
	return str(cnt)

def merger(outputList):
	return '\r\n'.join(outputList) + '\r\n'

if __name__ == '__main__':
	p = Problem(inputFile='picnic.in',
				outputFile='picnic.out',
				parser=parser,
				solver=solver,
				merger=merger,
				parallel=4)
	p.run()

