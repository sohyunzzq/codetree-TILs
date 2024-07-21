class Secret:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time
    
lst = list(input().split())

s = Secret(lst[0], lst[1], lst[2])

print("secret code : {}\nmeeting point : {}\ntime : {}".format(s.code, s.point, s.time))