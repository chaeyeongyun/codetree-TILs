# 삽입, 제거, 정렬이 반복
# 우선순위큐
from heapq import heappush, heappop
nums = []
n = int(input().rstrip())
for _ in range(n):
    num = int(input().rstrip())
    if num > 0:
        heappush(nums, -num)
    elif num == 0:
        top = 0
        if nums:
            top = -heappop(nums)
        print(top)
    else:
        pass