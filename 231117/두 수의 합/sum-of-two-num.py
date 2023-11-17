from collections import defaultdict
n, k = map(int, input().rstrip().split(" "))
nums = list(map(int, input().rstrip().split(" ")))

ans = 0
count = defaultdict(int)
for number in nums:
    diff = k - number
    ans += count[diff]
    count[number] += 1

print(ans)