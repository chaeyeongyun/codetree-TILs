from heapq import heappop, heappush
t = int(input().rstrip())
for _ in range(t):
    left_max_heap, right_min_heap = [], []
    m = int(input().rstrip())
    nums = list(map(int, input().rstrip().split(" ")))
    mid = nums[0]
    mid_list = [mid]
    for i in range(m // 2):
        a, b = nums[2 * i + 1], nums[2 * i + 2]
        cnt = 0
        if a < mid:
            cnt += 1
            heappush(left_max_heap, -a)
        else:
            heappush(right_min_heap, a)
        if b < mid:
            cnt += 1
            heappush(left_max_heap, -b)
        else:
            heappush(right_min_heap, b)
        if cnt == 2:
            # case 1. mid보다 작은값 두개가 들어왔을 때
            # left_max_heap에거 가장 큰 값이 mid가 되고 원래 mid는 right_min_heap에 들어간다
            heappush(right_min_heap, mid)
            mid = -heappop(left_max_heap)
        elif cnt == 0:
            # case 2. mid보다 큰 값 두개가 들어왔을 때
            # right_min_heap에거 가장 작은 값이 mid가 되고 원래 mid는 left_max_heap에 들어간다
            heappush(left_max_heap, mid)
            mid = heappop(right_min_heap)
        elif cnt == 1:
            # case 3. mid보다 큰 값 하나, 작은 값 하나 들어왔을때
            # mid는 그대로
            pass
        mid_list.append(mid)
    print(*mid_list)