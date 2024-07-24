dx, dy = [1, -1, 0, 0], [0, 0, -1, +1] 
#동: x+1 서: x-1 남: y-1 북: y+1

x, y = 0, 0
n = int(input())

for i in range(n):
    d, num = input().split()
    if d == "E":
        index = 0
    elif d == "W":
        index = 1
    elif d == "S":
        index = 2
    else:
        index = 3
    
    x, y = x + dx[index] * int(num), y + dy[index] * int(num)

print(x, y)