class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

weathers = []
for i in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        weathers.append(Weather(date, day, weather))

weathers.sort(key = lambda x: x.date)

print(weathers[0].date, weathers[0].day, weathers[0].weather)