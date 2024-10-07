class person:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

people = []
for i in range(5):
    n, h, w = list(input().split())
    p = person(n, h, w)

    people.append(p)

people.sort(key = lambda x: x.n)
print("name")
for p in people:
    print(p.n, p.h, p.w)

print()
people.sort(key = lambda x: -int(x.h))
print("height")
for p in people:
    print(p.n, p.h, p.w)