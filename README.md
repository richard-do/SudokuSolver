## To run

CSLinux:

python SudokuSolver.py target_puzzle.txt Algorithm

eg. python SudokuSolver.py puzzle1.txt BF

python SudokuSolver.py puzzle2.txt FC-MRV

python SudokuSolver.py puzzle3.txt BT

BF = Brute Force

FC-MRV = Forward Checking (Minimum remaining values)

BT = Backtrack

- .txt may not be needed for filename

- may need to replace python with path if environmental variable is not set up

- may not work on versions below python 2.0

## Formatting target_puzzle

0 0 0 0 0 8 0 4 0

0 9 0 6 0 0 8 0 3

0 0 0 1 5 0 0 0 0

2 0 0 7 3 0 0 6 0

4 0 6 0 1 0 0 7 0

0 0 0 0 0 0 0 0 0

7 0 5 0 0 1 0 0 0

8 0 0 0 0 0 0 0 0

9 6 3 8 0 0 5 0 0

Zeroes represent blank spaces.
