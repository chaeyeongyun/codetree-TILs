n, m = map(int, input().rstrip().split(" "))
graph = dict()
for i in range(1, n + 1):
    graph[i] = []
for _ in range(m):
    x, y = map(int, input().rstrip().split(" "))
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    global graph, visited, answer
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            answer += 1
            dfs(next_node)

visited = [False] * (n + 1)
visited[1] = True
answer = 0
dfs(1)
print(answer)