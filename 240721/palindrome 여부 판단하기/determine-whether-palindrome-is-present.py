def ispalindrome(str1):
    if str1[0:len(str1)] == str1[0:len(str1)][::-1]:
        return True
    return False

str1 = input()
if ispalindrome(str1):
    print("Yes")
else:
    print("No")