str1 = input()
str2 = input()
str3 = input()

lst = []
lst.append(len(str1))
lst.append(len(str2))
lst.append(len(str3))
lst.sort()

print(lst[2] - lst[0])