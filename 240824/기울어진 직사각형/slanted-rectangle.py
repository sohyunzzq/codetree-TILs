def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def distance(x, y, odd, even):
    sum1 = 0
    lst = [odd, even, odd, even]

    for i, j in enumerate(lst):
        for k in range(j):
            x += dx[i]
            y += dy[i]

            if not in_range(x, y):
                return 0
            
            sum1 += area[x][y]
    return sum1


def rectangle(x, y):
    maxi = 0
    for odd in range(1, n): #/ 방향 길이
        for even in range(1, n): #\ 방향 길이
            maxi = max(maxi, distance(x, y, odd, even))
    
    return maxi

dx, dy = [-1, -1, 1, 1], [1, -1, -1, 1]

ans = 0
n = int(input())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n): #시작점이 (i, j)
        ans = max(ans, rectangle(i, j))

print(ans)