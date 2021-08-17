import sys
def solve(energy):
    if len(energy) == 2:
        return 0
    max_num = 0
    for i in range(1, len(energy)-1):
        ans = energy[i-1] * energy[i+1]
        pips = energy[:i] + energy[i+1:]
        res = solve(pips)
        if(max_num < ans + res):
            max_num = ans+ res
    return max_num
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    energy = list(map(int, sys.stdin.readline().split()))
    print(solve( energy))