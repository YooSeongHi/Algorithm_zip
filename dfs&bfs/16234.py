import sys
from collections import deque
def bfs(x, y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    count = 1
    score = maps[x][y]
    queue = deque()
    queue.append((x,y))
    temp = [[x,y]]
    visit[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+cx, dy[i]+cy
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0:
                val =abs(maps[cx][cy]-maps[nx][ny])
                if L<=val<=R:
                    queue.append((nx,ny))
                    visit[nx][ny] = 1
                    count += 1
                    score += maps[nx][ny]
                    temp.append([nx,ny])
    
    result = score //count
    if count > 1:
        global is_move
        is_move = True
        for i, j in temp:
            maps[i][j] = result
  



if __name__ == '__main__':
    N, L , R = list(map(int, sys.stdin.readline().split()))
    maps = []
    for _ in range(N):
        maps.append(list(map(int, sys.stdin.readline().split())))
    
    year = 0
    while True:
        is_move = False
        num = 1
        curr_list = []
        cal = [[0, 0]]
        visit = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if visit[x][y] == 0:
                    bfs(x, y)
        if is_move:
            year +=1
        else:
            break
    print(year)
       
        



    
  