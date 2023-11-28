num_a, num_b = map(int, input().rstrip().split(" "))
set_a = set(input().rstrip().split(" "))
set_b = set(input().rstrip().split(" "))
a_minus_b = set_a - set_b
b_minus_a = set_b - set_a
answer = len(a_minus_b.union(b_minus_a))
print(answer)