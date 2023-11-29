from heapq import heappop, heappush
import sys
MAX_INT = sys.maxsize

def solution():
    global n, m, j, a_list, b_list
    q = []
    a_list.sort()
    b_list.sort()
    answer = MAX_INT
    for i in range(n):
        for j in range(m):
            if len(q) < (k - 1):
                heappush(q, -(a_list[i] + b_list[j]))
                continue
            k_1 = -q[0]
            cand = a_list[i] + b_list[j]
            if cand < answer and cand > k_1:
                answer = cand
            elif cand <= k_1:
                answer = k_1
                heappop(q)
                heappush(q, -cand)
            elif cand >= answer:
                break
    print(answer)

if __name__ == "__main__":
    n, m, k = map(int, input().rstrip().split(" "))
    a_list = list(map(int, input().rstrip().split(" ")))
    b_list = list(map(int, input().rstrip().split(" ")))
    solution()