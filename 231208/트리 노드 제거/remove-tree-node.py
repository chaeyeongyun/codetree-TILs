from collections import defaultdict, deque
n = int(input().rstrip())
parents = list(map(int, input().rstrip().split(" ")))
rm_node = int(input().rstrip())
leafs = set()

is_leaf = [True] * n
for p in parents:
    # 부모가 될 수 없는 노드가 리프노드
    is_leaf[p] = False
for i in range(n):
    if is_leaf[i]:
        leafs.add(i)

num_leaf = len(leafs)

stack = [rm_node]
while stack:
    node = stack.pop()
    if node in leafs:
        leafs.remove(node)
    for i in range(n):
        if parents[i] == node:
            stack.append(i)
if parents[rm_node] != -1:
    cnt = 0
    p = parents[rm_node]
    for i in range(n):
        if i == rm_node:
            continue
        if parents[i] == p:
             cnt += 1
    if cnt == 0:
        leafs.add(parents[rm_node])
print(len(leafs))