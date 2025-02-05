import os

def is_safe(board, row, col, n):
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
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    def backtrack(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0
                
    backtrack(0)
    return solutions

def print_solution(solution):
    for row in solution:
        print(' '.join('Q' if cell else '.' for cell in row))
    print()

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of queens (N): "))
        if n < 1:
            raise ValueError

        solutions = solve_nqueens(n)

        print(f"\nFound {len(solutions)} solutions for {n}-Queens problem:")
        for i, solution in enumerate(solutions, 1):
            print(f"Solution {i}:")
            print_solution(solution)

    except ValueError:
        print("Please enter a positive integer.")
