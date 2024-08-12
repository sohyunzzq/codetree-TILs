n = int(input())
lst = list(map(int, input().split()))

maxi = max(lst)
leng = len(str(maxi))

for i in range(n):
    lst[i] = str(lst[i])

for i in range(1, leng+1):
    arr = []
    for j in range(10):
        arr.append([])
    
    for j in range(n):
        if i > len(lst[j]):
            num = 0
        else:
            num = int(lst[j][-i])
        arr[num].append(lst[j])
    
    tmp = []
    for j in range(10):
        for k in range(len(arr[j])):
            tmp.append(arr[j][k])
    
    lst = tmp

for i in range(n):
    print(int(lst[i]), end = " ")

'''

function radix_sort(arr, k)
  for pos = k - 1 ... pos >= 0:
    set arr_new = [10][]
    for i = 0 ... i < arr.size
      set digit = posth digit of arr[i]
      arr_new[digit].append(arr[i])

    set store_arr = []
    for i = 0 ... i < 10
      for j = 0 ... j < arr_new[i].size
        store_arr.append(arr_new[i][j])
  
    arr = store_arr

  return arr
'''