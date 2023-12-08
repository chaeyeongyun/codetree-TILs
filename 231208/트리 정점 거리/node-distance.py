from collections import defaultdict
def dfs(node, target, dist, visited):
    global n, ans, tree
    for nxt, d in tree[node]:
        if not visited[nxt]:
            visited[nxt] = True
            if nxt == target:
                ans = dist + d
                return
            dfs(nxt, target, dist + d, visited)

def get_dist(a, b):
    global n, tree, ans
    visited = [False] * (n + 1)
    ans = 0
    visited[a] = True
    dfs(a, b, 0, visited)

n, m = map(int, input().rstrip().split(" "))
tree = defaultdict(list)
ans = 0
for _ in range(n - 1):
    a, b, d = map(int, input().rstrip().split(" "))
    tree[a].append((b, d))
    tree[b].append((a, d))
for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    get_dist(a, b)
    print(ans)