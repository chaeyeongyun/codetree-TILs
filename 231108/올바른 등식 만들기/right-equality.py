def inrange(x):
    return -20 <= x <= 20

def solution():
    global n, m, nums
    nums.insert(0, 0)
    # dp[i][j] = i번째 수까지 고려했을 때 합이 j인 가짓수
    dp = [[0] * 41 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        num = nums[i]
        for j in range(-20, 21):
            plus = dp[i - 1][j - num] if inrange(j - num) else 0
            minus = dp[i - 1][j + num] if inrange(j + num) else 0
            dp[i][j] = plus + minus
    print(dp[n][m])


if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    nums = list(map(int, input().rstrip().split(" ")))
    solution()