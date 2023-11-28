num_a, num_b = map(int, input().rstrip().split(" "))
set_a = set(input().rstrip().split(" "))
set_b = set(input().rstrip().split(" "))

answer = num_a + num_b
for elem in set_a:
    if elem in set_b:
        answer -= 2
print(answer)