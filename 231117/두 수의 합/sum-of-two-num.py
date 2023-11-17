from collections import defaultdict
n, k = map(int, input().rstrip().split(" "))
nums = list(map(int, input().rstrip().split(" ")))

count = defaultdict(list)
for i in range(n):
    count[nums[i]].append(i)
ans = 0
visited = defaultdict(lambda: False)
for number in nums:
    if visited[number]:
        continue
    if (k - number) not in count:
        visited[number] = True
        visited[k - number] = True    
        continue
    ans += len(count[number]) * len(count[k - number])
    visited[number] = True
    visited[k - number] = True
print(ans)