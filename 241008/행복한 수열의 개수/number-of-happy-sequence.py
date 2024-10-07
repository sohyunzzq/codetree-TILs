n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

def happy_row(area, num):
    for i in range(m):
        if area[row][col + i] != num:
            return False
    return True
        
cnt = 0
for row in range(n):
    for col in range(n-m+1):
        if happy_row(area, area[row][col]):
            cnt += 1
            break

lst2 = []
for i in range(n):
    lst2.append([0] * n)

for row in range(n):
    for col in range(n):
        lst2[row][col] = area[col][row]

for row in range(n):
    for col in range(n-m+1):
        if happy_row(lst2, lst2[row][col]):
            cnt += 1
            break

print(cnt)