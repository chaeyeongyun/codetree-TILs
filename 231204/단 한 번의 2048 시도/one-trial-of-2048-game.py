def rotate90():
    global grid
    next_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            next_grid[j][3 - i] = grid[i][j]
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
        grid = rotate90()
        grid = down()
        for _ in range(3):
            grid = rotate90()
    elif direction == "L":
        for _ in range(3):
            grid = rotate90()
        grid = down()
        grid = rotate90()
    elif direction == "D":
        grid = down()
        
    elif direction == "U":
        for _ in range(2):
            grid = rotate90()
        grid = down()
        for _ in range(2):
            grid = rotate90()
    else:
        raise ValueError
    
    for g in grid:
        print(*g)

if __name__ == "__main__":
    grid = [list(map(int, input().rstrip().split(" "))) for _ in range(4)]
    direction = input().rstrip()
    solution()