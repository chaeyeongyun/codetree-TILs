from collections import deque

def in_range(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m

def bfs(i, j):
    global n, m, grid
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False] * m for _ in range(n)]
    grid[i][j] = 0
    q = deque([(i, j)])
    escape = False
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.append((nx, ny))
                if nx == (n - 1) and ny == (m - 1):
                    escape = True
        if escape:
            break
    return escape 


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    escape = bfs(0, 0)
    if escape:
        print(1)
    else:
        print(0)