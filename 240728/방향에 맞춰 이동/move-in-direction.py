dx, dy = [1, -1, 0, 0], [0, 0, -1, +1] 
#동: x+1 서: x-1 남: y-1 북: y+1
dict1 = {"E": 0, "W": 1, "S": 2, "N": 3}

x, y = 0, 0
n = int(input())

for i in range(n):
    d, num = input().split()
    index = dict1[d]
        
    x += dx[index] * int(num)
    y += dy[index] * int(num)

print(x, y)