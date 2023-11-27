def solution():
    global n, k, change
    pos_record = dict() 
    positions = dict()
    for i in range(1, n + 1):
        positions[i] = i
        pos_record[i] = {i}
    # print(positions)
    # print(pos_record)
    # print("\n")
    for _ in range(3):
        for i in range(k):
            a, b = change[i]
            temp = positions[a]
            positions[a] = positions[b]
            positions[b] = temp
            pos_record[a].add(positions[a])
            pos_record[b].add(positions[b])
            # print(list(positions.values()))
    # print("\n")
    # print(positions)
    # print(pos_record)
    for i in range(1, n + 1):
        print(len(pos_record[i]))


if __name__ == "__main__":
    n, k = map(int, input().rstrip().split(" "))
    change = []
    for _ in range(k):
        change.append(tuple(map(int, input().rstrip().split(" "))))
    solution()