import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    if x== (N-1) and y == (M-1):
        return 1
    if visit[x][y] != -1:
        return visit[x][y]
    visit[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N  and 0 <= ny <M:
            if maps[nx][ny] < maps[x][y]:
                visit[x][y] += dfs(nx ,ny)
    return visit[x][y]
    


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    maps = []
 
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visit = [ [-1] * M for _ in range(N)]
    for _ in range(N):
        maps.append(list(map(int, sys.stdin.readline().split())))
    dfs(0 , 0)
    print(visit[0][0])
    