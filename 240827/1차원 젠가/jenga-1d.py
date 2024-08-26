def play(start, end, jenga):
    temp = []
    for i in range(len(jenga)):
        if start <= i <= end:
            continue
        temp.append(jenga[i])
    return temp

n = int(input())
jenga = []
for i in range(n):
    jenga.append(int(input()))

#구간은 다 없어지고, 그 위에 있던 거 내려옴

start, end = map(int, input().split())
jenga = play(start-1, end-1, jenga)

start, end = map(int, input().split())
jenga = play(start-1, end-1, jenga)

print(len(jenga))
for item in jenga:
    print(item)