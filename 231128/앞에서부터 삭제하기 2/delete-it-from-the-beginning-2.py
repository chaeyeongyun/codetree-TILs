import sys
MIN_INT = -sys.maxsize
n = int(input().rstrip())
nums = list(map(int, input().rstrip().split(" ")))
# 삭제 -> 정렬 -> 평균 반복
answer = MIN_INT
for k in range(1, n - 1):
    temp = nums[k:]
    min_val = 10000
    for v in temp:
        if v < min_val:
            min_val = v
    mean = (sum(temp) - min_val) / (len(temp) - 1)
    answer = max(mean, answer)

print("%.2f"%(answer))