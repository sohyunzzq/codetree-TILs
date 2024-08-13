def heapify(lst, n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and lst[l] > lst[largest]:
        largest = l
    
    if r <= n and lst[r] > lst[largest]:
        largest = r
    
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

def heap_sort(lst, n):
    for i in range(n // 2, 0, -1):
        heapify(lst, n, i)
    
    for i in range(n, 1, -1):
        lst[1], lst[i] = lst[i], lst[1]
        heapify(lst, i-1, 1)

n = int(input())
tmp = list(map(int, input().split()))
lst = [0]
for i in range(n):
    lst.append(tmp[i])

heap_sort(lst, n)

for i in range(1, n+1):
    print(lst[i], end = " ")