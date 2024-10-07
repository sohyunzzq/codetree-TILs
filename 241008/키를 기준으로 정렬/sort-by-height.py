class student:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())

students = []
for i in range(n):
    tmp = list(input().split())
    s = student(tmp[0], tmp[1], tmp[2])
    students.append(s)

students.sort(key = lambda x: x.h)

for s in students:
    print(s.name, s.h, s.w)