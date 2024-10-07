import sys

class where:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(sys.stdin.readline().rstrip())

wheres = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip().split()
    wheres.append(where(tmp[0], tmp[1], tmp[2]))

wheres.sort(key = lambda x: x.name, reverse = True)

print("name", wheres[0].name)
print("addr", wheres[0].addr)
print("city", wheres[0].city)