from heapq import heappop, heappush

def initialize():
    global positions, weights, directions, pred_boom
    positions.clear()
    weights.clear()
    directions.clear()
    pred_boom.clear()

def solution():
    global n, positions, weights, directions, dx, dy, pred_boom, last_boom
    survive_marble = set([i for i in range(1, n + 1)])
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            ix, iy = positions[i]
            jx, jy = positions[j]
            idx, idy = dx[directions[i]], dy[directions[i]]
            jdx, jdy = dx[directions[j]], dy[directions[j]]
            # 마주보는 경우
            if (idx * jdx + idy * jdy) == -1:
                dist = abs(ix - jx) + abs(iy - jy)
                if (ix + idx * dist) == jx and (iy + idy * dist) == jy and (jx + jdx * dist) == ix and (jy + jdy * dist) == iy:
                    heappush(pred_boom, (dist, i, j))
            # 직각의 경우
            if (idx * jdx + idy * jdy) == 0:
                dist = abs(ix - jx) + abs(iy - jy)
                # print("i", i, "j", j, "dist", dist)
                # print("ix", ix, "jx", jx, "iy", iy, "jy", jy)
                # print("idx", idx, "jdx", jdx, "idy", idy, "jdy", jdy)
                # print((ix + idx * (dist // 2)))
                # print((jx + jdx * (dist // 2)))
                # print((iy + idy * (dist // 2)))
                # print((jy + jdy * (dist // 2)))
                if (ix + idx * (dist // 2)) == (jx + jdx * (dist // 2)) and (iy + idy * (dist // 2)) == (jy + jdy * (dist // 2)):
                    heappush(pred_boom, (dist, i, j))
    while pred_boom:
        t, i, j = heappop(pred_boom)
        if i not in survive_marble or j not in survive_marble:
            continue
        iw, jw = weights[i], weights[j]
        if iw > jw:
            survive_marble.remove(j)
        elif iw < jw:
            survive_marble.remove(i)
        else:
            if i > j:
                survive_marble.remove(j)
            else:
                survive_marble.remove(i)
        last_boom = t
            
    

if __name__ == "__main__":
    t = int(input().rstrip())
    pred_boom = []
    next_positions = dict()
    positions = dict()
    weights = dict()
    directions = dict()
    dir_dict = {
        "U":0,
        "D":1,
        "L":2,
        "R":3
    }
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for _ in range(t):
        initialize()
        n = int(input().rstrip())
        last_boom = -1
        for i in range(1, n + 1):
            x, y, w, d = input().rstrip().split(" ")
            positions[i] = [int(x), int(y)]
            weights[i] = int(w)
            directions[i] = dir_dict[d]
        solution()
        print(last_boom)