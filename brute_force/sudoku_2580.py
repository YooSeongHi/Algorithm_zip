import sys
board = []
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
block = [[False]*10 for _ in range(9)] 
#col과 row를 이용해서 사각형을 만들 수 있다. : (row/3)*3 + col/3
def block_num(row, col):
    return (row//3)*3 + (col//3)
def solve(loc):
    #row
    if loc == 81:
        for n in board:
            print(' '.join(map(str, n)))
        return
    x_loc = loc//9
    y_loc = loc%9
    bnum = block_num(x_loc, y_loc)
    if(board[x_loc][y_loc] != 0):
        solve(loc+1)
    else:
        for num in range (1, 10):
            if row[x_loc][num] == False and col[y_loc][num] == False and block[bnum][num] == False:
                board[x_loc][y_loc] = num
                row[x_loc][num] = True
                col[y_loc][num] = True
                block[bnum][num] = True
                if solve(loc+1):
                    return True
                board[x_loc][y_loc] = 0
                row[x_loc][num] = False 
                col[y_loc][num] = False 
                block[bnum][num] = False 
    return False

                 

if __name__ == '__main__':
    for _ in range(9):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(9):
        for j in range(9):
            if(board[i][j] != 0):
                row[i][board[i][j]] = True
                col[j][board[i][j]] = True
                block[block_num(i,j)][board[i][j]] = True
    solve(0)