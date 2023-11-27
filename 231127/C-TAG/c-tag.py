def test_location(x, y, z):
    global n, m, a_group, b_group
    # x, y, z 세 자리 조합 선택했을 때 A와 B가 구분가는지
    # 구분가면 True, 아니면 False를 리턴
    s = set()
    for i in range(n):
        s.add(a_group[i][x] + a_group[i][y] + a_group[i][z])
    for i in range(n):
        if (b_group[i][x] + b_group[i][y] + b_group[i][z]) in s:
            return False
    return True

def solution():
    global n, m, a_group, b_group
    answer = 0
    for i in range(m): # O(M**3)
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if test_location(i, j, k): # O(N)
                    answer += 1
    # 전체 : O(NM**3)
    print(answer)

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    a_group = [input().rstrip() for _ in range(n)]
    b_group = [input().rstrip() for _ in range(n)]
    solution()