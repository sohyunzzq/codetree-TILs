import sys

class codename:
    def __init__(self, name, score):
        self.name = name
        self.score = score

users = []
for i in range(5):
    tmp = sys.stdin.readline().rstrip().split()
    users.append(codename(tmp[0], tmp[1]))

users.sort(key = lambda x: int(x.score))

print(users[0].name, users[0].score)