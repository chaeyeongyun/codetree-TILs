# 1. 최대힙
from heapq import heappop, heappush
n, m = map(int, input().rstrip().split(" "))
temp = list(map(int, input().rstrip().split(" ")))
nums = []
for num in temp:
    heappush(nums, -num)
for _ in range(m):
    x = -heappop(nums)
    x -= 1
    heappush(nums, -x)
answer = -nums[0]
print(answer)