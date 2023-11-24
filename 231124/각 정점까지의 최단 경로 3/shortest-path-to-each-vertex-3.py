from collections import defaultdict
from heapq import heappop, heappush
import sys

MAX_INT = sys.maxsize

def solution():
    global n, m, graph
    # 특정 정점에서 다른 모든 정점까지의 최단 경로
    # 다익스트라 알고리즘
    distances = [MAX_INT] * (n + 1)
    distances[1] = 0 # 출발점까지 거리는 0
    pq = [(0, 1)]
    while pq:
        dist, node = heappop(pq)
        for nxt_node, nxt_weight in graph[node]:
            new_dist = dist + nxt_weight
            if distances[nxt_node] > new_dist:
                distances[nxt_node] = new_dist
                heappush(pq, (new_dist, nxt_node))
    
    for i in range(2, n + 1):
        print(distances[i] if distances[i] != MAX_INT else -1)

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    graph = defaultdict(list)
    for _ in range(m):
        a, b, w = map(int, input().rstrip().split(" "))
        graph[a].append((b, w))
    solution()