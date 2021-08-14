import sys
#재귀 사용
check_list = []
S = []
N = 0
def solve(index, num):
    if index == N:
        check_list[num] = True
        return
    solve(index+1, num+S[index])
    solve(index+1, num)

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    S = list(map(int, sys.stdin.readline().split()))
    check_list = [False] * (sum(S)+2)
    solve(0, 0)
    for val, i in enumerate(check_list):
        if i == False:
            print(val)
            break
    
#itertools 사용
from itertools import combinations
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    S = list(map(int, sys.stdin.readline().split()))
    max_num = sum(S)
    combin_list = [0]*(max_num+1)
    
    for i in range(1, N+1):
        nums = list(combinations(S, i))
        for num in nums:
            combin_list[sum(num)] = 1
    answer = 0
    for num in range(1, max_num):
        if combin_list[num] == 0:
            answer = num
            break
    if answer == 0:
        print(max_num+1)
    else:
        print(answer)

   