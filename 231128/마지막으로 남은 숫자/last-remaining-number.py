# 정렬, 제거, 삽입 반복
from heapq import heappop, heappush, heapify
n = int(input().rstrip())
nums = list(map(lambda x: -int(x), input().rstrip().split(" ")))
heapify(nums)
while len(nums) >= 2:
    a = -heappop(nums)
    b = -heappop(nums)
    diff = abs(a - b)
    if diff > 0:
        heappush(nums, -diff)
if nums:
    print(-nums[0])
else:
    print(-1)