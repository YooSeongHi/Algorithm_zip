import sys
def bfs(i, j):
    max_length = 0
    queue = [(i,j)]
    check = [[0]*M for _ in range(N)]
    check[i][j] = 1
    while queue:
        x,y = queue.pop(0)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx< N and 0<=ny< M and maps[nx][ny] =="L" and check[nx][ny] == 0:
                check[nx][ny] = check[x][y] +1
                queue.append((nx,ny))
                if check[nx][ny] > max_length:
                    max_length = check[nx][ny]
    return max_length
                
if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    maps = []
    max_list = 0
    for _ in range(N):
        maps.append(sys.stdin.readline())

    for i in range(N):
        for j in range(M):
            if maps[i][j] == "L":
                num = bfs(i,j)
                if num > max_list:
                    max_list = num
    print(max_list-1)
    
      