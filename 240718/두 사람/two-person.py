lst1 = list(input().split())
lst2 = list(input().split())

if (int(lst1[0]) >= 19 and lst1[1] == "M") or (int(lst2[0]) >= 19 and lst2[1] == "M"):
    print("1")
else:
    print("0")