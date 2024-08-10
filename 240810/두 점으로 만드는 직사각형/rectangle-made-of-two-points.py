x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

minx = min(x1, a1)
maxx = max(x2, a2)

miny = min(y1, b1)
maxy = max(y2, b2)

print((maxx - minx) * (maxy - miny))