def add(inp):
    global hashmap
    k, v = inp
    hashmap[k] = v

def find(inp):
    global hashmap
    key = inp[0]
    val = hashmap.get(key, None)
    print(val)

def remove(inp):
    global hashmap
    key = inp[0]
    del hashmap[key]

if __name__ == "__main__":
    n = int(input().rstrip())
    hashmap = dict()
    for _ in range(n):
        order, *inp = input().rstrip().split(" ")
        if order == "add":
            add(inp)
        elif order == "find":
            find(inp)
        elif order == "remove":
            remove(inp)
        else:
            raise ValueError