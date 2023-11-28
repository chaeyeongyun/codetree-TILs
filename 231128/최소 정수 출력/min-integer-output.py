from heapq import heappop, heappush
n = int(input().rstrip())
nums = []
for _ in range(n):
    # 요소 추가와 정렬을 반복해야 한다.
    # 최소힙 사용이 적합
    # 최소힙은 삽입과 삭제가 O(logN)
    inp = int(input().rstrip())
    if inp == 0:
        x = 0
        if nums:
            x = heappop(nums)
        print(x)
    elif inp > 0:
        heappush(nums, inp)
    else:
        pass