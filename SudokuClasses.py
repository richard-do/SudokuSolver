import copy
import operator

class Puzzle:

	def __init__(self, data=None, sPuzzle=None, spValues=None):
		if sPuzzle is None:
			self.puzzle = [[0 for y in range(9)] for x in range(9)]
			self.pValues = [[0 for y in range(9)] for x in range(9)]
			self.populate(data)
		else:
			self.puzzle = sPuzzle
			self.pValues = spValues

	def populate(self, data):
		"Extracts data into puzzle and pValues"
		row = 0
		col = 0

		for x in data:
			if "\n" in x:
				row = 0
				col += 1
			else:
				self.puzzle[row][col] = int(x)

				if int(x) != 0:
					self.pValues[row][col] = []
				else:
					self.pValues[row][col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

				row += 1

	def getVals(self, x, y):
		"Gets values the field at x,y can take on"
		num = [1,2,3,4,5,6,7,8,9]

		for col in range(9):
			if self.puzzle[col][y] in num:
				num.remove(self.puzzle[col][y])

		for row in range(9):
			if self.puzzle[x][row] in num:
				num.remove(self.puzzle[x][row])

		moveX = x%3
		moveY = y%3

		"Checks 3x3 for duplicate values.  Use mod 3 to put column and row"
		"into the correct starting points."
		for i in range(3):
			for j in range(3):
				if self.puzzle[i+(x-moveX)][j+(y-moveY)] in num:
					num.remove(self.puzzle[i+(x-moveX)][j+(y-moveY)])
		return len(num)

	def genMRV(self, emptyFields):
		"Generated a sorted list of unfilled values based on MRV"
		unsortedList = copy.deepcopy(emptyFields)
		sortedList, updatedList = [], []
		for c in emptyFields:
			x = c[0]
			y = c[1]
			sortedList.append([[x,y], self.getVals(x, y)])

		sortedList.sort(key=lambda x:x[1])

		for c in sortedList:
			updatedList.append(c[0])

		return updatedList

	def findDup(self):
		"Check to see if any duplicate values exist within the puzzle"
		valCol = []
		valRow = []

		"Check each column and row for duplicate values"
		for x in range(9):
			for y in range(9):
				if ((self.puzzle[x][y] is not 0 and self.puzzle[y][x] is not 0) and
					(self.puzzle[x][y] in valCol or self.puzzle[y][x] in valRow)):
					return True
				else:
					valCol.append(self.puzzle[x][y])
					valRow.append(self.puzzle[y][x])
			valCol, valRow = [], []

		vals = []
		x, y = 0, 0
		"Check each 3x3 box for duplicate values"
		for box in range(9):
			for col in range(3):
				for row in range(3):
					if (self.puzzle[col+(x*3)][row+(x*3)] in vals and
						self.puzzle[col+(x*3)][row+(x*3)] is not 0):
						return True
					else:
						vals.append(self.puzzle[col+(x*3)][row+(x*3)])

			"Checks left to right, up to down"
			if x != 2:
				x += 1
			else:
				x = 0
				y += 1
			vals = []
		
		return False

	def check(self, coords, val):
		"Checks if the input value is not a duplicate of another"
		"within the same row, column, and 3x3."
		x = coords[0]
		y = coords[1]

		"Check columns and rows."
		for j in range(9):
			if val == self.puzzle[x][j] or val == self.puzzle[j][y]:
				return False

		"Put x, y into the correct starting positions in the 3x3."
		moveX = x%3
		moveY = y%3

		for i in range(3):
			for j in range(3):
				if val == self.puzzle[i+(x-moveX)][j+(y-moveY)]:
					return False

		return True

	def updateInit(self):
		"Update possible answers for each field in initial puzzle state."
		for col in range(9):
			for row in range(9):
				self.update(col, row)

		return 0

	def update(self, x, y):
		"Update possible answers for each field relative to number at xy."
		num = self.puzzle[x][y]

		"Empty pValues if at x, y there is a non-zero value"
		if num != 0:
			self.pValues[x][y] = []

		for col in range(9):
			if num in self.pValues[col][y]:
				self.pValues[col][y].remove(num)

		for row in range(9):
			if num in self.pValues[x][row]:
				self.pValues[x][row].remove(num)

		moveX = x%3
		moveY = y%3

		"Checks 3x3 for duplicate values.  Use mod 3 to put column and row"
		"into the correct starting points."
		for i in range(3):
			for j in range(3):
				if num in self.pValues[i+(x-moveX)][j+(y-moveY)]:
					self.pValues[i+(x-moveX)][j+(y-moveY)].remove(num)
		return 0

	def checkGoalState(self):
		"Returns True if goal state was met."
		valCol = []
		valRow = []

		"Check to see if any duplicate values exist in columns, row, or"
		"if any unfilled values exist."
		for x in range(9):
			for y in range(9):
				if (self.puzzle[x][y] in valCol or
				self.puzzle[y][x] in valRow or
				self.puzzle[x][y] is 0):
					return False
				else:
					valCol.append(self.puzzle[x][y])
					valRow.append(self.puzzle[y][x])
			valCol, valRow = [], []

		vals = []
		x, y = 0, 0
		"Check each 3x3 box for duplicate values"
		for box in range(9):
			for col in range(3):
				for row in range(3):
					if self.puzzle[col+(x*3)][row+(x*3)] in vals:
						return False
					else:
						vals.append(self.puzzle[col+(x*3)][row+(x*3)])

			"Checks left to right, up to down"
			if x != 2:
				x += 1
			else:
				x = 0
				y += 1
			vals = []
		
		return True

	def __str__(self):
		"Prints out current state of Sudoku puzzle"
		out = [[str(self.puzzle[x][y])[0]+str(" ") for x in range(9)] for y in range(9)]
		return '\n'.join([''.join(x) for x in out])


if __name__ == "__main__":
	main()