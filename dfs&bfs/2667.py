import sys
def bfs (x, y, N, num, en_graph):
    queue =[ (x, y)]
    en_graph[x][y] = num
    dx = [0, 0, -1 ,1]
    dy = [-1, 1, 0, 0]
    homes = 1
    while queue:
        ix , iy = queue.pop(0)
        for z in range(4):
            nx = ix + dx[z]
            ny = iy + dy[z]
            if (nx < 0 )  or (ny <0) or (nx>= N) or (ny>= N):
                continue
            if graph[nx][ny] == '1' and en_graph[nx][ny] == 0:
                en_graph[nx][ny] = num
                queue.append([nx, ny])
                homes += 1
    return homes

def find_home():
    en_graph = [[0]*N for _ in range(N)]
    num = 1
    answer = []
  
    for i in range (N):
        for j in range (N):
            if en_graph[i][j] != 0:
                continue
            if graph[i][j] == "1":
                answer.append(bfs(i,j, N, num, en_graph))
                num += 1
    answer.sort()
    print(num-1)
    for an in answer:
        print(an)
           

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = []
    for _ in range(N):
        graph.append(sys.stdin.readline())
    find_home()

