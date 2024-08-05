n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

ans = 0
for i in range(1, 4):
    cup = [0] * 4
    cup[i] = 1 #i번 종이컵에 조약돌
    score = 0
    for j in range(n):
        a = lst[j][0]
        b = lst[j][1]
        c = lst[j][2]
        
        cup[a], cup[b] = cup[b], cup[a]
        if cup[c] == 1:
            score += 1
    
    ans = max(ans, score)

print(ans)