def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def dfs(i, j):
    global grid, cnt
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if in_range(nx, ny) and grid[nx][ny]:
            grid[nx][ny] = 0
            cnt += 1
            dfs(nx, ny)

if __name__ == "__main__":
    n = int(input().rstrip())
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    people_cnt = []
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                grid[i][j] = 0
                cnt = 1
                dfs(i, j)
                people_cnt.append(cnt)
    print(len(people_cnt))
    people_cnt.sort()
    for p in people_cnt:
        print(p)