n = int(input())

print("* "*n)

for i in range(n-1): #줄 번호
    for j in range(1, i+2):   
        print("* ", end = "")
    for j in range(n-2-i, 0, -1):
        print("  ", end = "")
    print("*")