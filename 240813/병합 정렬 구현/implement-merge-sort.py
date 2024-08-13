def merge(lst, low, mid, high): #[low, mid], [mid + 1, high] 두 개 합치기
    i = low
    j = mid + 1

    merged = []
    while i <= mid and j <= high: #각자 자신의 범위 안에 있을 때
        if lst[i] <= lst[j]:
            merged.append(lst[i])
            i += 1
        else:
            merged.append(lst[j])
            j += 1
    
    while i <= mid: #오른쪽 끝나고 왼쪽은 남음
        merged.append(lst[i])
        i += 1
    
    while j <= high:
        merged.append(lst[j])
        j += 1
    
    for i in range(low, high+1):
        lst[i] = merged[i-low]

def merge_sort(lst, low, high):
    if low < high: #원소가 2개 이상일 때
        mid = (low + high) // 2
        merge_sort(lst, low, mid) #왼쪽
        merge_sort(lst, mid + 1, high) #오른쪽
        
        merge(lst, low, mid, high)

n = int(input())
lst = list(map(int, input().split()))

merge_sort(lst, 0, n-1)

for num in lst:
    print(num, end = " ")