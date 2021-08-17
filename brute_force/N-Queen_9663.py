import sys
check_col = []
check_digit1 = []
check_digit2 = []
board = []
N = 0
def check(row, col):
  
    if check_col[col]:
        return False
    if check_digit1[col+row]:
        return False
    if check_digit2[N+row-col-1]:
        return False
    return True

def solve(row):
    global N
    if row == N:
        return 1
    res = 0
    for col in range(N):
        if check(row, col):
            check_digit1[col+row] = True
            check_digit2[N+row-col-1] = True
            check_col[col] = True
            board[row][col] = True
            res += solve(row+1)
            board[row][col] = False
            check_digit1[col+row] = False
            check_digit2[N+row-col-1] = False
            check_col[col] = False

    return res
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    check_col = [False] * N
    check_digit1 = [False] * (N*2 -1)
    check_digit2= [False] * (N*2 -1)
    board = [[False]*N for _ in range(N)]
    print(check_col)
    print(check_digit2)
    print(board)
    print(solve(0))