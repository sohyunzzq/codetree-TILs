n, k, t = input().split()
n = int(n)
k = int(k)

lst = []
for i in range(n):
    string = input()

    if len(string) >= len(t) and string[0:len(t)] == t:
        lst.append(list(string))

lst.sort()

for item in lst[k-1]:
    print(item, end = "")