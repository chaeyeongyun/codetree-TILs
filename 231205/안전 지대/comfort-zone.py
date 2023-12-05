import sys
sys.setrecursionlimit(10**10)

def flood(k):
    """k이하 높이 아파트 0으로 만들기"""
    global n, m, grid
    new_grid = [y[:] for y in grid]
    for i in range(n):
        for j in range(m):
            if new_grid[i][j] <= k:
                new_grid[i][j] = 0
    return new_grid

def in_range(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m

def count_section(k):
    """안전영역수 세기"""
    global n, m
    new_grid = flood(k)
    def dfs(i, j):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if in_range(nx, ny) and new_grid[nx][ny] > 0:
                new_grid[nx][ny] = 0
                dfs(nx, ny)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_grid[i][j] > 0:
                new_grid[i][j] = 0
                dfs(i, j)
                cnt += 1
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    answer = 0
    answer_k = 1
    for k in range(1, 101):
        cnt = count_section(k)
        if answer < cnt:
            answer_k = k
            answer = cnt
    print(f"{answer_k} {answer}")