from collections import deque

def in_range(r, c, h, w):
    global l
    return 0 <= r < l and 0 <= c < l and 0 <= (r + h - 1) < l and 0 <= (c + w - 1) < l

def is_wall(r, c, h, w):
    global l, chess
    for i in range(r, r + h):
        for j in range(c, c + w):
            if chess[i][j] == 2:
                return True
    return False

def is_push(i_r, i_c, i_h, i_w, target, d):
    global l, n, position, size
    t_r, t_c = position[target]
    t_h, t_w = size[target]
    if d == 0:
        # 위쪽
        if (t_r + t_h) == i_r:
            if i_c <= t_c <= (i_c + i_w - 1) or i_c <= (t_c + t_w - 1) <= (i_c + i_w - 1):
                return True
            if t_c < i_c and (i_c + i_w - 1) < (t_c + t_w - 1):
                return True
    if d == 1:
        # 오른쪽
        if t_c == i_c + i_w:
            if i_r <= t_r <= (i_r + i_h - 1) or i_r <= (t_r + t_h - 1) <= (i_r + i_h - 1):
                return True
            if t_r < i_r and (i_r + i_h - 1) < (t_r + t_h - 1):
                return True
    if d == 2:
        # 아래쪽
        if t_r == (i_r + i_h):
            if i_c <= t_c <= (i_c + i_w - 1) or i_c <= (t_c + t_w - 1) <= (i_c + i_w - 1):
                return True
            if t_c < i_c and (i_c + i_w - 1) < (t_c + t_w - 1):
                return True
    if d == 3:
        # 왼쪽
        if (t_c + t_w) == i_c:
            if i_r <= t_r <= (i_r + i_h - 1) or i_r <= (t_r + t_h - 1) <= (i_r + i_h - 1):
                return True
            if t_r < i_r and (i_r + i_h - 1) < (t_r + t_h - 1):
                return True
    return False

def damage(i):
    global l, n, chess, survive, position, size, stamina
    r, c = position[i]
    h, w = size[i]
    dam = 0
    for x in range(r, r + h):
        for y in range(c, c + w):
            if chess[x][y] == 1:
                dam += 1
    stamina[i] -= dam
    if stamina[i] <= 0:
        survive[i] = False

def down(i):
    global l, n, chess, survive, position, size, stamina
    moved_list = [i]
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque([i])
    while q:
        knight = q.popleft()
        knight_r, knight_c = position[knight]
        knight_stamina = stamina[knight]
        knight_h, knight_w = size[knight]
        nxt_k_r, nxt_k_c = knight_r + 1, knight_c
        if not in_range(nxt_k_r, nxt_k_c, knight_h, knight_w) or is_wall(nxt_k_r, nxt_k_c, knight_h, knight_w):
            return
        for t in range(1, n + 1):
            if not visited[t] and survive[t] and is_push(knight_r, knight_c, knight_h, knight_w, t, 2):
                q.append(t)
                visited[t] = True
                moved_list.append(t)
    # while문이 끝났다면 움직임이 가능한 것
    for m in moved_list:
        mr, mc = position[m]
        # 현 위치 바꿔주기
        position[m] = (mr + 1, mc)
        #데미지 주기
        if m != i:
            damage(m)

def up(i):
    global l, n, chess, survive, position, size, stamina
    moved_list = [i]
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque([i])
    while q:
        knight = q.popleft()
        knight_r, knight_c = position[knight]
        knight_stamina = stamina[knight]
        knight_h, knight_w = size[knight]
        nxt_k_r, nxt_k_c = knight_r - 1, knight_c
        if not in_range(nxt_k_r, nxt_k_c, knight_h, knight_w) or is_wall(nxt_k_r, nxt_k_c, knight_h, knight_w):
            return
        for t in range(1, n + 1):
            if not visited[t] and survive[t] and is_push(knight_r, knight_c, knight_h, knight_w, t, 0):
                q.append(t)
                visited[t] = True
                moved_list.append(t)
    # while문이 끝났다면 움직임이 가능한 것
    for m in moved_list:
        mr, mc = position[m]
        # 현 위치 바꿔주기
        position[m] = (mr - 1, mc)
        #데미지 주기
        if m != i:
            damage(m)

def right(i):
    global l, n, chess, survive, position, size, stamina
    moved_list = [i]
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque([i])
    while q:
        knight = q.popleft()
        knight_r, knight_c = position[knight]
        knight_stamina = stamina[knight]
        knight_h, knight_w = size[knight]
        nxt_k_r, nxt_k_c = knight_r, knight_c + 1
        if not in_range(nxt_k_r, nxt_k_c, knight_h, knight_w) or is_wall(nxt_k_r, nxt_k_c, knight_h, knight_w):
            return
        for t in range(1, n + 1):
            if not visited[t] and survive[t] and is_push(knight_r, knight_c, knight_h, knight_w, t, 1):
                q.append(t)
                visited[t] = True
                moved_list.append(t)
    # while문이 끝났다면 움직임이 가능한 것
    for m in moved_list:
        mr, mc = position[m]
        # 현 위치 바꿔주기
        position[m] = (mr, mc + 1)
        #데미지 주기
        if m != i:
            damage(m)

def left(i):
    global l, n, chess, survive, position, size, stamina
    moved_list = [i]
    visited = [False] * (n + 1)
    visited[i] = True
    q = deque([i])
    while q:
        knight = q.popleft()
        knight_r, knight_c = position[knight]
        knight_stamina = stamina[knight]
        knight_h, knight_w = size[knight]
        nxt_k_r, nxt_k_c = knight_r, knight_c - 1
        if not in_range(nxt_k_r, nxt_k_c, knight_h, knight_w) or is_wall(nxt_k_r, nxt_k_c, knight_h, knight_w):
            return
        for t in range(1, n + 1):
            if not visited[t] and survive[t] and is_push(knight_r, knight_c, knight_h, knight_w, t, 3):
                q.append(t)
                visited[t] = True
                moved_list.append(t)
    # while문이 끝났다면 움직임이 가능한 것
    for m in moved_list:
        mr, mc = position[m]
        # 현 위치 바꿔주기
        position[m] = (mr, mc - 1)
        #데미지 주기
        if m != i:
            damage(m)

def move(i, d):
    """
    i : 움직일 기사 번호
    d : 방향 (0:위쪽, 1:오른쪽, 2:아래쪽, 3:왼쪽)
    """
    global l, n, chess, survive, position, size, stamina
    if d == 0:
        up(i)
    if d == 1:
        right(i)
    if d == 2:
        down(i)
    if d == 3:
        left(i)
    
    
    # print_info()

def print_info():
    global l, n, chess, survive, position, size, stamina
    print("survive")
    print(survive)
    print("position")
    print(position)
    print("stamina")
    print(stamina)

if __name__ == "__main__":
    l, n, q = map(int, input().rstrip().split(" "))
    chess = [list(map(int, input().rstrip().split(" "))) for _ in range(l)]
    survive = dict()
    position = dict()
    size = dict()
    stamina = dict()
    init_stamina = dict()
    for i in range(1, n + 1):
        r, c, h, w, k = map(int, input().rstrip().split(" "))
        survive[i] = True
        position[i] = (r - 1, c - 1)
        size[i] = (h, w)
        stamina[i] = k
        init_stamina[i] = k
    for _ in range(q):
        i, d = map(int, input().rstrip().split(" "))
        if survive[i]:
            move(i, d)
    answer = 0
    for t in range(1, n + 1):
        if survive[t]:
            answer += (init_stamina[t] - stamina[t])
    print(answer)