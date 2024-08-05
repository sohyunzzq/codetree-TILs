a, b, c = map(int, input().split())

ans = 0
anum = c // a
bnum = 0
    
for i in range(anum + 1):
    tmp = (anum - i) * a

    while tmp + b <= c:
        tmp += b

    ans = max(ans, tmp)

print(ans)
    
'''
26 783 882

26*3 + 783

'''