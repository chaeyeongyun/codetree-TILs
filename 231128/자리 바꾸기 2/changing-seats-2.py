def solution():
    global n, k, change
    pos_record = dict() 
    positions = dict()
    for i in range(1, n + 1):
        positions[i] = i
        pos_record[i] = {i}

    for _ in range(3):
        for i in range(k):
            a, b = change[i]
            positions[a], positions[b] = positions[b], positions[a]
            if a not in pos_record[positions[a]]:
                pos_record[positions[a]].add(a)
            if b not in pos_record[positions[b]]:
                pos_record[positions[b]].add(b)
            
    for i in range(1, n + 1):
        print(len(pos_record[i]))


if __name__ == "__main__":
    n, k = map(int, input().rstrip().split(" "))
    change = []
    for _ in range(k):
        change.append(tuple(map(int, input().rstrip().split(" "))))
    solution()