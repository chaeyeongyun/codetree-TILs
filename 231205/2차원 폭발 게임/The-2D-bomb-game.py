def rotate90():
    """90도 회전하기"""
    global n, grid
    next_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            next_grid[j][n - i - 1] = grid[i][j]
    grid = [y[:] for y in next_grid]

def bomb():
    """터지는 위치 0으로 채우기"""
    global n, m, grid
    next_grid = [[0] * n for _ in range(n)]
    if m == 1:
        # m은 1인 경우 값이 존재한다면 모두 폭발
        grid = [y[:] for y in next_grid]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    return True
        return False
    is_bomb = False
    for j in range(n):
        # 연속 개수 카운트
        cnt = 1
        for i in range(n):
            if grid[i][j]:
                # 빈 칸이 아닌 경우
                if i >= 1 and grid[i - 1][j] == grid[i][j]:
                    # 이전값과 연속이면
                    cnt += 1
                elif cnt >= m:
                    # 연속이 아니고 이전 연속값이 m개 이상이어서 터져야하는 경우
                    is_bomb = True
                    for c in range(1, cnt + 1):
                        next_grid[i - c][j] = 0
                    cnt = 1
                next_grid[i][j] = grid[i][j]
        # 마지막요소까지 연속값이라서 미처 터지지 못한 경우
        if cnt >= m:
            is_bomb = True
            for c in range(cnt):
                next_grid[n - c - 1][j] = 0
    grid = [y[:] for y in next_grid]
    return is_bomb

def drop():
    """중력 적용하기"""
    global n, m, grid
    next_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        next_idx = n - 1 # 바닥부터 채우기
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[next_idx][j] = grid[i][j]
                next_idx -= 1
    grid = [y[:] for y in next_grid]            

def count_bomb():
    """남은 폭탄 세기"""
    global n, grid
    cnt = 0
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if grid[i][j]:
               cnt += 1
    return cnt

if __name__ == "__main__":
    n, m, k = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    for _ in range(k):
        is_bomb = True
        while is_bomb:
            is_bomb = bomb()
            drop()
        rotate90()
        drop()
    is_bomb = True
    while is_bomb:
        is_bomb = bomb()
        drop()
    print(count_bomb())