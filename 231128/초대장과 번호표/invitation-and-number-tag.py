def solution():
    global n, g, groups, member_cnt, person_to_group
    answer = 0 
    stack = [1]
    while stack:
        answer += 1
        nxt = stack.pop()
        for g in person_to_group[nxt]:
            groups[g].remove(nxt)
            if len(groups[g]) == 1:
                for v in groups[g]:
                    stack.append(v)
    print(answer)

if __name__ == "__main__":
    n, g = map(int, input().rstrip().split(" "))
    groups = dict()
    member_cnt = dict()
    person_to_group = dict()
    for i in range(1, g + 1):
        cnt, *members = map(int, input().rstrip().split(" "))
        groups[i] = set(members)
        member_cnt[i] = cnt
        for member in members:
            if member not in person_to_group:
                person_to_group[member] = [i]
            else:
                person_to_group[member].append(i)
    solution()