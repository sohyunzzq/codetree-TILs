a, b, x, y = map(int, input().split())

#a - b          :3 - 10
#a - x - y - b  :3 - 2/8 - 10
#a - y - x - b  :3 - 8/2 - 10

ans1 = b - a
ans2 = abs(x-a) + abs(b-y)
ans3 = abs(y-a) + abs(b-x)

print(min(ans1, ans2, ans3))