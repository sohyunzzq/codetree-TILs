class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []

for _ in range(n):
    name, kor, eng, math = input().split()
    students.append(Student(name, kor, eng, math))

students.sort(key = lambda x: (-int(x.kor), -int(x.eng), -int(x.math)))

for _ in range(n):
    print(students[_].name, students[_].kor, students[_].eng, students[_].math)