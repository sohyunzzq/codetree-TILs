def shift(string):
    result = ""

    result = string[-1] + string[0:length - 1]
    return result

def RLE(string):             
    cnt = 1
    for i in range(length-1):
        if string[i] != string[i+1]:
            cnt += 1
    
    return cnt * 2





string = input()
length = len(string)

ans = RLE(string)

if length == 10:
    for i in range(length-1):
        if string[i] == string[i+1]:
            continue
        else:
            break
        
        ans = 3

for i in range(length - 1):
    string = shift(string)
    ans = min(ans, RLE(string))

print(ans)