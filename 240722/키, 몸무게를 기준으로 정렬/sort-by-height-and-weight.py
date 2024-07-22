class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = []
for _ in range(n):
    name, h, w = input().split()
    people.append(Person(name, h, w))

people.sort(key = lambda x: (int(x.height), -int(x.weight)))

for _ in range(n):
    print(people[_].name, people[_].height, people[_].weight)