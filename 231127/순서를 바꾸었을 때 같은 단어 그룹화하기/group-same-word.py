from collections import defaultdict

n = int(input().rstrip())
counter = defaultdict(int)
for _ in range(n):
    word = ''.join(sorted(list(input().rstrip())))
    counter[word] += 1
answer = 0
for word in counter:
    answer = max(counter[word], answer)
print(answer)