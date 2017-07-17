import sys
import copy
import time
from SudokuClasses import Puzzle

node_count = 0
start_time = int(time.time()*1000)

def main():

	if len(sys.argv) is not 3:
		print "Usage: SudokuSolver.py puzzlefile.txt algorithm"

	with open(sys.argv[1], 'r') as txt:
		data = txt.read().replace(" ", "")

	if isValid(data) is False:
		print "Invalid puzzle or format"
		return 0

	sudoku = Puzzle(data)

	"Given a valid puzzle with duplicate values would result in infinite recursion."
	"So this test case must be eliminated"
	if sudoku.findDup() is True:
		prtout([None, 0])
		return 0

	emptyFields = getEmptyFields(sudoku)

	if sys.argv[2] == "BF":
		"Brute force algorithm"
		sol = BF(sudoku, emptyFields, int(time.time()*1000))
		prtout(sol)

	elif sys.argv[2] == "BT":
		"Backtracking algorithm"
		sudoku.updateInit()
		sol = BT(sudoku, emptyFields, int(time.time()*1000))
		prtout(sol)

	elif sys.argv[2] == "FC-MRV":
		"Forward checking algorithm"
		sudoku.genMRV(emptyFields)
		sol = FC(sudoku, emptyFields, int(time.time()*1000))
		prtout(sol)

	else:
		print "Invalid option. Usage: BF BT FC-MRV"

	return 0

def BF(puzzle, emptyFields, startTime):
	"""
	Brute force a puzzle by checking all possible permutations
	of 1-9 in each unfilled number
	"""

	if not emptyFields and puzzle.checkGoalState() is True:
		return [puzzle, int(time.time()*1000)-startTime]

	"Expand if unfilled values exists"
	if emptyFields:
		x = emptyFields[0][0]
		y = emptyFields[0][1]

		for val in range(1, 10):
			global node_count
			node_count += 1
			puzzle.puzzle[x][y] = val

			"Return solution if found"
			a = BF(puzzle, emptyFields[1:], startTime)
			if a[0]:
				return a

	"If reached, no solution exists for puzzle"
	return [None, int(time.time()*1000)-startTime]

def BT(puzzle, emptyFields, startTime):
	"""
	Test possible values for each unfilled value.  Backtracks (prunes)
	if constraint is violated where each field must have a valid value.
	"""

	if not emptyFields and puzzle.checkGoalState() is True:
		return [puzzle, int(time.time()*1000)-startTime]

	x = emptyFields[0][0]
	y = emptyFields[0][1]

	for val in puzzle.pValues[x][y]:
		global node_count
		node_count += 1

		"Prune if constraints of sudoku puzzle is violated"
		check = puzzle.check(emptyFields[0], val)
		if check is True:
			puzzle.puzzle[x][y] = val

			"Returns solution if found"
			a = BT(puzzle, emptyFields[1:], startTime)
			if a[0]:
				return a

		puzzle.puzzle[x][y] = 0

	return [None, int(time.time()*1000)-startTime]

def FC(puzzle, emptyFields, startTime):
	"""
	Test possible values for each unfilled value using a minimum remaining value
	heuristic.
	"""
	if puzzle.checkGoalState() is True:
		return [puzzle, int(time.time()*1000)-startTime]

	"Sort emptyFields where coordinates of empty fields with lowest min remaining"
	"are pushed to the front"
	sortedList = puzzle.genMRV(emptyFields)

	x = sortedList[0][0]
	y = sortedList[0][1]

	for val in puzzle.pValues[x][y]:
		global node_count
		node_count += 1

		"Prune if constraints of sudoku puzzle is violated"
		check = puzzle.check(sortedList[0], val)
		if check is True:
			puzzle.puzzle[x][y] = val

			"Returns solution if found"
			a = FC(puzzle, sortedList[1:], startTime)
			if a[0]:
				return a

		puzzle.puzzle[x][y] = 0

	return [None, int(time.time()*1000)-startTime]

def isValid(data):
	"Checks if puzzle is valid 9x9 containing single digits in each field"
	row=0
	col=0

	for x in data:
		if "\n" in x:
			"Check to see if it exceeds bounds"
			if col is not 9 or row > 9:
				return False
			else:
				row += 1
				col = 0
		else:
			"Check to see all characters are digits"
			if x.isdigit() is not True:
				return False
			else:
				col += 1

	"Ensure the last line does not exceed boundary"
	if col is not 9:
		return False

	return True

def getEmptyFields(puzzle):
	"Gets coordinates of all unfilled values"
	l = []
	for x in range(9):
		for y in range(9):
			if puzzle.puzzle[x][y] == 0:
				l.append([x, y])
	return l

def prtout(sol):
	"Prints out data pertaining to puzzle"

	"Output solution"
	if sol[0] is None:
		print "No solution found"
	else:
		print sol[0]

	running_time = int(time.time()*1000) - start_time
	T = "Total clock time: " + str(running_time)
	S = "Search clock time: " + str(sol[1])
	N = "Nodes explored: " + str(node_count)

	"Output preformance to screen"
	print T
	print S
	print N

	"Output solution and preformance to files"
	if sys.argv[1][:6] == "puzzle":
		if sol[0] is not None:
			solution = "solution" + sys.argv[1][-5:]
			f = open(solution, "w")
			print >>f, sol[0]
			f.close()

		preformance = "preformance" + sys.argv[1][-5:]
		f = open(preformance, "w")
		f.write(T+"\n"+S+"\n"+N)
		f.close()

	else:
		if sol[0] is not None:
			solution = "solution" + sys.argv[1][-5:]
			f = open(solution, "w")
			print >>f, sol[0]
			f.close()

		preformance = "preformance_" + sys.argv[1]
		f = open(preformance, "w")
		f.write(T+"\n"+S+"\n"+N)
		f.close()

	return 0

if __name__ == "__main__":
	main()