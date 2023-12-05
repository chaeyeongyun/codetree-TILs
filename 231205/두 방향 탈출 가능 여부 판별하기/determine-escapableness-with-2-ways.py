# 뱀없고
# 방문하지 않았고 -> 오른쪽 혹은 아래로만 가니깐 이럴일이 없을거같은디..
# 범위 안에 있어야함
def in_range(nx, ny):
    global n
    return 0 <= nx < n and 0 <= ny < n

def dfs(i, j):
    global n, answer
    if i == n - 1 and j == n - 1:
        answer = True
        return
    # 오른쪽 혹은 아래쪽만 이동 가능
    dx = [0, 1]
    dy = [1, 0]
    for k in range(2):
        nx, ny = i + dx[k], j + dy[k]
        if in_range(nx, ny) and grid[nx][ny] == 1:
            dfs(nx, ny)

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    answer = False
    dfs(0, 0)
    if answer:
        print(1)
    else:
        print(0)