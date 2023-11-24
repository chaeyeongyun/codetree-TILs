from collections import defaultdict
from heapq import heappop, heappush
import sys

MAX_INT = sys.maxsize

def solution():
    global n, m, k, graph
    dists = [MAX_INT] * (n + 1)
    pq = [(0, k)]
    dists[k] = 0
    while pq:
        dist, node = heappop(pq)
        for nxt_node, nxt_weight in graph[node]:
            new_dist = dist + nxt_weight
            if new_dist < dists[nxt_node]:
                dists[nxt_node] = new_dist
                heappush(pq, (new_dist, nxt_node))
    for i in range(1, n + 1):
        print(dists[i] if dists[i] != MAX_INT else -1)


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    k = int(input().rstrip())
    graph = defaultdict(list)    
    for _ in range(m):
        a, b, w = map(int, input().rstrip().split(" "))
        graph[a].append((b, w))
        graph[b].append((a, w))
    solution()