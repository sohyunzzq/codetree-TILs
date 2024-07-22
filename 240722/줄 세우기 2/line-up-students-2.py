class Student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())
students = []

for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i+1))

students.sort(key = lambda x: (x.height, -x.weight))

for i in range(n):
    print(students[i].height, students[i].weight, students[i].num)