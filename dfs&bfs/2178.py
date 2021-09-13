#BFS문제
import sys
def bfs():
    queue = [[0,0]]
    board[0][0] = 1
    #상하좌우
    dx = [0,0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        i, j = queue.pop(0)
        for v in range(4):
            nx = i + dx[v]
            ny = j + dy[v]
            if(nx <0 or ny< 0 or nx>=n or ny>m):
                continue
            if(board[nx][ny] == '1'):
                queue.append([nx,ny])
                board[nx][ny] = board[i][j] + 1
    

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(n):
        board.append(list(sys.stdin.readline()))
    bfs()
    print(board[n-1][m-1])
