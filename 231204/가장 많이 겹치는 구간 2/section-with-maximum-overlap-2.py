from collections import defaultdict

n = int(input().rstrip())
checks = defaultdict(int)
for _ in range(n):
    x1, x2 = map(int, input().rstrip().split(" "))
    checks[x1] += 1
    checks[x2] -= 1

answer = 0
temp = 0
idxs = sorted(list(checks.keys()))
for idx in idxs:
    temp += checks[idx]
    answer = max(answer, temp)

print(answer)