import sys

class bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

tmp = sys.stdin.readline().rstrip().split()

bomb1 = bomb(tmp[0], tmp[1], tmp[2])

print("code :", bomb1.code)
print("color :", bomb1.color)
print("second :", bomb1.time)