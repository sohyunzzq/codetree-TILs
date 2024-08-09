a, b = map(int, input().split())
c, d = map(int, input().split())

clean = [0] * 101

for i in range(a, b):
    clean[i] = 1
for i in range(c, d):
    clean[i] = 1

print(sum(clean))