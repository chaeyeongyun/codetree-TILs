def solution():
    global n, grid, r, c
    bomb_size = grid[r][c]
    temp_grid = [y[:] for y in grid]
    for i in range(r + 1):
        for j in range(max(0, c - bomb_size + 1), min(c + bomb_size - 1, n - 1) + 1):
            if j == c:
                continue
            if i == 0:
                grid[i][j] = 0
            else:
                grid[i][j] = temp_grid[i - 1][j]
    for i in range(min(n, r + bomb_size)):
        if i >= 2 * bomb_size - 1:
            grid[i][c] = grid[i - 2 * bomb_size + 1][c]
        else:
            grid[i][c] = 0
    for g in grid:
        print(*g)
    


if __name__ == "__main__":
    n = int(input().rstrip())
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    r, c = map(lambda x: int(x) - 1, input().rstrip().split(" "))
    solution()