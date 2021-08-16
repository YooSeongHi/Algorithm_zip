import sys
N = 0
M = 0
board = []
dx = [0 ,0, 1, -1] #위 아래 오른쪽 왼쪽
dy = [1, -1, 0, 0]
def solve(cnt, nx, ny, mx, my):
    global N, M, min_num
    if cnt > 10:
        return -1
    one_fall = False
    two_fall = False
    if (nx < 0 or nx>=N or ny<0 or ny>=M):
        one_fall = True
    if (mx<0 or mx >= N or my<0 or my >= M):
        two_fall = True
    
    if one_fall and two_fall:
        return -1
    if one_fall or two_fall:
        return cnt
    num = -1
    for i in range(4):
        nx1, ny1= nx + dx[i], ny + dy[i]
        mx1, my1 = mx + dx[i], my + dy[i]

        if (0<= nx1 < N and 0<= ny1 < M) and board[nx1][ny1] == '#':
            nx1, ny1 = nx, ny
        if (0<= mx1 < N and 0<= my1 < M) and board[mx1][my1] == '#':
            mx1, my1 = mx, my
        point = solve(cnt + 1, nx1, ny1, mx1, my1)
        if point == -1:
            continue
        #최소가 없거나(최초로 최소 값을 설정) 최소가 현재 값보다 클때 
        if num == -1 or num > point:
            num = point
    return num

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline()) for _ in range (N)]
    nx= ny=mx= my = -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                if nx == -1:
                    nx, ny = i, j
                else:
                    mx, my = i, j
                board[i][j] = '.' #다음 코인을 검색하기 위해서 초기화
    print(solve(0, nx, ny, mx, my))
   

