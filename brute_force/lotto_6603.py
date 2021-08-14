import sys
#재귀 사용
def solve(test_case, index, lott):
    if(len(lott) == 6):
        print(' '.join(lott))
        return
    if(index == len(test_case)):
        return
    solve(test_case, index+1, lott + [test_case[index]])
    solve(test_case, index+1, lott)

if __name__ == '__main__':
    while True:
        n, *test_case = list( sys.stdin.readline().split())
        if(n == '0'):
            break
        solve(test_case, 0, [])   
        print()


#itertools 사용
# import sys
# from itertools import combinations

# if __name__ == '__main__':
#     while True:
#         test_case = list(sys.stdin.readline().split())
#         if(test_case[0] == '0'):
#             break
#         combin_list = list(combinations(test_case[1:], 6))
#         for com in combin_list:
#             print(' '.join(x for x in com))
#         print()
        

        

    