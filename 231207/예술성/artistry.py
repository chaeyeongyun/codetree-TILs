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
    global n, paint, group, group_cnt, group_start, group_ns
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
    group_ns = group_num - 1

# def pair_scoring(a_group, b_group):
#     """두 그룹 간의 조화로움 점수 계산"""
#     global n, paint, group, group_cnt, group_start
#     dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
#     score = group_cnt[a_group] + group_cnt[b_group]
#     score *= paint[group_start[a_group][0]][group_start[a_group][1]]
#     score *= paint[group_start[b_group][0]][group_start[b_group][1]]
#     meet_num = 0
#     visited = [[False] * n for _ in range(n)]
#     visited[group_start[a_group][0]][group_start[a_group][1]] = True
#     q = deque([tuple(group_start[a_group])])
#     while q:
#         x, y = q.popleft()
#         for d in range(4):
#             nx, ny = x + dx[d], y + dy[d]
#             if in_range(nx, ny) and not visited[nx][ny]:
#                 if group[nx][ny] == a_group:
#                     q.append((nx, ny))
#                     visited[nx][ny] = True
#                 if group[nx][ny] == b_group:
#                     meet_num += 1
#     score *= meet_num
#     return score

# def scoring():
#     """예술 점수 계산"""
#     global n, paint, group, group_cnt, group_start, group_ns
#     sum_score = 0
#     # 각 쌍의 조화로움 계산
#     for i in range(1, group_ns + 1):
#         for j in range(i + 1, group_ns + 1):
#             score = pair_scoring(i, j)
#             sum_score += score
#     return sum_score

def scoring():
    global n, paint, group, group_cnt, group_start, group_ns
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    # 특정 변을 경계로 하는 칸이 그룹이 다르다면 (a그룹칸수 + b그룹칸수) * a숫자 * b숫자만큼 더해준다
    # 곱하기의 특성을 활용한 것
    score = 0
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if in_range(nx, ny) and paint[i][j] != paint[nx][ny]:
                    a_group, b_group = group[i][j], group[nx][ny]
                    score += (group_cnt[a_group] + group_cnt[b_group]) * paint[i][j] * paint[nx][ny]
    return score // 2 # 중복이 생기므로 나누어줌
                    
def rotate():
    global n, paint
    # 십자모양 반시계90 회전
    new_paint = [[0] * n for _ in range(n)]
    c = (n - 1) // 2
    for i in range(n):
        new_paint[c][i] = paint[i][c]
        new_paint[n - 1 - i][c] = paint[c][i]
    # 정사각형들 시계 90 회전
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
    group_ns = 0
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