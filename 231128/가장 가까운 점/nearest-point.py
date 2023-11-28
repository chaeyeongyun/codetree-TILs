# 가장 가까운 점을 고르고, 2를 더해주고, 다시 넣어줌
# 삭제, 삽입, 정렬이 반복되어야함
# 우선순위큐가 적절하다
from heapq import heappop, heappush
n, m = map(int, input().rstrip().split(" "))
points = []
for _ in range(n):
    x, y = map(int, input().rstrip().split(" "))
    heappush(points, (abs(x) + abs(y), x, y))
for _ in range(m):
    dist, x, y = heappop(points)
    x, y = x + 2, y + 2
    heappush(points, (abs(x) + abs(y), x, y))
print(points[0][1], points[0][2])