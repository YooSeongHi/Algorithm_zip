import sys
#kruscal 알고리즘
def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(u, v):
    i = find(u)
    j = find(v)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j

if __name__ =='__main__':
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = []
    for _ in range(M):
        graph.append(list(map(int, sys.stdin.readline().split())))
    graph.sort(key=lambda x: x[2])
    mst_cost = 0
    mst_num = 0
    parent = [i for i in range(N+1)]
    for u, v, t in graph:
        if find(u) != find(v):
            union(u,v)
            mst_cost += t
            mst_num +=1

    print(mst_cost)
