def func(n):
    if n % 2 == 0 and (int(str(n)[0]) + int(str(n)[1])) % 5 == 0:
        print("Yes")
    else:
        print("No")

n = int(input())
func(n)