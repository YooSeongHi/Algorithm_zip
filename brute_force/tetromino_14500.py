import sys
max_num = 0
N =0
M = 0
num_list = []
bool_list = []
dx = [0, 0, 1, -1] #위 아래 오른쪽 왼쪽
dy = [1, -1, 0, 0]
def solve(x, y, num, cnt):
    global max_num, N, M, num_list, bool_list
    if(cnt == 4):
        if num > max_num:
            max_num = num
        return

    if(x<0) or (x>=N) or (y<0) or (y>=M): #범위를 벗어낫을 경우
        return
    if bool_list[x][y]: #이미 방문했을 경우
        return
    bool_list[x][y] = True
    for i in range(4):
        solve(x+dx[i], y+ dy[i], num + num_list[x][y], cnt+1)
    bool_list[x][y] = False 
    


if __name__ == '__main__':
    N, M = map(int , sys.stdin.readline().split())
    num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(0, N)]
    bool_list = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            solve(i, j, 0, 0)
            #따로 처리해야하는 ㅗ모양의 블록 처리
            if j+2 < M:
                col = num_list[i][j] + num_list[i][j+1] + num_list[i][j+2]
                if i-1 >= 0:
                    ver = col + num_list[i-1][j+1]
                    if ver > max_num:
                        max_num = ver
                if i+1 < N:
                    ver = col + num_list[i+1][j+1]
                    if ver> max_num:
                        max_num = ver

            if i+2 < N:
                ver = num_list[i][j] + num_list[i+1][j] + num_list[i+2][j]
                if j-1 >= 0:
                    col = ver + num_list[i+1][j-1]
                    if col > max_num:
                        max_num= col
                    
                if j+1 < M:
                    col = ver + num_list[i+1][j+1]
                    if col > max_num:
                        max_num = col

    print(max_num)
