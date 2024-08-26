def shift(string):
    result = ""

    result = string[-1] + string[0:length - 1]
    return result

def RLE(string):             
    cnt = 1
    for i in range(length-1):
        if string[i] != string[i+1]:
            cnt += 1
    
    if cnt == 1 and length == 10:
        return 3
    return cnt * 2





string = input()
length = len(string)

ans = 20

for i in range(length):
    string = shift(string)
    ans = min(ans, RLE(string))

print(ans)