import sys
MAX_INT = sys.maxsize

def solution():
    global ckpoints, n
    dist_l, dist_r = [0] * n, [0] * n
    for i in range(1, n):
        ax, ay = ckpoints[i]
        bx, by = ckpoints[i - 1]
        dist_l[i] = abs(ax - bx) + abs(ay - by) + dist_l[i - 1]
    for i in range(n-2, -1, -1):
        ax, ay = ckpoints[i]
        bx, by = ckpoints[i + 1]
        dist_r[i] = abs(ax - bx) + abs(ay - by) + dist_r[i + 1]
    # print(dist_l)
    # print(dist_r)
    answer = MAX_INT
    for i in range(1, n-1): # 첫번째와 마지막 체크포인트를 제외하고 빼본다
        d = dist_l[i - 1] + dist_r[i + 1]
        ax, ay = ckpoints[i - 1]
        bx, by = ckpoints[i + 1]
        d += abs(ax - bx) + abs(ay - by)
        answer = min(answer, d)
    print(answer)
        

if __name__ == "__main__":
    n = int(input().rstrip())
    ckpoints = [tuple(map(int, input().rstrip().split(" "))) for _ in range(n)]
    solution()