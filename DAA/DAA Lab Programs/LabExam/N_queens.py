# def isSafe(board, row, col, n):
    
#     # Check right side of the row
#     for i in range(col, n):
#         if board[row][i]:
#             return False
        
#     # Check upper right diagonal
#     i, j = row, col
#     while i >= 0 and j < n:
#         if board[i][j]:
#             return False
#         i -= 1
#         j += 1
        
#     # Check lower right diagonal
#     i, j = row, col
#     while i < n and j < n:
#         if board[i][j]:
#             return False
#         i += 1
#         j += 1

#     return True

# def nQueens(board, n, column):
#     if column == -1:
#         return True
    
#     for i in range(n):
#         if board[i][column] == 0:
#             if isSafe(board, i, column, n):
#                 board[i][column] = 1
#                 if nQueens(board, n, column - 1):
#                     return True
#                 board[i][column] = 0  
    
#     return False


# n = int(input("Enter the chess board dimension N: "))
# # Initialize the chess board
# board = [[0] * n for _ in range(n)]

# if nQueens(board, n, n -1):
#     for row in board:
#         print(row)
# else:
#     print("No solution found")


# To print all solutions

def isSafe(board, row, col, n):
    # Check right side of the row
    for i in range(col, n):
        if board[row][i]:
            return False
        
    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
        
    # Check lower right diagonal
    i, j = row, col
    while i < n and j < n:
        if board[i][j]:
            return False
        i += 1
        j += 1

    return True

def nQueens(board, n, column, solutions):
    if column == -1:
        solutions.append([row[:] for row in board])
        return
    
    for i in range(n):
        if board[i][column] == 0:
            if isSafe(board, i, column, n):
                board[i][column] = 1
                nQueens(board, n, column - 1, solutions)
                board[i][column] = 0

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


n = int(input("Enter the chess board dimension N: "))
board = [[0] * n for _ in range(n)]
solutions = []
nQueens(board, n, n - 1, solutions)

if solutions:
    print(f"Found {len(solutions)} solutions for {n}-Queens problem:")
    for solution in solutions:
        print_board(solution)
else:
    print("No solution found")
