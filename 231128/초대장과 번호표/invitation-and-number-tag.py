def solution():
    global n, g, groups, member_cnt, person_to_group
    answer = 0 
    visited = [False] * (n + 1)
    stack = [1]
    while stack:
        nxt = stack.pop()
        if visited[nxt]:
            continue
        answer += 1
        for g in person_to_group[nxt]:
            groups[g].remove(nxt)
            if len(groups[g]) == 1:
                v = groups[g].pop()
                if not visited[v]:
                    groups[g].add(v)
                    stack.append(v)
        visited[nxt] = True

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