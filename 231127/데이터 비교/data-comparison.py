n = int(input().rstrip())
l1 = input().rstrip().split(" ")
m = int(input().rstrip())
l2 = input().rstrip().split(" ")
l1 = set(l1)
answer = []
for s in l2:
    if s in l1:
        answer.append("1")
    else:
        answer.append("0")
print(" ".join(answer))