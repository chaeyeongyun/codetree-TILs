def initialize():
    global sa, sb, dp
    for i in range(1, len(sa)):
        dp[0][i] = i
    for i in range(1, len(sb)):
        dp[i][0] = i
    

def solution():
    global sa, sb, dp
    dp = [[0] * len(sa) for _ in range(len(sb))]
    initialize()
    for i in range(1, len(sb)):
        for j in range(1, len(sa)):
            if sb[i] == sa[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    # for d in dp:
    #     print(d)
    print(dp[-1][-1])


if __name__ == "__main__":
    sa = [0] + list(input().rstrip())
    sb = [0] + list(input().rstrip())
    solution()