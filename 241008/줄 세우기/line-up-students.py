n = int(input())

class stu:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

stus = []
for i in range(n):
    h, w = list(input().split())
    s = stu(int(h), int(w), i + 1)
    stus.append(s)

stus.sort(key = lambda x: (-x.h, -x.w, x.num))

for s in stus:
    print(s.h, s.w, s.num)