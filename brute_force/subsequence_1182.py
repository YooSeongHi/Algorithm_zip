import sys
#재귀 사용
n = 0
s = 0
result = 0
def solve(index, num, num_list):
    global n, s, result
    if index == s:
        if num == n:
            result += 1
        return
    solve(index+1, num+num_list[index], num_list)
    solve(index+1, num, num_list)
    

if __name__ == '__main__':
    s, n = list(map(int, sys.stdin.readline().split()))
    num_list = list(map(int, sys.stdin.readline().split()))
    solve(0, 0, num_list)
    if n == 0: #크기가 0인 부분집합에는 비어있는 부분수열이 포함되기 때문
        result -=1
    print(result)

#itertools 사용
from itertools import combinations
if __name__ == '__main__':
    s, n = list(map(int , sys.stdin.readline().split()))
    num_list = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(1, s+1):
        combin_list = list(combinations(num_list, i))
        for lis in combin_list:
            if n == sum(lis):
                result += 1
    print(result)