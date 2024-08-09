a, b, c = map(int, input().split())

#가운데랑 더 가까운 사람이, 가운데 옆으로 이동

if a + 1 == b and b + 1 == c:
    print(0)
else:
    print(max(b-a, c-b) - 1)