binary = input()

decimal = 0

for i in range(len(binary)):
    decimal = decimal * 2 + int(binary[i])

print(decimal)