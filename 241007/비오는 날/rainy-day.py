import sys

class data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(sys.stdin.readline().rstrip())

datas = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip().split()
    if tmp[2] == "Rain":
        datas.append(data(tmp[0], tmp[1], tmp[2]))

datas.sort(key = lambda x: x.date)

print(datas[0].date, datas[0].day, datas[0].weather)