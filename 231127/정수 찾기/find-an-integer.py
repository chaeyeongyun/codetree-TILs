n = int(input().rstrip())
a = input().rstrip().split(" ")
m = int(input().rstrip())
b = input().rstrip().split(" ")

a = set(a)
for i in b:
    if i in a:
        print(1)
    else:
        print(0)