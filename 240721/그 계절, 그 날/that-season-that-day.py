day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isleafyear(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False

def season(m):
    if 3 <= m <= 5:
        return "Spring"
    elif 6 <= m <= 8:
        return "Summer"
    elif 9 <= m <= 11:
        return "Fall"
    else:
        return "Winter"

y, m, d = map(int, input().split())

if isleafyear(y):
    day[2] = 29

if d <= day[m]:
    print(season(m))
else:
    print(-1)