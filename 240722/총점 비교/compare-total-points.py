class Student:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

n = int(input())

students = []
for _ in range(n):
    name, a, b, c = input().split()
    students.append(Student(name, a, b, c))

students.sort(key = lambda x: int(x.a) + int(x.b) + int(x.c))

for _ in range(n):
    print(students[_].name, students[_].a, students[_].b, students[_].c)