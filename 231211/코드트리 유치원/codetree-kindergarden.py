class Student:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None
    def __repr__(self):
        pn = "None" if self.prev is None else self.prev.num
        nn = "None" if self.next is None else self.next.num
        return f"num {self.num}, prev {pn}, next {nn}"

def insert_next_a(inp):
    global students, cur_student
    a, b = inp
    if a not in students:
        students[a] = Student(num = a)
    a_student = students[a]
    while cur_student in students:
        cur_student += 1
    prev = a_student
    for _ in range(b):
        students[cur_student] = Student(cur_student)
        students[cur_student].prev = prev
        students[cur_student].next = prev.next
        if students[cur_student].prev is not None:
            students[cur_student].prev.next = students[cur_student]
        if students[cur_student].next is not None:
            students[cur_student].next.prev = students[cur_student]
        prev = students[cur_student]
        cur_student += 1

def insert_prev_a(inp):
    global students, cur_student
    a, b = inp
    if a not in students:
        students[a] = Student(num = a)
    a_student = students[a]
    while cur_student in students:
        cur_student += 1
    next = a_student
    for _ in range(b):
        students[cur_student] = Student(cur_student)
        students[cur_student].next = next
        students[cur_student].prev = next.prev
        if students[cur_student].prev is not None:
            students[cur_student].prev.next = students[cur_student]
        if students[cur_student].next is not None:
            students[cur_student].next.prev = students[cur_student]
        cur_student += 1

def get_prev_next(inp):
    global students
    a = inp[0]
    if a not in students:
        print(-1)
        return
    if students[a].prev is None or students[a].next is None:
        print(-1)
        return
    print(f"{students[a].prev.num} {students[a].next.num}")

def print_students():
    global students
    for st in students:
        print(students[st])

if __name__ == "__main__":
    Q = int(input().rstrip())
    students = dict()
    cur_student = 1
    for _ in range(Q):
        order, *inp = map(int, input().rstrip().split(" "))
        if order == 1:
            insert_next_a(inp)
        elif order == 2:
            insert_prev_a(inp)
        elif order == 3:
            get_prev_next(inp)
        else:
            raise ValueError
        # print_students()