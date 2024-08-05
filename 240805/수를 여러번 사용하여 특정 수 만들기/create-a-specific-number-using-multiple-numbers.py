a, b, c = map(int, input().split())

ans = 0
anum = c // a
bnum = 0
    
while anum != 0:
    tmp = 0
    tmp += anum * a + bnum * b
    if tmp > c:
        break
    ans = max(ans, tmp)
    anum -= 1
    bnum += 1

print(ans)
    


'''
77 / 17 = 4 (68 + 9)

17
17
17
17

17 25
17
17

17 25
17 25

17 25
   25
   25
'''