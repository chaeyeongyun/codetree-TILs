word = input().rstrip()

def solution():
    global word
    counter = dict()
    for w in word:
        if w in counter:
            counter[w] += 1
        else:
            counter[w] = 1
    for w in word:
        if counter[w] == 1:
            print(w)
            return
    print(None)
solution()