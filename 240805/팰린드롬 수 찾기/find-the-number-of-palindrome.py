x, y = map(int, input().split())

cnt = 0
for num in range(x, y+1):
    num = str(num)
    length = len(num)

    if num == num[::-1]:
        cnt += 1
print(cnt)