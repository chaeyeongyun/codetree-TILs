def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def cnt_neighbor(i, j, grid):
    global dx, dy
    cnt = 0
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if in_range(nx, ny) and grid[nx][ny] > 0:
            cnt += 1
    return cnt

def grow():
    global n, k, c, grid, herbicide
    new_grid = [y[:] for y in grid]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt = cnt_neighbor(i, j, grid)
                new_grid[i][j] += cnt
    grid = [y[:] for y in new_grid]

def can_breed(x, y):
    global grid
    return in_range(x, y) and grid[x][y] == 0 and herbicide[x][y] == 0

def breed_tree(i, j, new_grid):
    global grid, herbicide, dx, dy
    directions = []
    cnt = 0
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if can_breed(nx, ny):
            cnt += 1
            directions.append(d)
    if cnt > 0:
        num_trees = grid[i][j] // cnt
        for d in directions:
            nx, ny = i + dx[d], j + dy[d]
            new_grid[nx][ny] += num_trees

def breeding():
    global n, k, c, grid, herbicide, dx, dy
    new_grid = [y[:] for y in grid]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                breed_tree(i, j, new_grid)
    grid = [y[:] for y in new_grid]

def try_control(i, j):
    """i행j열에 제초제 분사할 경우"""
    global n, k, c, grid, diag_dx, diag_dy
    cnt = grid[i][j]
    for d in range(4):
        for r in range(1, k + 1):
            nx, ny = i + diag_dx[d] * r, j + diag_dy[d] * r
            if in_range(nx, ny):
                if grid[nx][ny] > 0:
                    cnt += grid[nx][ny]
                else:
                    break
    return cnt

def get_max_control_idx():
    global n, grid
    diag_dx = [-1, -1, 1, 1]
    diag_dy = [-1, 1, -1, 1]
    max_cnt = -1
    max_idx = [-1, -1]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt = try_control(i, j)
            elif grid[i][j] == 0:
                cnt = 0
            if max_cnt < cnt:
                max_idx[0], max_idx[1] = i, j
                max_cnt = cnt
    return *max_idx, max_cnt

def remove_herbicide():
    global n, herbicide
    for i in range(n):
        for j in range(n):
            if herbicide[i][j] >= 1:
                herbicide[i][j] -= 1

def control():
    global n, k, c, grid, herbicide, diag_dx, diag_dy, answer
    remove_herbicide()
    x, y, cnt = get_max_control_idx()
    if cnt <= 0:
        # 빈칸 분사가 최선인 경우이므로 아무일이 일어나지 않는다
        return
    grid[x][y] = 0
    herbicide[x][y] = c
    answer += cnt
    for d in range(4):
        for r in range(1, k + 1):
            nx, ny = x + diag_dx[d] * r, y + diag_dy[d] * r
            if in_range(nx, ny):
                if grid[nx][ny] >= 0:
                    grid[nx][ny] = 0
                    herbicide[nx][ny] = c
                else:
                    break

def print_info():
    global grid, herbicide
    print("grid")
    for g in grid:
        print(*g)
    print("herbicide")
    for h in herbicide:
        print(*h)
    print("answer", answer)

if __name__ == "__main__":
    n, m, k, c = map(int, input().rstrip().split(" "))
    grid = [list(map(int, input().rstrip().split(" ")))for _ in range(n)]
    herbicide = [[0] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    diag_dx = [-1, -1, 1, 1]
    diag_dy = [-1, 1, -1, 1]
    answer = 0
    for year in range(m):
        grow()
        breeding()
        control()
        # print("year", year)
        # print_info()
    print(answer)