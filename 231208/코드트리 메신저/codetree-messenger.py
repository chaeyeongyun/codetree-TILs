from collections import defaultdict, deque

def ready(inp):
    global n, parents, auths, graph
    for i in range(n):
        parents[i + 1] = int(inp[i])
    for i in range(n, 2 * n):
        auths[i - n + 1] = int(inp[i])
    for i in range(1, n + 1):
        p, c = parents[i], i
        graph[p].add(c)

def alarm_switch(inp):
    global alarm
    c = int(inp[0])
    alarm[c] = not alarm[c]

def auth_change(inp):
    global auths
    c, power = map(int, inp)
    auths[c] = power

def change_parents(inp):
    global parents, graph
    c1, c2 = map(int, inp)
    c1_p, c2_p = parents[c1], parents[c2]
    parents[c1], parents[c2] = c2_p, c1_p
    graph[c1_p].remove(c1)
    graph[c1_p].add(c2)
    graph[c2_p].remove(c2)
    graph[c2_p].add(c1)

def num_can_alarm(inp):
    global graph, auths, alarm
    c = int(inp[0])
    num = 0
    q = deque([(c, 0)])
    while q:
        node, dist = q.popleft()
        for child in graph[node]:
            if not alarm[child]:
                continue
            if auths[child] < (dist + 1):
                continue
            q.append((child, dist + 1))
            num += 1
    print(num)

if __name__ == "__main__":
    n, q = map(int, input().rstrip().split(" "))
    parents, auths = [-1] * (n + 1), [-1] * (n + 1)
    alarm = [True]  * (n + 1)
    graph = defaultdict(set)
    for _ in range(q):
        order, *inp = input().rstrip().split(" ")
        if order == "100":
            ready(inp)
        elif order == "200":
            alarm_switch(inp)
        elif order == "300":
            auth_change(inp)
        elif order == "400":
            change_parents(inp)
        elif order == "500":
            num_can_alarm(inp)
        else:
            raise ValueError