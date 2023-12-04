from collections import defaultdict
n = int(input().rstrip())
# a, b는 최대 10**9이므로 배열로 +1-1테크닉 수행은 불가
# 시작점, 끝점을 저장하여 수행
checks = defaultdict(int)
for _ in range(n):
    # 주어지는 모든 좌표값은 다름
    a, b = map(int, input().rstrip().split(" "))
    checks[a] += 1
    checks[b] -= 1

answer = 0
temp = 0
idxs = sorted(list(checks.keys()))
for i in idxs:
    temp += checks[i]
    if temp == 0:
        answer += 1

print(answer)