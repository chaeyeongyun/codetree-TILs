from collections import deque
def in_range(x, y):
    """좌표 (x, y)가 n x n 배열의 유효한 좌표인지 확인"""
    global n
    return 0 <= x < n and 0 <= y < n

def initialize():
    """그룹 관련 배열 및 dictionary 초기화"""
    global group, group_cnt, group_start
    group = [[0] * n for _ in range(n)]
    group_cnt.clear()
    group_start.clear()

def dfs(i, j, visited, group_num):
    """grouping 위한 dfs함수"""
    global n, paint, group, group_cnt
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]
        if in_range(nx, ny) and not visited[nx][ny] and paint[nx][ny] == paint[i][j]:
            visited[nx][ny] = True
            group_cnt[group_num] += 1
            group[nx][ny] = group_num
            dfs(nx, ny, visited, group_num)

def grouping():
    """그림 내 그룹 분류"""
    global n, paint, group, group_cnt, group_start
    visited = [[False] * n for _ in range(n)]
    group_num = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True
            group_start[group_num] = (i, j)
            group_cnt[group_num] = 1
            group[i][j] = group_num
            dfs(i, j, visited, group_num)
            group_num += 1

def pair_scoring(a_group, b_group):
    """두 그룹 간의 조화로움 점수 계산"""
    global n, paint, group, group_cnt, group_start
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    score = group_cnt[a_group] + group_cnt[b_group]
    score *= paint[group_start[a_group][0]][group_start[a_group][1]]
    score *= paint[group_start[b_group][0]][group_start[b_group][1]]
    meet_num = 0
    visited = [[False] * n for _ in range(n)]
    visited[group_start[a_group][0]][group_start[a_group][1]] = True
    q = deque([tuple(group_start[a_group])])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and not visited[nx][ny]:
                if group[nx][ny] == a_group:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                if group[nx][ny] == b_group:
                    meet_num += 1
    score *= meet_num
    return score

def scoring():
    """예술 점수 계산"""
    global n, paint, group, group_cnt, group_start
    group_nums = list(group_cnt.keys())
    sum_score = 0
    # 각 쌍의 조화로움 계산
    for i in range(len(group_nums)):
        for j in range(i + 1, len(group_nums)):
            score = pair_scoring(group_nums[i], group_nums[j])
            sum_score += score
    return sum_score

# def cross_rotate():
#     """십자모양 반시계90 회전"""
#     global n, paint
#     new_paint = [[0] * n for _ in range(n)]
#     c = (n - 1) // 2
#     for i in range(n):
#         new_paint[n - 1 - c][i] = paint[i][c]
#         new_paint[n - 1 - i][c] = paint[c][i]
#     for i in range(n):
#         paint[i][c] = new_paint[i][c]
#         paint[c][i] = new_paint[c][i]

# def square_rotate():
#     """정사각형들 시계 90 회전"""
#     global n, paint
#     new_paint = [[0] * n for _ in range(n)]
#     c = (n - 1) // 2
#     for i in range(n):
#         for j in range(n):
#             if i == c or j == c:
#                 continue
#             new_paint[j][c - 1 - i] = paint[i][j]


def rotate():
    global n, paint
    #십자모양 반시계90 회전
    new_paint = [[0] * n for _ in range(n)]
    c = (n - 1) // 2
    for i in range(n):
        new_paint[n - 1 - c][i] = paint[i][c]
        new_paint[n - 1 - i][c] = paint[c][i]
    # c x c 격자에 대한 회전으로 구현하고 각 정사각형의 좌상단 좌표만큼 밀어준다
    for i in range(c):
        for j in range(c):
            x1s = [0, 0, c + 1, c + 1]
            y1s = [0, c + 1, 0, c + 1]
            for d in range(4):
                new_paint[j + x1s[d]][c - 1 - i + y1s[d]] = paint[i + x1s[d]][j + y1s[d]]
    paint = [y[:] for y in new_paint]

def print_info():
    global n, paint, group, group_cnt, group_start
    print("paint")
    for p in paint:
        print(*p)
    print("\n")
    print("group")
    for g in group:
        print(*g)
    print("\n")
    print("group_cnt")
    print(group_cnt)
    print("group_start")
    print(group_start)

if __name__ == "__main__":
    n = int(input().rstrip())
    paint = [list(map(int, input().rstrip().split(" "))) for _ in range(n)]
    group = [[0] * n for _ in range(n)]
    group_cnt = dict()
    group_start = dict()
    answer = 0
    for k in range(4):
        initialize()
        grouping()
        score = scoring()
        answer += score
        if k < 3:
            rotate()
    print(answer)
    # initialize()
    # grouping()
    # score = scoring()
    # answer += score
    # rotate()