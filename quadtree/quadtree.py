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
	return inputData.splitlines()[1:]

def recursion(s):
	global i
	c = s[i]
	i += 1
	if c == 'w' or c == 'b':
		return c
	ul = recursion(s)
	ur = recursion(s)
	ll = recursion(s)
	lr = recursion(s)
	return 'x' + ll + lr + ul + ur

def solver(inputItem):
	global i
	i = 0
	return recursion(inputItem)

def merger(outputList):
	return '\r\n'.join(outputList) + '\r\n'

if __name__ == '__main__':
	p = Problem(inputFile='quadtree.in',
				outputFile='quadtree.out',
				parser=parser,
				solver=solver,
				merger=merger,
				parallel=4)
	p.run()

