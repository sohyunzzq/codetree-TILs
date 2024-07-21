n, k, t = input().split()

lst = [input() for i in range(int(n))]
lst = [item for item in lst if item[0:len(t)] == t]
lst.sort()
print(lst[int(k)-1])