answer = True
m = int(input().rstrip())
in_degree = [0] * 10001
out_degree = [0] * 10001
nodes = set()
for _ in range(m):
    a, b = map(int, input().rstrip().split(" "))
    in_degree[b] += 1
    out_degree[a] += 1
    nodes.add(a)
    nodes.add(b)
zero_in = 0
for node in nodes:
    if in_degree[node] == 0:
        zero_in += 1
        if zero_in > 1:
            answer = False
            break
    if in_degree[node] > 1:
        answer = False
        break
print(1 if answer else 0)