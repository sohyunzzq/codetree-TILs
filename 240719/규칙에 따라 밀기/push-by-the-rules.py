str1 = input()
cmd = input()

for i in cmd:
    if i == "L": #왼쪽
        str1 = str1[1:len(str1)] + str1[0]
    else:
        str1 = str1[len(str1)-1] + str1[0:len(str1)-1]

print(str1)