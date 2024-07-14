#N QUEENS
print ("Enter the number of queens")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n,ind):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if i==0 and j in ind :
              continue
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1 , ind)==True:
                    return True
                board[i][j] = 0

    return False
ind =[]
while True:

  if N_queen(N,ind):
    for i in board:
      print (i)
    for i in range(N):
      if board[0][i] == 1:
        ind.append(i)
    board = [[0]*N for _ in range(N)]
    print()
  else:
    break



def isSafe(arr, row, col, n):
   
    for i in range(col, n):
        if arr[row][i]:
            return False
  
    i, j = row, col
    while i >= 0 and j < n:
        if arr[i][j]:
            return False
        i -= 1
        j += 1

    i, j = row, col
    while i < n and j < n:
        if arr[i][j]:
            return False
        i += 1
        j += 1

    return True

def nQueens(arr, n, column):
    if column == -1:
        return True
    
    for i in range(n):
        if arr[i][column] == 0:
            if isSafe(arr, i, column, n):
                arr[i][column] = 1
                if nQueens(arr, n, column - 1):
                    return True
                arr[i][column] = 0  
    
    return False

n = 4 
arr = [[0] * n for _ in range(n)]

if nQueens(arr, n, n -1):
    for row in arr:
        print(row)
else:
    print("No solution found")
