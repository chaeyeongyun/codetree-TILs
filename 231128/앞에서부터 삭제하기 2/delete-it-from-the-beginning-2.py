import sys
MIN_INT = -sys.maxsize
n = int(input().rstrip())
nums = list(map(int, input().rstrip().split(" ")))
# 삭제 -> 정렬 -> 평균 반복
answer = MIN_INT
sum_val = nums[-1]
min_val = nums[-1]
for k in range(2, n):
    sum_val += nums[-k]
    min_val = min(nums[-k], min_val)
    mean = (sum_val - min_val) / (k - 1)
    answer = max(mean, answer)

print("%.2f"%(answer))