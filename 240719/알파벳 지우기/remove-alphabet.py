str1 = input()
str2 = input()

num1 = ""
num2 = ""

for i in str1:
    if i.isdigit():
        num1 += i

for i in str2:
    if i.isdigit():
        num2 += i

print(int(num1) + int(num2))