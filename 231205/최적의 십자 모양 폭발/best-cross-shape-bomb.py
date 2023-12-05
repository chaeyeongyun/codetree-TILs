def count_pairs(grid):
    """값 같은 쌍 세기"""
    global n
    cnt = 0
    # 상->하, 좌->우 탐색하므로 오른쪽 요소, 아래 요소와만 비교
    for i in range(n):
        for j in range(n):
            if not grid[i][j]:
                continue
            if j <= (n - 2) and grid[i][j] == grid[i][j + 1]:
                cnt += 1
            if i <= (n - 2) and grid[i][j] == grid[i + 1][j]:
                cnt += 1
    return cnt

# def bomb_pairs(i, j, init_cnt):
#     global n, grid
#     cnt = init_cnt
#     bomb_range = grid[i][j] - 1
#     for c in range(max(0, j - bomb_range), min(n, j + bomb_range + 1)):
#         # 상, 하, 우에 기존 쌍 있는지 확인
#         # 새로 붙는 쌍이 동일 쌍인지 확인
#         if c == j:
#             continue
#         if i >= 1 and i <= (n - 2) and grid[i - 1][c] == grid[i + 1]:
#             cnt += 1
#         if i >= 1 and grid[i][c] == grid[i - 1][c]:
#             cnt -= 1
#         if i <= (n - 1) and grid[i][c] == grid[i + 1][c]:
#             cnt -= 1
#         if c <= (n - 2) and grid[i][c] == grid[i][c + 1]:
#             cnt -= 1
#         if c == (j - bomb_range) and c >= 1 and grid[i][c - 1] == grid[i][c]:
#             # 영향 받는 첫 열이면서 좌에 비교할 블럭이 있을 때
#             cnt -= 1

    
#     for r in range(max(0, i - bomb_range), min(n, i + bomb_range + 1)):
#         # 상, 좌, 우 기존 쌍 확인
#         # 새로 붙는 쌍이 동일 쌍인지 확인
#         if 1 <= j and r != i and grid[r][j - 1] == grid[r][j]:    
#             # 위에서 i, j위치의 좌와는 확인이 되므로 여기서는 패스
#             cnt -= 1
#         if j <= (n - 2) and grid[r][j + 1] == grid[r][j]:
#             cnt -= 1
#         if r >= 1 and grid[r - 1][j] == grid[r][j]:
#             cnt -= 1
#         if r == (i + bomb_range) and r < (n - 2) and grid[r + 1][j] == grid[r][j]:
#             # 마지막행에 도달했고, 밑에 비교할 블럭이 또 있을 때
#             cnt -= 1
    
#     if 0 <= (i - bomb_range - 1) < n and 0 <= i + bomb_range + 1 < n and grid[i - bomb_range - 1] == grid[i + bomb_range + 1]:
#         # j열에서 새로 붙는 블럭이 있을 때
#         cnt += 1
#     return cnt

def bomb_pairs(i, j):
    global grid, n
    bomb_range = grid[i][j] - 1
    temp_grid = [y[:] for y in grid]
    for r in range(max(0, i - bomb_range), min(n, i + bomb_range + 1)):
        temp_grid[r][j] = 0
    for c in range(max(0, j - bomb_range), min(n, j + bomb_range + 1)):
        temp_grid[i][c] = 0
    next_grid = drop(temp_grid)
    return count_pairs(next_grid)
            
def drop(temp_grid):
    global n
    next_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        next_idx = n - 1
        for i in range(n - 1, -1, -1):
            if temp_grid[i][j]:
                next_grid[next_idx][j] = temp_grid[i][j]
                next_idx -= 1
    return next_grid

        
            

def solution():
    global n, grid
    # init_cnt = count_pairs()
    answer = 0
    for i in range(n):
        for j in range(n):
            new_cnt = bomb_pairs(i, j)
            answer = max(answer, new_cnt)
    return answer

if __name__ == "__main__":
    n = int(input().rstrip())
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    print(solution())