import sys

def findIce(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    ice = 0
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if nx < 0 or ny <0 or nx>=N or ny>=M:
            continue
        if node[nx][ny] <= 0 :
            ice += 1
    return ice
def bfs(x, y, check):
    queue = [(x,y)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    ice = findIce(x, y)
    ice_list = []
    ice_list.append([x,y,ice])
    check[x][y] = 1
    while queue:
        ix, iy = queue.pop(0)
        for i in range(4):
            nx = ix + dx[i]
            ny = iy + dy[i]
            if nx < 0 or ny <0 or nx>=M or ny>=M:
                continue
            if node[nx][ny] > 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append((nx,ny))
                ice = findIce(nx,ny)
                ice_list.append([nx,ny,ice])
    for l1, l2, l3 in ice_list:
        node[l1][l2] -= l3
if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    node = []
    clock = 0
    for _ in range(N):
        node.append(list(map(int, sys.stdin.readline().split())))
    
    while True:
        check = [[0]*M for _ in range(N)]
        num = 0
        
        for i in range(N):
            for j in range(M):
                if node[i][j] > 0 and check[i][j] == 0:
                    bfs(i, j, check) 
                    num += 1
                    if num >= 2 or num == 0:
                        break
        clock += 1
        if num == 0:
            print(0)
            break
        if num >= 2:
            print(clock-1)
            break

        

        
    

    