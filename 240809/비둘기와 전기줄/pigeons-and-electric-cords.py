n = int(input())

pigeons = [-1] * 11

ans = 0
for i in range(n):
    num, pos = map(int, input().split())
    if pigeons[num] != -1 and pigeons[num] != pos:
        ans += 1
    pigeons[num] = pos
    
print(ans)