from heapq import heappop, heappush
t = int(input().rstrip())
for _ in range(t):
    max_heap, min_heap = [], []
    m = int(input().rstrip())
    nums = list(map(int, input().rstrip().split(" ")))
    answer = []
    for i in range(m):
        heappush(max_heap, -nums[i])
        heappush(min_heap, nums[i])
        if i % 2 == 0:
            max_temp, min_temp = max_heap[:], min_heap[:]
            for _ in range(len(max_temp)):
                ma, mi = -heappop(max_temp), heappop(min_temp)
                if ma == mi:
                    answer.append(str(ma))
                    break
    print(" ".join(answer))