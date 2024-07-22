class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
code, color, second = input().split()
b = Bomb(code, color, second)

print("code : {}".format(b.code))
print("color : {}".format(b.color))
print("second : {}".format(b.second))