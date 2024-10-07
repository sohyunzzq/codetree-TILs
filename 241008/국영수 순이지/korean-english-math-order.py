n = int(input())

class score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

scores = []
for i in range(n):
    n, k, e, m = list(input().split())
    s = score(n, int(k), int(e), int(m))

    scores.append(s)

scores.sort(key = lambda x: (-x.kor, -x.eng, -x.math))
for s in scores:
    print(s.name, s.kor, s.eng, s.math)