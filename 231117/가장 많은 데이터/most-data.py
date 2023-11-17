from collections import defaultdict

count = defaultdict(int)
n = int(input().rstrip())
max_cnt = 0
for _ in range(n):
    s = input().rstrip()
    count[s] += 1
    if count[s] > max_cnt:
        max_cnt = count[s]
print(max_cnt)