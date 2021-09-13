import sys
def dfs(V):
    visit_node[V] = True
    t = node[V]
    if not visit_node[t]:
        dfs(t)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    while T != 0:
        M = 0
        N = int(sys.stdin.readline())
        node = [0] + list(map(int, sys.stdin.readline().split()))
        visit_node = [True] + [False] * N
        for i in range(1, N+1):
            if not visit_node[i]:
                dfs(i)
                M += 1
        T -= 1
        print(M)
