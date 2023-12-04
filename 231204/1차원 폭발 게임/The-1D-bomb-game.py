from collections import deque

def solution():
    global n, m, bombs
    result = []
    if m == 1:
        return result
    end = False
    while not end:
        boom = False
        past = -1
        cnt = 0
        for i in range(len(bombs)):
            if bombs[i] == past:
                if cnt == 0:
                    cnt = 2
                    result.pop()
                else:
                    cnt += 1
            else:
                if cnt >= m:
                    boom = True
                else:
                    result += [past] * cnt
                result.append(bombs[i])
                cnt = 0
            past = bombs[i]
        if cnt < m:
            result += [past] * cnt
        if not boom:
            end = True
        if not end:
            bombs = result[:]
            result = []
    return result    
    
            

if __name__ == "__main__":
    n, m = map(int, input().rstrip().split(" "))
    bombs = [int(input().rstrip()) for _ in range(n)]
    result = solution()
    print(len(result))
    for r in result:
        print(r)