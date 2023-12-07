from collections import defaultdict

def rotate():
    """1초의 회전"""
    global now, l, belt, chair, remain_sushi
    new_belt = dict()
    for x in belt:
        next_x = (x + 1) % l
        new_belt[next_x] = belt[x]
    belt = new_belt
    now += 1

def eat():
    # 앞에 있는 초밥 먹기
    global now, l, belt, chair, remain_sushi, sushi_cnt
    remove_chairs = []
    for chair_num in chair:
        name = chair[chair_num]
        if chair_num in belt and name in belt[chair_num]:
            if remain_sushi[name] < belt[chair_num][name]:
                belt[chair_num][name] -= remain_sushi[name]
                sushi_cnt -= remain_sushi[name]
                del remain_sushi[name]
                remove_chairs.append(chair_num)
                del belt[chair_num][name] # 같은 손님 또 안오므로 이 사전은 또 쓰일일이 없음
            elif remain_sushi[name] > belt[chair_num][name]:
                remain_sushi[name] -= belt[chair_num][name]
                sushi_cnt -= belt[chair_num][name]
                del belt[chair_num][name]
            else:
                sushi_cnt -= remain_sushi[name]
                del belt[chair_num][name]
                del remain_sushi[name]
                remove_chairs.append(chair_num)
    for rm in remove_chairs:
        del chair[rm]

def make_sushi(inp):
    global now, belt, chair, remain_sushi, sushi_cnt
    t, x, name = inp
    t, x = int(t), int(x)
    for _ in range(t - now - 1):
        rotate()
        eat()
    rotate()
    if x not in belt:
        belt[x] = dict()
    if name in belt[x]:
        belt[x][name] += 1
    else:
        belt[x][name] = 1
    sushi_cnt += 1
    eat()

def customer_in(inp):
    global now, belt, chair, remain_sushi, sushi_cnt
    t, x, name, n = inp
    t, x, n = int(t), int(x), int(n)
    for _ in range(t - now - 1):
        rotate()
        eat()
    rotate()
    chair[x] = name
    remain_sushi[name] = n
    eat()

def take_a_picture(inp):
    global now, belt, chair, remain_sushi, sushi_cnt
    t = int(inp[0])
    for _ in range(t - now):
        rotate()
        eat()
    customer_cnt = len(chair)
    print(f"{customer_cnt} {sushi_cnt}")




def print_info():
    print("now", now)
    print("belt")
    print(belt)
    print("chair")
    print(chair)
    print("remain_sushi")
    print(remain_sushi)


if __name__ == "__main__":
    l, q = map(int, input().rstrip().split(" "))
    belt = dict()
    chair = dict()
    remain_sushi = dict()
    sushi_cnt = 0
    now = 0
    for _ in range(q):
        order, *inp = input().rstrip().split(" ")
        if order == "100":
            make_sushi(inp)
        elif order == "200":
            customer_in(inp)
        elif order == "300":
            take_a_picture(inp)
        else:
            raise ValueError