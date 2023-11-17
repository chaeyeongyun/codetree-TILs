from collections import defaultdict
def solution():
    global n, m, nums, q_nums
    count = defaultdict(lambda: 0)
    for n in nums:
        count[n] += 1
    ans = []
    for n in q_nums:
        ans.append(str(count[n]))
    print(" ".join(ans))

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    nums = list(map(int, input().rstrip().split(" ")))
    q_nums = list(map(int, input().rstrip().split(" ")))
    solution()