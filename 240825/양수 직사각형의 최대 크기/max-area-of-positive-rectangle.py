def check(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if area[i][j] < 0:
                return False
    return True

def get_sum(x1, y1, x2, y2):
    sum1 = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum1 += area[i][j]
    return sum1

def rectangle():
    maxi = 0
    ans = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    if check(x1, y1, x2, y2):
                        tmp = get_sum(x1, y1, x2, y2)
                        if tmp > maxi:
                            maxi = tmp
                            ans = (x2 - x1 + 1) * (y2 - y1 + 1)
    return ans

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

print(rectangle())