def fill_zero(row, col):
    global grid, n
    bomb_size = grid[row][col] - 1
    for i in range(max(0, row - bomb_size), min(n, row + bomb_size + 1)):
        grid[i][col] = 0
    for j in range(max(0, col - bomb_size), min(n, col + bomb_size + 1)):
        grid[row][j] = 0

def bomb(col):
    global grid, n
    next_grid = [[0] * n for _ in range(n)]
    # 폭탄이 터질 행 구하기
    row = -1
    for i in range(n):
        if grid[i][col] != 0:
            row = i
            break
    if row == -1:
        # 해당 열에 터질 폭탄이 없음
        return
    # 폭탄 터지는 반경
    bomb_size = grid[row][col] - 1
    # 터진 곳 0으로 채우기
    fill_zero(row, col)
    # 영향을 받은 열들에 중력 가하기
    for j in range(n):
        next_idx = n - 1 # 바닥부터 채워줘야 함
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                next_grid[next_idx][j] = grid[i][j]
                next_idx -= 1 # 채워줬으니 다음 인덱스로 이동
    grid = [y[:] for y in next_grid]

if __name__ == "__main__":
    # n = 격자 크기, m = 떨어질 횟수
    n, m = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    cols = [int(input().rstrip()) - 1 for _ in range(m)]
    for col in cols:
        bomb(col)
    for g in grid:
        print(*g)