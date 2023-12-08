from collections import defaultdict, deque
n = int(input().rstrip())
parents = list(map(int, input().rstrip().split(" ")))
rm_node = int(input().rstrip())
graph = defaultdict(list)
for i in range(n):
    graph[parents[i]].append(i)

leafs = n - 2
q = deque([rm_node])
while q:
    node = q.popleft()
    leafs -= len(graph[node])
    for nxt in graph[node]:
        q.append(nxt)

print(leafs)