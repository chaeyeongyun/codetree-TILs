from collections import defaultdict
def solution():
    global n, k, nums
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
    counter_list = []
    for key in counter:
        counter_list.append((key, counter[key]))
    counter_list.sort(key=lambda x: (-x[1], -x[0]))
    answers = [str(counter_list[i][0]) for i in range(k)]
    print(" ".join(answers))
        

if __name__ == "__main__":
    n, k = map(int, input().rstrip().split(" "))
    nums = list(map(int, input().rstrip().split(" ")))
    solution()