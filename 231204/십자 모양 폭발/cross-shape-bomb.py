def solution():
    global n, grid, r, c
    bomb_size = grid[r][c]
    next_grid = [[0] * n for _ in range(n)]
    # 터질 위치 0으로 채우기
    for j in range(max(0, c - bomb_size + 1), min(n, c + bomb_size)):
        grid[r][j] = 0
    for i in range(max(0, r - bomb_size + 1), min(n, r + bomb_size)):
        grid[i][c] = 0
    
    # 터진 곳에 값 채우기
    for j in range(n):
        target_row = n - 1 # 맨 아래칸부터 확인
        for i in range(n - 1, -1, -1):
            if grid[i][j]: # grid에 0이 아닌 값이 있으면 그 값을 맨 아래칸부터 채우게된다.
                next_grid[target_row][j] = grid[i][j]
                target_row -= 1
    
    for g in next_grid:
        print(*g)

if __name__ == "__main__":
    n = int(input().rstrip())
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    r, c = map(lambda x: int(x) - 1, input().rstrip().split(" "))
    solution()