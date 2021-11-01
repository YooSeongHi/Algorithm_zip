import sys
def find(i):
    if node[i] != i:
        node[i] = find(node[i])
    return node[i]

def union(s, e):
    ns = find(s)
    ne = find(e)
    if ns<ne:
        node[ne] = ns
    else:
        node[ns] = ne
if __name__ == '__main__':

    while True:
        n, m = list(map(int, sys.stdin.readline().split()))
        if n == 0 and m == 0:
            break
        edge = []
        for _ in range(m):
            edge.append(list(map(int, sys.stdin.readline().split())))
        node = [i for i in range(n)]
        edge.sort(key= lambda x:x[2])
        answer = 0
        for s, e, w in edge:
            
            if find(s) != find(e):
                union(s,e)
            else:
                answer += w
        print(answer)


