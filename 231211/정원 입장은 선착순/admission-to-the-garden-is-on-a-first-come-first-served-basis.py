from heapq import heappop, heappush

def solution():
    global people
    answer = 0
    garden = None
    # (i, a, t)로 저장하여 번호 작은 것부터 나오도록
    wait_list = []
    out_time = 0
    while people or wait_list:
        if garden is None or not wait_list:
            garden = heappop(people)
            in_time = garden[0]
            out_time = garden[0] + garden[2]
            answer = max(answer, in_time - garden[0])
        elif wait_list:
            garden = heappop(wait_list)
            in_time = out_time
            out_time = in_time + garden[2]
            answer = max(answer, (in_time - garden[1]))
        
        while people and people[0][0] < out_time:
            a, i, t = heappop(people)
            heappush(wait_list, (i, a, t))
    print(answer)


if __name__ == "__main__":
    N = int(input().rstrip())
    people = []
    for i in range(1, N + 1):
        ai, ti = map(int, input().rstrip().split(" "))
        # (a, i, t)로 저장하여 들어온 순으로 추출하되 들어운 시간이 같으면 번호가 작은 것이 나오도록
        heappush(people, (ai, i, ti))
    solution()