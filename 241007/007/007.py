import sys

class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

c, p, t = sys.stdin.readline().rstrip().split()

s = Secret(c, p, t)

print("secret code :", s.code)
print("meeting point :", s.place)
print("time :", s.time)