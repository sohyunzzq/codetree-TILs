class Code:
    def __init__(self, name, score):
        self.n = name
        self.s = score

codes = []
for i in range(5):
    name, score = input().split()
    codes.append(Code(name, score))

codes.sort(key = lambda x: int(x.s))
print(codes[0].n, codes[0].s)