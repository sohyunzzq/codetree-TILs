def baseball(ans0, ans1, ans2):
    for i in range(n):
        s = 0
        b = 0
        temp = lst[i][0]

        if int(temp[0]) == ans0:
            s += 1
        if int(temp[1]) == ans1:
            s += 1
        if int(temp[2]) == ans2:
            s += 1
        if int(temp[0]) in (ans1, ans2):
            b += 1
        if int(temp[1]) in (ans0, ans2):
            b += 1
        if int(temp[2]) in (ans0, ans1):
            b += 1
    
        if lst[i][1] != s or lst[i][2] != b:
            return False
    return True

n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
    lst[i][0] = str(lst[i][0])

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            if baseball(i, j, k):
                cnt += 1

print(cnt)