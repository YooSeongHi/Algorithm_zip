import sys
import copy
def isAllIce(): #전체 노드가 0인지 확인
    for i in range(N):
        for j in range(M):
            if node[i][j] != 0:
                return False
    return True
def findIce(x,y): #상하좌우로 0이 몇개인지 확인
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    num = 0
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0 <= nx < N and 0<= ny< M and ice[nx][ny] == 0 :
            num +=1
    return num
def bfs(x, y):
    queue = [(x,y)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    check = [[0]*M for _ in range(N)]
    check[x][y] = 1
    while queue:
        ix, iy = queue.pop(0)
        for i in range(4):
            nx = ix + dx[i]
            ny = iy + dy[i]
            if nx < 0 or ny <0 or nx>=M or ny>=M:
                continue
            if land[nx][ny] != 0 and check[nx][ny] == 0:
                land[nx][ny] = 0
                check[nx][ny] = 1
                queue.append((nx,ny))
 
if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    node = []
    year = 1
    for _ in range(N):
        node.append(list(map(int, sys.stdin.readline().split())))
    while True:
        if isAllIce():
            print(0)
            break
        #ice : 이미 녹은 얼음에 영향을 주면 안되기 때문에 값을 저장
        ice = copy.deepcopy(node)
        for i in range(N):
            for j in range(M):
                if ice[i][j] != 0 :
                    num = findIce(i,j)
                    node[i][j] = max(ice[i][j] - num, 0)
        land = copy.deepcopy(node)
        for i in range(N):
            for j in range(M):
                if land[i][j] != 0 :
                    land[i][j] = 0
                    bfs(i, j)
                    year += 1
        if year > 1:
            print(year)
            break
        year += 1

        

        
    

    