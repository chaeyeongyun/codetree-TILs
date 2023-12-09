import sys

MAX_INT = sys.maxsize

def in_range(x, y):
    global N
    return 0 <= x < N and 0 <= y < N

# def initialize():
#     global N, santa_pos, rudolf_pos, is_survive
#     # board 초기화
#     for i in range(N):
#         for j in range(N):
#             board[i][j] = 0
#     # 루돌프 마킹
#     board[rudolf_pos[0]][rudolf_pos[1]] = 0
#     # 산타 마킹
#     for p in santa_pos:
#         if not is_survive[p]:
#             continue
#         s_r, s_c = santa_pos[p]
#         board[s_r][s_c] = p
def get_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def rudolf_move():
    global N, P, C, D, santa_pos, rudolf_pos, is_survive, is_faint
    dxs = [-1, 0, 1, 0, -1, -1, 1, 1]
    dys = [0, 1, 0, -1, -1, 1, -1, 1]
    r_r, r_c = rudolf_pos
    # 산타들과의 거리 계산
    min_santa = 0
    min_dist = MAX_INT
    for p in range(1, P + 1):
        if not is_survive[p]:
            continue
        s_r, s_c = santa_pos[p]
        dist = get_distance(r_r, r_c, s_r, s_c)
        if dist < min_dist:
            min_dist = dist
            min_santa = p
        elif dist == min_dist:
            bef_s_r, bef_s_c = santa_pos[min_santa]
            if bef_s_r < s_r:
                min_santa = p
            elif bef_s_r == s_r:
                if bef_s_c < s_c:
                    min_santa = p
    s_r, s_c = santa_pos[min_santa]
    if s_r < r_r and s_c < r_c:
        direc = 4
    elif s_r < r_r and s_c > r_c:
        direc = 5
    elif s_r > r_r and s_c < r_c:
        direc = 6
    elif s_r > r_r and s_c > r_c:
        direc = 7
    elif s_r == r_r and s_c < r_c:
        direc = 3
    elif s_r == r_r and s_c > r_c:
        direc = 1
    elif s_r < r_r and s_c == r_c:
        direc = 0
    elif s_r > r_r and s_c == r_c:
        direc = 2
    r_r += dxs[direc]
    r_c += dys[direc]
    rudolf_pos[0], rudolf_pos[1] = r_r, r_c
    # 충돌했다면
    if s_r == r_r and s_c == r_c:
        boom_rudolf(min_santa, direc)

def boom_rudolf(santa, direction):
    global N, P, C, D, santa_pos, santa_score, rudolf_pos, is_survive, is_faint, turn, board
    dxs = [-1, 0, 1, 0, -1, -1, 1, 1]
    dys = [0, 1, 0, -1, -1, 1, -1, 1]
    santa_score[santa] += C
    santa_pos[santa][0] += dxs[direction] * C
    santa_pos[santa][1] += dys[direction] * C
    s_r, s_c = santa_pos[santa]
    if not in_range(s_r, s_c):
        is_survive[santa] = False
        return
    is_faint[santa] = turn
    # 연쇄충돌
    r, c = s_r, s_c
    moved = {santa}
    direc = direction
    while in_range(r, c):
        is_boom = False
        for p in range(1, P + 1):
            if not is_survive[p]:
                continue
            if p in moved:
                continue
            pr, pc = santa_pos[p]
            if pr == r and pc == c:
                r += dxs[direc]
                c += dys[direc]
                if in_range(r, c):
                    santa_pos[p][0], santa_pos[p][1] = r, c
                    moved.add(p)
                else:
                    is_survive[p] = False
                is_boom = True
                break
            if is_boom:
                break
        if not is_boom:
            break

def is_santa(r, c):
    """r행 c열에 다른 산타 있는지 체크"""
    global santa_pos, P
    for p in range(1, P + 1):
        pr, pc = santa_pos[p]
        if pr == r and pc == c:
            return True
    return False


