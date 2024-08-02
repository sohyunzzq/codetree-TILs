n = int(input())

lst = [0] * 101
numlst = []
for i in range(n):
    num, alpha = input().split()
    lst[int(num)] = alpha
    numlst.append(int(num))

numlst.sort()
start=numlst[0]
end = numlst[n-1]

max_val = 0

if end - start == n - 1:
    max_val = max(max_val, end-start)

for i in range(start, end + 1):
    g, h = 0, 0
    for j in range(i, end + 1):
        if lst[j] == "G":
            g += 1
        elif lst[j] == "H":
            h += 1
        if (lst[j] == "G" or lst[j] == "H") and (lst[i] == "G" or lst[i] == "H") and g == h:
            max_val = max(max_val, abs(j-i))
        
print(max_val)