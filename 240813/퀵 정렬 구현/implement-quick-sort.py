def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1

def quick_sort(lst, low, high):
    if low < high:
        pos = partition(lst, low, high)

        quick_sort(lst, low, pos - 1)
        quick_sort(lst, pos + 1, high)

n = int(input())
lst = list(map(int, input().split()))

quick_sort(lst, 0, n-1)

for num in lst:
    print(num, end = " ")