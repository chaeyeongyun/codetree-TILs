def down(row, col, block):
    # col열의 row행 이하 블럭들이 block만큼 내려가는 코드
    global grid
    for i in range(row, -1, -1):
        if i - block < 0:
            grid[i][col] = 0
        else:
            grid[i][col] = grid[i - block][col]

def solution():
    global n, grid, r, c
    bomb_size = grid[r][c]
    # 한 칸씩만 내려오면 되는 열
    for i in range(1, bomb_size):
        if c >= i:
            down(r, c - i, 1)
        if (c + i) < n:
            down(r, c + i, 1)
    # 여러칸 내려가야하는 중심 열
    down(min(r + bomb_size + 1, n - 1), c, 2 * bomb_size - 1)
    for g in grid:
        print(*g)
    


if __name__ == "__main__":
    n = int(input().rstrip())
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    r, c = map(lambda x: int(x) - 1, input().rstrip().split(" "))
    solution()