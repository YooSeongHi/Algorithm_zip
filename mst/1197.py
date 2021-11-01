import sys
def find(i):
    if node[i] != i:
        node[i] = find(node[i])
    return node[i]
def union(nx,ny):
    if nx<ny:
        node[ny] = nx
    else:
        node[nx] = ny

if __name__ == '__main__':
    V, E = list(map(int, sys.stdin.readline().split()))
    bridge = []
    node = [i for i in range(V+1)]
    for _ in range(E):
        bridge.append(list(map(int, sys.stdin.readline().split())))
    bridge.sort(key=lambda x: x[2])

    answer = 0
    for s, e, w in bridge:
        nx = find(s)
        ny = find(e)
        if nx != ny:
            union(nx,ny)
            answer += w
    print(answer)