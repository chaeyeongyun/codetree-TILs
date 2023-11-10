import sys
MAX_INT = sys.maxsize
def initialize():
    global dp, first, second
    

def solution():
    global first, second, dp
    dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            fw, sw = first[i - 1], second[j - 1]
            if fw == sw:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(max(sum(dp, [])))
    # for d in dp:
    #     print(d)

if __name__ == "__main__":
    first = input().rstrip()
    second = input().rstrip()
    solution()