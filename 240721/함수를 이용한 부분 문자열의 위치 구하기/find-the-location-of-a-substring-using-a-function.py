def check(str1, str2):
    for i in range(len(str1)):
        if str1[i:i+len(str2)] == str2:
            return i
    return -1

str1 = input()
str2 = input()

print(check(str1, str2))