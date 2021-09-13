import sys

def dfs(v):
    visit_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if(visit_dfs[i] == 0 and node[v][i] == 1):
            dfs(i)
def bfs(v):
    queue = [v]
    visit_bfs[v] = 1
   
    while queue:
        v = queue.pop(0)
        print(v, end= ' ')
        for i in range(1, n+1):
            if(visit_bfs[i] == 0 and node[v][i] == 1):
                queue.append(i)
                visit_bfs[i] = 1

if __name__ == "__main__":
    n, m , v = map(int, sys.stdin.readline().split())
    node = [[0]*(n+1) for _ in range(0, n+1)]
    visit_dfs = [0] * (n+1)
    visit_bfs = [0] * (n+1)

    for _ in range(0, m):
        i, j = map(int,sys.stdin.readline().split())
        node[i][j] = node[j][i] = 1
    
    dfs(v)    
    print()
    bfs(v)
    

    