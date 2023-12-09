import sys

nums = ["4", "5", "6"]
n = int(input().rstrip())

def check(comb):
    l = len(comb) // 2
    for i in range(1, l + 1):
        if comb[-i:] == comb[-2*i:-2*i + i]:
            return False
    return True


def dfs(comb=""):
    if len(comb) == n:
        print("".join(comb))
        sys.exit()
    for num in nums:
        nxt_comb = comb + num
        if check(nxt_comb):
            dfs(nxt_comb)

dfs()