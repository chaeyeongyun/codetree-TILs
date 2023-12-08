from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 5)
n = int(input().rstrip())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b, dist = map(int, input().rstrip().split(" "))
    graph[a].append((b, dist))
    graph[b].append((a, dist))

def dfs(node, d = 0):
    global visited, graph, distance, last_node
    for nxt_node, dist in graph[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = True
            if distance < d + dist:
                distance =  d + dist
                last_node = nxt_node
            dfs(nxt_node, d + dist)

distance = 0
last_node = 1
visited = [False] * (n + 1)
visited[1] = True
dfs(1)
visited = [False] * (n + 1)
visited[last_node] = True
dfs(last_node)
print(distance)