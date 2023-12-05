# 뱀없고
# 방문하지 않았고 (이걸 처리하지 않으면 시간 초과됨)
# 범위 안에 있어야함
def in_range(nx, ny):
    global n, m
    return 0 <= nx < n and 0 <= ny < m

def dfs(i, j):
    global n, m, answer, visited, grid
    if i == n - 1 and j == m - 1:
        answer = True
        return
    if answer:
        return
    # 오른쪽 혹은 아래쪽만 이동 가능
    dx = [0, 1]
    dy = [1, 0]
    for k in range(2):
        nx, ny = i + dx[k], j + dy[k]
        if in_range(nx, ny) and grid[nx][ny] == 1:
            grid[nx][ny] = 0
            dfs(nx, ny)

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    answer = False
    grid[0][0] = 0
    dfs(0, 0)
    if answer:
        print(1)
    else:
        print(0)