n, m = map(int, input().rstrip().split(" "))
num_to_str = dict()
str_to_num = dict()
for i in range(n):
    s = input().rstrip()
    num_to_str[i + 1] = s
    str_to_num[s] = i + 1
for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(num_to_str[int(q)])
    else:
        print(str_to_num[q])