def alpha(str1):
    dict1 = {}

    for i in str1:
        if str1 in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 0

    if len(dict1) >= 2:
        return True
    return False

A = input()
if alpha(A):
    print("Yes")
else:
    print("No")