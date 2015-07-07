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

def rotateBlock(block):
	height = len(block)
	width = len(block[0])
	newBlock = [[0 for i in range(height)] for j in range(width)]
	for i in range(height):
		for j in range(width):
			newBlock[j][height-i-1] = block[i][j]
	return newBlock

def removeDupBlocks(blocks):
	blockStringList = []
	for block in blocks:
		blockStringList.append(str(block))
	blockStringList = list(set(blockStringList))
	newBlocks = map(eval, blockStringList)
	return newBlocks

def calcRelativePos(blocks):
	for i in range(len(blocks)):
		x = -1
		y = -1
		for h in range(len(blocks[i])):
			for w in range(len(blocks[i][h])):
				if blocks[i][h][w] == 1:
					if x == -1:
						x = w
						y = h
					blocks[i][h][w] = (h-y, w-x)
	return blocks

def removeWhiteSpace(blocks):
	newBlocks = []
	for block in blocks:
		newBlock = []
		for row in block:
			newBlock +=  filter(lambda x: x != 0, row)
		newBlocks.append(newBlock)
	return newBlocks

def createBlocks(block):
	blocks = []
	blocks.append(block)
	for i in range(3):
		block = rotateBlock(block)
		blocks.append(block)
	blocks = removeDupBlocks(blocks)
	blocks = calcRelativePos(blocks)
	blocks = removeWhiteSpace(blocks)
	return blocks

def parser(inputData):
	inputList = []

	lineList = inputData.splitlines()
	#print lineList

	idx = 0
	t = int(lineList[idx])

	for i in range(t):
		idx += 1
		[h, w, r, c] = map(int, lineList[idx].split(' '))

		board = [[0 for i in range(w)] for j in range(h)]
		for j in range(h):
			idx += 1
			line = lineList[idx].strip()
			for k in range(w):
				if line[k] == '#':
					board[j][k] = 1
		
		block = [[0 for i in range(c)] for j in range(r)]
		for j in range(r):
			idx += 1
			line = lineList[idx].strip()
			for k in range(c):
				if line[k] == '#':
					block[j][k] = 1

		inputItem = {}
		inputItem['h'] = h
		inputItem['w'] = w
		inputItem['r'] = r
		inputItem['c'] = c
		inputItem['board'] = board
		blocks = createBlocks(block)
		inputItem['blocks'] = blocks
		inputItem['limit'] = sum([x.count(0) for x in board]) / len(blocks[0])
		inputList.append(inputItem)

	pprint.pprint(inputList)

	return inputList

def setBlock(y, x, block, delta):
	global board

	#print "setBlock param : ", y, x, block, delta
	#pprint.pprint(board)
	ret = True
	height = len(board)
	width = len(board[0])
	for black in block:
		rY = y + black[0]
		rX = x + black[1]
		if rY >= 0 and rY < height and rX >= 0 and rX < width:
			if board[rY][rX] > 0:
				ret = False
			board[rY][rX] += delta
		else:
			ret = False
	#pprint.pprint(board)
	return ret

def recursion(placed):
	global h, w, r, c, board, blocks, best, limit

	#print "recursion param : ", placed, board

	x = -1
	y = -1
	for i in range(h):
		for j in range(w):
			#print "idx", i, j
			if board[i][j] == 0:
				y = i
				x = j
				#print "find", i, j
				break
		if x != -1:
			break
	
	if x == -1:
		best = max(best, placed)
		return

	for i in range(len(blocks)):
		if setBlock(y, x, blocks[i], 1):
			#print "success", board
			recursion(placed+1)
		setBlock(y, x, blocks[i], -1)
		#print "next", board
	
	board[y][x] = 1
	recursion(placed)
	board[y][x] = 0

def solver(inputItem):
	global h, w, r, c, board, blocks, best, limit

	h = inputItem['h']
	w = inputItem['w']
	r = inputItem['r']
	c = inputItem['c']
	board = inputItem['board']
	blocks = inputItem['blocks']
	limit = inputItem['limit']
	best = 0
	recursion(0)
	return str(best)

def merger(outputList):
	return '\r\n'.join(outputList) + '\r\n'

if __name__ == '__main__':
	p = Problem(inputFile='boardcover2.in',
				outputFile='boardcover2.out',
				parser=parser,
				solver=solver,
				merger=merger,
				parallel=1)
	p.run()

