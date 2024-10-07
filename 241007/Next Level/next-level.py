import sys

class user:
    def __init__(self, name = "codetree", level = 10):
        self.name = name
        self.level = level

user1 = user()
name2, level2 = sys.stdin.readline().rstrip().split()
user2 = user(name2, level2)

users = [user1, user2]

for user in users:
    print("user", user.name, "lv", user.level)