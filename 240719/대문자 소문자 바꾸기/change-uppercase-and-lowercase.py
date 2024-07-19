str1 = input()

for i in str1:
    if i.isupper():
        print(i.lower(), end = "")
    else:
        print(i.upper(), end = "")