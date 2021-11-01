import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        book_num = int(sys.stdin.readline())
        book = []
        for _ in range(book_num):
            book.append(sys.stdin.readline().rstrip())
        book.sort()
        check = False
        for i in range(book_num-1):
            if book[i+1].startswith(book[i]):
                check = True
                break
        if check:
            print("NO")
        else:
            print("YES")
        