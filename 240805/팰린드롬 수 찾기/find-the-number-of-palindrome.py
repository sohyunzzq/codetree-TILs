x, y = map(int, input().split())

cnt = 0
for num in range(x, y+1):
    num = str(num)
    length = len(num)

    if num[0:length//2+1] == num[::-1][0:length//2+1]:
        cnt += 1

print(cnt)