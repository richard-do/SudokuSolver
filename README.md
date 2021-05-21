### Requirements

Python v3 and beyond

### To run

Install Python through Windows Store

Run IDLE Python

File > Open > Find SudokuSolver.py on your system

Run > Run ... Customized (Or Shift + F5) which allows input of command line arguments

In the box that appears, input: target_puzzle.txt algorithm

eg. ./target_puzzle.txt BF

If the file is in the same folder, prefix with ./ otherwise provide absolute path to file.

Older versions of python may require fiddling with the location of each command line argument to get this to work.

### Algorithms

BF = Brute Force

FC-MRV = Forward Checking (Minimum remaining values)

BT = Backtrack

### Formatting target_puzzle

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
