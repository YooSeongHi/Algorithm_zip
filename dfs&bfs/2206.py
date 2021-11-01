import sys
def bfs():
    queue = [[0,0]]
    x, y = [0, 0, -1, 1], [-1, 1, 0,0]
    
    while queue:
        cx, cy = queue.pop(0)
        for i in range(4):
            nx, ny = x[i]+cx, y[i]+cy
            if
if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    board = []
    for _ in range(N):
        board.append(sys.stdin.readline())

