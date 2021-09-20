import sys

def dfs(v):
    
    num.append(v)
    for i in range(1, computer+1):
        if node[v][i] == 1:
            node[v][i] = 0
            num.append(i)
            dfs(i)

if __name__ == '__main__':
    computer = int(sys.stdin.readline())
    network = int(sys.stdin.readline())
    node = [[0]*(computer+1) for _ in range(computer+1)]
    num = []
    for _ in range(network):
        x, y = list(map(int, sys.stdin.readline().split()))
        node[x][y] = node[y][x] = 1
    dfs(1)
    print(len(set((num)))-1)
    
    