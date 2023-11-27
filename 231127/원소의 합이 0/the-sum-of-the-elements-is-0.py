from collections import defaultdict
def solution():
    global n, a_list, b_list, c_list, d_list
    ab_counter, cd_counter = defaultdict(int), defaultdict(int)
    # a, b / c, d로 나누어서 두개씩?
    # O(n^2)
    for i in range(n):
        for j in range(n):
            ab_counter[a_list[i] + b_list[j]] += 1
            
    answer = 0
    for i in range(n):
        for j in range(n):
            cd = c_list[i] + d_list[j]
            if -cd in ab_counter:
                answer += ab_counter[-cd]
    print(answer)

if __name__ == "__main__":
    n = int(input().rstrip())
    a_list = list(map(int, input().rstrip().split(" ")))
    b_list = list(map(int, input().rstrip().split(" ")))
    c_list = list(map(int, input().rstrip().split(" ")))
    d_list = list(map(int, input().rstrip().split(" ")))
    solution()