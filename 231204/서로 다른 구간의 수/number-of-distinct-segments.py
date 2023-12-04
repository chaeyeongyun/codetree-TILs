from collections import defaultdict
n = int(input().rstrip())
# a, b는 최대 10**9이므로 배열로 +1-1테크닉 수행은 불가
# 시작점, 끝점을 저장하여 수행
checks = defaultdict(int)
start, end = 0, 0
for _ in range(n):
    # 주어지는 모든 좌표값은 다름
    a, b = map(int, input().rstrip().split(" "))
    checks[a] += 1
    checks[b] -= 1
    start = min(start, a, b)
    end = max(end, a, b)

answer = 0
temp = 0
for i in range(start, end + 1):
    if i not in checks:
        continue
    temp += checks[i]
    if temp == 0:
        answer += 1

print(answer)