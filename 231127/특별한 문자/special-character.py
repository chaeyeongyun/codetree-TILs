from collections import OrderedDict

word = input().rstrip()
def solution():
    global word
    counter = OrderedDict()
    for w in word:
        if w in counter:
            counter[w] += 1
        else:
            counter[w] = 1
    for w in counter:
        if counter[w] == 1:
            print(w)
            return
    print(None)
solution()