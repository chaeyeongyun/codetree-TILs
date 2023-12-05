def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def dfs(i, j, target):
    global n, grid, cnt
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if in_range(nx, ny) and grid[nx][ny] == target:
            grid[nx][ny] = 0
            cnt += 1
            dfs(nx, ny, target)

if __name__ == "__main__":
    n = int(input().rstrip())
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    max_block = 0
    boom_block = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt = 1
                target = grid[i][j]
                grid[i][j] = 0
                dfs(i, j, target)
                max_block = max(cnt, max_block)
                if cnt >= 4:
                    boom_block += 1
    print("%d %d"%(boom_block, max_block))