def santa_move():
    global N, P, C, D, santa_pos, rudolf_pos, is_survive, is_faint, turn
    # 상우하좌 순
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    r_r, r_c = rudolf_pos
    for p in range(1, P + 1):
        if is_faint[p] in [turn, turn - 1] or not is_survive[p]:
            continue
        s_r, s_c = santa_pos[p]
        org_dist = get_distance(r_r, r_c, s_r, s_c)
        min_direc = -1
        min_dist = MAX_INT
        for d in range(4):
            new_s_r, new_s_c = s_r + dxs[d], s_c + dys[d]
            if not in_range(new_s_r, new_s_c):
                # 게임판 밖으로는 못감
                continue
            if is_santa(new_s_r, new_s_c):
                # 산타 있으면 못 감
                continue
            dist = get_distance(r_r, r_c, new_s_r, new_s_c)
            if dist < min_dist:
                min_dist = dist
                min_direc = d
        if min_dist < org_dist:
            # 가까워질 수 있는 경우만 이동
            s_r += dxs[min_direc]
            s_c += dys[min_direc]
            santa_pos[p][0], santa_pos[p][1] = s_r, s_c
            if s_r == r_r and s_c == r_c:
                # 루돌프와 충돌시
                boom_santa(p, min_direc)
    
def boom_santa(santa, direction):
    global N, P, C, D, santa_pos, santa_score, rudolf_pos, is_survive, is_faint, turn, board    
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    santa_score[santa] += D
    # 반대방향으로 튕김
    direc = (direction + 2) % 4
    santa_pos[santa][0] += dxs[direc] * D 
    santa_pos[santa][1] += dys[direc] * D
    s_r, s_c = santa_pos[santa]
    if not in_range(s_r, s_c):
        # 격자 밖으로 튕길 경우 죽음
        is_survive[santa] = False
    is_faint[santa] = turn
    # 연쇄충돌
    r, c = s_r, s_c
    moved = {santa}
    while in_range(r, c):
        is_boom = False
        for p in range(1, P + 1):
            if not is_survive[p]:
                continue
            if p in moved:
                continue
            pr, pc = santa_pos[p]
            if pr == r and pc == c:
                r += dxs[direc]
                c += dys[direc]
                if in_range(r, c):
                    santa_pos[p][0], santa_pos[p][1] = r, c
                    moved.add(p)
                else:
                    is_survive[p] = False
                is_boom = True
                break
            if is_boom:
                break
        if not is_boom:
            break
        
def end_score():
    global P, is_survive, santa_score
    for p in range(1, P + 1):
        if is_survive[p]:
            santa_score[p] += 1

def is_end():
    global is_survive
    if any(is_survive):
        return False
    return True

def print_info():
    print(turn, "turn")
    print("santa_pos")
    print(santa_pos)
    print("santa_score")
    print(santa_score)
    print("rudolf_pos")
    print(rudolf_pos)
    print("is_survive")
    print(is_survive)
    print("is_faint")
    print(is_faint)
    print("\n")


if __name__ == "__main__":
    N, M, P, C, D = map(int, input().rstrip().split(" "))
    # board에 santa 번호, rudolf 0로 저장
    # board = [[0] * n for _ in range(n)]
    # 산타위치
    santa_pos = dict()
    # 산타 점수
    santa_score = [0] * (P + 1)
    # 루돌프 위치
    rudolf_pos = [0, 0]
    # 산타 생존 여부
    is_survive = [True] * (P + 1)
    is_survive[0] = False
    # 산타 기절턴
    is_faint = [-1] * (P + 1)
    r_r, r_c = map(lambda x: int(x) - 1, input().rstrip().split(" "))
    rudolf_pos[0], rudolf_pos[1] = r_r, r_c
    for _ in range(P):
        p_n, s_r, s_c = map(int, input().rstrip().split(" "))
        s_r, s_c = s_r - 1, s_c - 1
        santa_pos[p_n] = [s_r, s_c]
    # 게임 시작
    for turn in range(1, M + 1):
        # initialize()
        rudolf_move()
        santa_move()
        if is_end():
            break
        end_score()
        # print_info()
    print(*santa_score[1:])