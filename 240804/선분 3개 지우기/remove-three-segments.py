n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            area = [0] * 101
            for m in range(n):
                if m == i or m == j or m == k:
                    continue
                
                for r in range(lst[m][0], lst[m][1] + 1):
                    area[r] += 1
                
            check = True
            for r in range(101):
                if area[r] > 1:
                    check = False
                    break
            if check:
                cnt += 1

print(cnt)