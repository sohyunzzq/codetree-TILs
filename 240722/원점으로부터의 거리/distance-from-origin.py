class Coor:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

n = int(input())
Coors = []

for i in range(n):
    x, y = map(int, input().split())
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    Coors.append(Coor(x, y, i+1))

Coors.sort(key = lambda x: (x.x + x.y))

for _ in range(n):
    print(Coors[_].num)