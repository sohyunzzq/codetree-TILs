a, b = map(int, input().split())
c, d = map(int, input().split())

if b < c or d < a: #안 겹침
    print(b-a + d-c)
else: #겹칩
    print(max(b, d) - min(a, c))