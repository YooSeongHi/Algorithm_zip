import sys
def bfs(x, y, color, colors, check):
    queue = [(x,y)]
    check[x][y] = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        ix, iy = queue.pop(0)
        for i in range(4):
            nx = ix + dx[i]
            ny = iy + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if colors[nx][ny] == color and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append([nx,ny])


                


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    colors = []
    en_colors = []
    check_colors = [[0]*N for _ in range(N)]
    check_en_colors = [[0]*N for _ in range(N)]
    for _ in range(N):
        color_str = sys.stdin.readline()
        colors.append(color_str)
        en_colors.append(color_str.replace('R', 'G'))
    color_num = 0
    no_color_num = 0
    for i in range(N):
        for j in range(N):
            if check_colors[i][j] == 0:
                bfs(i, j, colors[i][j], colors, check_colors)
                color_num += 1
             
            if check_en_colors[i][j] == 0:
                bfs(i, j, en_colors[i][j], en_colors, check_en_colors)
                no_color_num += 1
    print(color_num, end=" ")
    print(no_color_num)
    