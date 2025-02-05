'''
N-Queens solver using backtracking. Finds all valid solutions for N non-attacking queens on an
NxN board.

Features:
- Backtracking algorithm with conflict checks
- Validates positive integer input
- Prints solutions in chessboard format (Q/.)
- Returns solution count and board states

Time complexity: O(N!) 
'''

def is_safe(board, row, col, _n):
    '''
    This function checks if the current layout of the board has any constraint violations 
    i.e it checks if any queen is attacking another queen.
    '''
    # Check row and diagonals for conflicts
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < _n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_nqueens(_n):
    '''
    This function implements a nested backtracking function that places a queen on a
    certain position and then checks if the board is safe. If it is safe then the function
    will place the next queen on the next spot in the backtracking tree. If all possible
    placement slots are exhausted then the function will bakctrack to the previous 
    queens position and chanfe it.
    '''
    board = [[0] * _n for _ in range(_n)]
    solutions = []
    def backtrack(col):
        if col == _n:
            solutions.append([row[:] for row in board])
            return
        for row in range(_n):
            if is_safe(board, row, col, _n):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0
    backtrack(0)
    return solutions

def print_solution(solution):
    '''
    If a solution to the problem is found then it is printed to the terminal
    '''
    for row in solution:
        print(' '.join('Q' if cell else '.' for cell in row))
    print()

if __name__ == "__main__":
    try:
        _n = int(input("Enter the number of queens (N): "))
        if _n < 1:
            raise ValueError

        answers = solve_nqueens(_n)

        print(f"\nFound {len(answers)} solutions for {_n}-Queens problem:")
        for case, board_layout in enumerate(answers, 1):
            print(f"Solution {case}:")
            print_solution(board_layout)

    except ValueError:
        print("Please enter a positive integer.")
