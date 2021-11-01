import sys
def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(x,y):
    if x<y:
        parent[y] = x
    else:
        parent[x] =y

def calculate(curr):
    min_num = 10000000000
    answer_x = 0
    answer_num = 0
    for x in range(curr+1, N):
        curr_num = min(abs(node[curr][0]-node[x][0]), abs(node[curr][1]-node[x][1]), abs(node[curr][2]-node[x][2]))
        if curr_num < min_num:
            min_num = curr_num
            answer_x = x
            answer_num = curr_num
    edge.append([curr, answer_x, answer_num])
   
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    node = []
    for _ in range(N):
        node.append(list(map(int, sys.stdin.readline().split())))
    parent = [i for i in range(N)]
    edge = []
    for i in range(N-1):
        calculate(i)
    edge.sort(key=lambda x: x[2])

    answer = 0
    for s, u, w in edge:
        nx = find(s)
        ny = find(u)
        if nx != ny:
            union(nx, ny)
            answer += w
    print(answer)
        
    
    
