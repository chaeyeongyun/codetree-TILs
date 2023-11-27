from collections import defaultdict

def solution():
    global n, k, nums
    cnt = defaultdict(int)
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            target = k - nums[i] - nums[j]
            answer += cnt[target]
            
        cnt[nums[i]] += 1
    print(answer)
    

if __name__ == "__main__":
    n, k = map(int, input().rstrip().split(" "))
    nums = list(map(int, input().rstrip().split(" ")))
    solution()