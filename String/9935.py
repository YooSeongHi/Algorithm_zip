import sys
if __name__ == '__main__':
    str_list = sys.stdin.readline().rstrip()
    bom_str = list(sys.stdin.readline().rstrip())
    make_str = []
    for i in range(len(str_list)):
        make_str.append(str_list[i])
        if len(make_str) >= len(bom_str) and make_str[-1] == bom_str[-1]:
            if make_str[-len(bom_str):] == bom_str:
                for _ in range(len(bom_str)):
                    make_str.pop()
    if make_str:
        print(''.join(make_str))
    else:
        print("FRULA")


        