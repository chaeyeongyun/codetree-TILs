from collections import defaultdict
n = int(input().rstrip())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b, dist = map(int, input().rstrip().split(" "))
    graph[a].append((b, dist))
    graph[b].append((a, dist))

def dfs(node, d = 0):
    global visited, graph, distance
    for nxt_node, dist in graph[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = True
            distance = max(distance, d + dist)
            dfs(nxt_node, d + dist)

distance = 0
for i in range(1, n + 1):
    if i in graph[i - 1]:
        continue
    visited = [False] * (n + 1)
    visited[i] = True
    dfs(i)
print(distance)