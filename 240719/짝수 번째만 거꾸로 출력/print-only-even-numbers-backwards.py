str1 = input()

result = ""

for i in range(len(str1)):
    if (i+1) % 2 == 0:
        result = str1[i] + result

print(result)