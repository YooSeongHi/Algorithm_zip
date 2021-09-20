import sys
def find(k):
    if k != parent[k]:
        parent[k] = find(parent[k])
    return parent[k]
def union(u, v):
    r1 = find(u)
    r2 = find(v)
    if r1<r2:
        parent[r2] = r1
    else:
        parent[r1] = r2

if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    graph = []
    for _ in range(M):
        a, b, c = list(map(int, sys.stdin.readline().split()))
        graph.append([c,a,b])
    graph.sort()
    parent = [i for i in range(N+1)]

    mst_cost = 0
    mst_len = 0
    mst = []
    selected = []  # 선택된 간선
    answer = 0
    for c, a, b in graph:
        if find(a) != find(b):
            union(a, b)
            answer += c
            selected.append(c)

    # 마을을 두개로 분리하기 위해서 마지막 간선 제거
    answer -= selected.pop()

    # 출력
    print(answer)