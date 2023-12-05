from collections import deque

def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def bfs(r, c):
    global n, k, grid, cnt
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()
        cnt += 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                q.append((nx, ny))

if __name__ == "__main__":
    n, k = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    start_points = [tuple(map(lambda x: int(x) - 1, input().rstrip().split(" "))) for _ in range(k)]
    cnt = 0
    for r, c in start_points:
        if grid[r][c] == 0:
            grid[r][c] = 1
            bfs(r, c)
    print(cnt)