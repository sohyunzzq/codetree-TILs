n = int(input())

lst = [0] * 101
numlst = []
for i in range(n):
    num, alpha = input().split()
    lst[int(num)] = alpha

max_val = 0

for i in range(101):
    for j in range(i, 101):
        if lst[i] == 0 or lst[j] == 0:
            continue
            
        g, h = 0, 0
        for k in range(i, j + 1):
            if lst[k] == "G":
                g += 1
            elif lst[k] == "H":
                h += 1
        
        if g == h or h == 0 or g == 0:
            max_val = max(max_val, abs(j-i))
        
print(max_val)