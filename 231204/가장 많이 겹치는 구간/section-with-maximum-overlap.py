n = int(input().rstrip())
sections = [0] * 200001
start, end = 0, 0
for _ in range(n):
    a, b = map(int, input().rstrip().split(" "))
    sections[a] += 1
    sections[b] -= 1
    start = min(start, a, b)
    end = max(end, a, b)

answer = 0
cnt = 0
for i in range(start, end + 1):
    cnt += sections[i]
    answer = max(answer, cnt)
print(answer)