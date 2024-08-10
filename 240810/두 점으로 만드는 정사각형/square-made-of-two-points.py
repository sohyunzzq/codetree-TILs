x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

#정사각형

minx = min(x1, a1)
miny = min(y1, b1)

maxx = max(x2, a2)
maxy = max(y2, b2)

print(max(maxx - minx, maxy - miny) ** 2)