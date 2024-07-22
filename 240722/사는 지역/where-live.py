class City:
    def __init__(self, name, num, city):
        self.name = name
        self.num = num
        self.city = city

n = int(input())
people = []

for i in range(n):
    name, num, city = input().split()
    people.append(City(name, num, city))

people.sort(key = lambda x: x.name)

print("name {}".format(people[2].name))
print("addr {}".format(people[2].num))
print("city {}".format(people[2].city))