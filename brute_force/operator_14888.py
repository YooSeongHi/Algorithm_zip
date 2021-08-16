import sys
from itertools import permutations

def calc(num_list, index, curr, plus, minus, mul, div):
    if index == len(num_list):
        return (curr, curr)
    res = []    
    if plus > 0:
        res.append(calc(num_list, index + 1, curr + num_list[index], plus-1, minus, mul, div))
    
    if minus > 0:
        res.append(calc(num_list, index +1, curr - num_list[index], plus, minus-1, mul, div))
    
    if mul > 0:
        res.append(calc(num_list, index+1, curr * num_list[index], plus, minus, mul-1, div))   
    
    if div> 0:
        if curr < 0:
            res.append(calc(num_list, index+1, -(-curr//num_list[index]), plus, minus, mul, div-1))
        else:
            res.append(calc(num_list, index+1, curr // num_list[index], plus, minus, mul, div-1))
    ans = (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )
    return ans

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    op_list = list(map(int, sys.stdin.readline().split()))
    result = calc(num_list, 1, num_list[0], op_list[0], op_list[1], op_list[2], op_list[3])
    print(result[0])
    print(result[1])
 
   