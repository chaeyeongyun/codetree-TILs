from collections import defaultdict
n = int(input().rstrip())
# 루트노드는 1
graph = defaultdict(list)
for _ in range(n - 1):
    x, y = map(int, input().rstrip().split(" "))
    graph[x].append(y)
    graph[y].append(x)

parents = [0] * (n + 1)
visited = [False] * (n + 1)
def dfs(node):
    global graph, visited, parents
    for nxt in graph[node]:
        if not visited[nxt]:
            parents[nxt] = node
            visited[nxt] = True
            dfs(nxt)

visited[1] = True
dfs(1)
for i in range(2, n + 1):
    print(parents[i])