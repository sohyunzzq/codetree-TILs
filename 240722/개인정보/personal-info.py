class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for _ in range(5):
    name, h, w = input().split()
    people.append(Person(name, h, w))

print("name")
people.sort(key = lambda x: x.name)
for _ in range(5):
    print("{} {} {:.1f}".format(people[_].name, people[_].height, float(people[_].weight)))
print()

print("height")
people.sort(key = lambda x: -int(x.height))
for _ in range(5):
    print("{} {} {:.1f}".format(people[_].name, people[_].height, float(people[_].weight)))