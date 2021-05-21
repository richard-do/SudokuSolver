### Requirements

Python v3 and beyond

### To run

Install Python through Windows Store

Run IDLE Python

Open SudokuSolver.py

Shift + F5 for customized run (to allow command line arguments)

In the box that appears, input: target_puzzle.txt algorithm

eg. ./target_puzzle.txt BF

If the file is in the same folder, prefix with ./puzzle_file.txt otherwise provide absolute path to file.

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
