str1 = input()
index = str1.find("e")

str1 = str1[0:index] + str1[index+1:len(str1)]
print(str1)