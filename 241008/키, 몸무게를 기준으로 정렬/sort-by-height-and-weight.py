class person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())

people = []
for i in range(n):
    n, h, w = list(input().split())
    p = person(n, int(h), int(w))
    people.append(p)

people.sort(key = lambda x: (x.h, -x.w))

for p in people:
    print(p.name, p.h, p.w)