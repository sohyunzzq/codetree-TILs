class Lst:
    def __init__(self, color=0, w=0, b=0):
        self.color = color
        self.w = w
        self.b = b

n = int(input())
lsts = [Lst() for i in range(n*100*2+1)]

now = n*100

#흰색: 1, 검은색: 2, 회색: 3
for i in range(n):
    num, pos = input().split()
    if pos == "L":
        for j in range(now-int(num)+1, now+1):
            if lsts[j].w >= 1 and lsts[j].b >= 2:
                lsts[j].color = 3
            else:
                lsts[j].color = 1
            lsts[j].w += 1
        now = now - int(num) + 1
    else:
        for j in range(now, now+int(num)):
            if lsts[j].w >= 2 and lsts[j].b >= 1:
                lsts[j].color = 3
            else:
                lsts[j].color = 2
            lsts[j].b += 1
        now = now + int(num) - 1

white = 0
black = 0
gray = 0

for i in range(n*100*2+1):
    if lsts[i].color == 1:
        white += 1
    elif lsts[i].color == 2:
        black += 1
    elif lsts[i].color == 3:
        gray += 1

print(white, black, gray)