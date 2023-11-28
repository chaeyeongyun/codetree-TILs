from heapq import heappop, heappush

class PriorityQueue():
    """최대힙"""
    def __init__(self, vals:list=[]):
        self.items = []
        for val in vals:
            heappush(self.items, -val)
    def pop(self):
        return -heappop(self.items)
    def push(self, v):
        heappush(self.items, -v)
    def empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def top(self):
        return -self.items[0]

if __name__ == "__main__":
    n = int(input().rstrip())
    q = PriorityQueue()
    for _ in range(n):
        order, *inp = input().rstrip().split(" ")
        if order == "push":
            q.push(int(inp[0]))
        elif order == "size":
            print(q.size())
        elif order == "pop":
            print(q.pop())
        elif order == "empty":
            print(1 if q.empty() else 0)
        elif order == "top":
            print(q.top())
        else:
            raise ValueError