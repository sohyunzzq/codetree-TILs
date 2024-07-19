def is_leafyear(y):
    if y % 4 == 0 and not (y % 100 == 0 and y % 400 != 0):
        return True
    return False

y = int(input())

if is_leafyear(y):
    print("true")
else:
    print("false")