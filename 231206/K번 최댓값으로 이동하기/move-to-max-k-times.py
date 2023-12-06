from collections import deque

def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def bfs(r, c):
    global n, k, nums
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False] * n for _ in range(n)]
    q = deque([(r, c)])
    visited[r][c] = True
    num = nums[r][c]
    max_num = 0
    max_x, max_y = r, c
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and nums[nx][ny] < num and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                if nums[nx][ny] > max_num:
                    max_num = nums[nx][ny]
                    max_x, max_y = nx, ny
                elif nums[nx][ny] == max_num:
                    max_x, max_y = sorted([(max_x, max_y), (nx, ny)])[0]
    return max_num, max_x, max_y

        



if __name__ == "__main__":
    n, k = map(int, input().rstrip().split(" "))
    nums = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    r, c = map(lambda x: int(x) - 1, input().rstrip().split(" "))
    max_x, max_y = r, c
    for _ in range(k):
        max_num, max_x, max_y = bfs(max_x, max_y)
        # print("max_num", max_num, "max_x", max_x, "max_y", max_y)
        if max_num == 0:
            break
    print(f"{max_x + 1} {max_y + 1}")