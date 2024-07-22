class Mem:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

mems = []
n = int(input())
for _ in range(n):
    name, h, w = input().split()
    mems.append(Mem(name, h, w))

mems.sort(key = lambda x: int(x.h))

for _ in range(n):
    print(mems[_].name, mems[_].h, mems[_].w)