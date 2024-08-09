a, b, c = map(int, input().split())

if (a + 1 == b and b + 1 == c) or (a - 1 == b and b - 1 == c): #이미 연속됨
    print(0)
elif (a + 2 == b) or (b + 2 == c) or (a - 2 == b) or (b - 2 == c): #가운데 낄 수 있음
    print(1)
else:
    print(2)