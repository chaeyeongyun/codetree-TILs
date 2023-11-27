from collections import defaultdict
def solution():
    global n, a_list, b_list, c_list, d_list
    # n**4개의 경우의 수 있음
    # 요소의 개수 체크 O(n)
    # a_counter, b_counter, c_counter, d_counter = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    # for i in range(n):
    #     a_counter[a_list[i]] += 1
    #     b_counter[b_list[i]] += 1
    #     c_counter[c_list[i]] += 1
    #     d_counter[d_list[i]] += 1
    ab_counter, cd_counter = defaultdict(int), defaultdict(int)
    # a, b / c, d로 나누어서 두개씩?
    for i in range(n):
        for j in range(n):
            ab_counter[a_list[i] + b_list[j]] += 1
            cd_counter[c_list[i] + d_list[j]] += 1
    answer = 0
    for ab in ab_counter:
        answer += ab_counter[ab] * cd_counter[-ab]
    print(answer)

if __name__ == "__main__":
    n = int(input().rstrip())
    a_list = list(map(int, input().rstrip().split(" ")))
    b_list = list(map(int, input().rstrip().split(" ")))
    c_list = list(map(int, input().rstrip().split(" ")))
    d_list = list(map(int, input().rstrip().split(" ")))
    solution()