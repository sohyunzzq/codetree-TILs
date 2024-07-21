class User:
    def __init__(self, userid="codetree", level=10):
        self.userid = userid
        self.level = level

lst = list(input().split())

user1 = User()
user2 = User(lst[0], lst[1])

print("user {} lv {}\nuser {} lv {}".format(user1.userid, user1.level, user2.userid, user2.level))