n = int(input())

lst = []
for i in range(n):
    lst.append(input())

alpha = input()

cnt = 0
total = 0
for i in lst:
    if i[0] == alpha:
        total += len(i)
        cnt += 1

print("{} {:.2f}".format(cnt, total/cnt))