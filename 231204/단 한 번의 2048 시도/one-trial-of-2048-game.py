def right():
    global grid
    next_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        next_idx = 3
        for j in range(3, -1, -1):
            if grid[i][j]:
                for k in range(j - 1, -1, -1):
                    if grid[i][k]:
                        break
                if j >= 1 and grid[i][k] == grid[i][j]:
                    grid[i][j], grid[i][k] = 2 * grid[i][j], 0
                next_grid[i][next_idx] = grid[i][j]
                next_idx -= 1
    return next_grid

def left():
    global grid
    next_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        next_idx = 0
        for j in range(4):
            if grid[i][j]:
                for k in range(j + 1, 4):
                    if grid[i][k]:
                        break
                if j <= 2 and grid[i][k] == grid[i][j]:
                    grid[i][j], grid[i][k] = 2 * grid[i][j], 0
                next_grid[i][next_idx] = grid[i][j]
                next_idx += 1
    return next_grid

def up():
    global grid
    next_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        next_idx = 0
        for i in range(4):
            if grid[i][j]:
                for k in range(i + 1, 4):
                    if grid[k][j]:
                        break
                if i <= 2 and grid[k][j] == grid[i][j]:
                    grid[i][j], grid[k][j] = 2 * grid[i][j], 0
                next_grid[next_idx][j] = grid[i][j]
                next_idx += 1
    return next_grid

def down():
    global grid
    next_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        next_idx = 3
        for i in range(3, -1, -1):
            if grid[i][j]:
                for k in range(i - 1, -1, -1):
                    if grid[k][j]:
                        break
                if i >= 1 and grid[k][j] == grid[i][j]:
                    grid[i][j], grid[k][j] = 2 * grid[i][j], 0
                next_grid[next_idx][j] = grid[i][j]
                next_idx -= 1
                # if i >= 1 and grid[i - 1][j] == grid[i][j]:
                #     grid[i][j], grid[i - 1][j] = 2 * grid[i][j], 0
                # next_grid[next_idx][j] = grid[i][j]
                # next_idx -= 1
    return next_grid

def solution():
    global grid, direction
    if direction == "R":
        next_grid = right()
    elif direction == "L":
        next_grid = left()
    elif direction == "D":
        next_grid = down()
    elif direction == "U":
        next_grid = up()
    else:
        raise ValueError
    for g in next_grid:
        print(*g)

if __name__ == "__main__":
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(4)]
    direction = input().rstrip()
    solution()