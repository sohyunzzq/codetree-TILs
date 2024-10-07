class coor:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

n = int(input())

coors = []
for i in range(n):
    x, y = map(int, input().split())
    c = coor(x, y, i+1)

    coors.append(c)

coors.sort(key = lambda x: (abs(x.x) + abs(x.y), x.num))

for c in coors:
    print(c.num)