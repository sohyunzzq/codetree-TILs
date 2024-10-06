import sys

n = int(sys.stdin.readline())

dict1 = {"E": 0, "S": 1, "W": 2, "N": 3}
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0

for i in range(n):
    dr, num = input().split()

    dr = dict1[dr]
    for j in range(int(num)):
        x += dx[dr]
        y += dy[dr]

print(x, y)