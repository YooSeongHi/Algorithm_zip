import sys
from collections import deque
def makeFunction(func_list, num, nums):
    reval = False
    revers = False
    if num < nums.count('D'):
        print("error")
    else:
        for fun in func_list:
            if fun == 'R':
                if revers:
                    revers = False
                else:
                    revers = True
            else:
                if(len(nums) == 0):
                    reval = True
                    break
                else:
                    if revers:
                        nums.pop()
                    else:
                        nums.popleft()
        if reval:
            print("error")
        else:
            if revers:
                print("["+",".join(reversed(nums))+"]")
            else:
                print("[" + ",".join(nums) + "]")

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
    
        func = sys.stdin.readline().rstrip()
        num = int(sys.stdin.readline())
        input_list = sys.stdin.readline()[1:-2].split(',')
        if  num == 0:
            input_list = []
      
        makeFunction(func, num, deque(input_list))
