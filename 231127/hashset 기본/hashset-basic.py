n = int(input())
s = set()
for _ in range(n):
    order, num = input().rstrip().split(" ")
    num = int(num)
    if order == "find":
        print("true" if num in s else "false")
    elif order == "add":
        s.add(num)
    elif order == "remove":
        s.remove(num)
    else:
        raise ValueError