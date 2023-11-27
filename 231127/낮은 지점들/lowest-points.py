from heapq import heappop, heappush

coordinates = dict()
n = int(input().rstrip())
for _ in range(n):
    x, y = map(int, input().rstrip().split(" "))
    if x in coordinates:
        coordinates[x] = min(coordinates[x], y)
    else:
        coordinates[x] = y

answer = 0
for x in coordinates:
    answer += coordinates[x]
print(answer)