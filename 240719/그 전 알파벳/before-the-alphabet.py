abc = "abcdefghijklmnopqrstuvwxyz"

alpha = input()

for i in range(len(abc)):
    if alpha == abc[i]:
        if i < 0:
            i += 26
        print(abc[i-1])
        break