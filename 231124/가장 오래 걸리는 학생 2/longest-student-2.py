from heapq import heappush, heappop
from collections import defaultdict

def solution():
    global n, m, reverse_graph
    # 학교(N)까지의 최단거리가 가장 큰 학생(1~N-1) 구하기
    # N에서 다른 모든 정점까지의 거리를 구하면 된다
    dists = [-1] * (n + 1)
    pq = [(0, n)]
    dists[n] = 0
    while pq:
        dist, node = heappop(pq)
        for nxt_n, nxt_d in reverse_graph[node]:
            new_dist = dist + nxt_d
            if new_dist < dists[nxt_n] or dists[nxt_n] == -1:
                dists[nxt_n] = new_dist
                heappush(pq, (new_dist, nxt_n))
    print(max(dists)) 

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    reverse_graph = defaultdict(list)
    for _ in range(m):
        i, j, d = map(int, input().rstrip().split(" "))
        reverse_graph[j].append((i, d))
    solution()