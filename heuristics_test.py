from eightpuzzle import *

def heuristic1_test(state):
    puzzle = EightPuzzleState(state)
    print(f"Heuristic 1\nresult = {puzzle.h1(puzzle)}\nExpected Value = 8\n")

def heuristic2_test(state):
    puzzle = EightPuzzleState(state)
    print(f"Heuristic 2\nresult = {puzzle.h2(puzzle)}\nExpected Value = 14.53\n")

def heuristic3_test(state):
    puzzle = EightPuzzleState(state)
    print(f"Heuristic 3\nresult = {puzzle.h3(puzzle)}\nExpected Value = 18\n")

def heuristic4_test(state):
    puzzle = EightPuzzleState(state)
    print(f"Heuristic 4\nresult = {puzzle.h4(puzzle)}\nExpected Value = 13\n")





if __name__ == '__main__':
    test_puzzle = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    heuristic1_test(test_puzzle)
    heuristic2_test(test_puzzle)
    heuristic3_test(test_puzzle)
    heuristic4_test(test_puzzle)