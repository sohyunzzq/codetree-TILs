x, y = map(int, input().split())

ans = 0
for num in range(x, y+1):
    num = str(num)
    check = [0] * 10

    for i in range(len(num)):
        check[int(num[i])] += 1
    
    same = 0 #2개 이상 같은 숫자
    diff = 0 #하나만 다른 숫자
    for i in range(10):
        if check[i] >= 2:
            same += 1
        elif check[i] == 1:
            diff += 1
    
    if same == 1 and diff == 1:
        ans += 1

print(ans)