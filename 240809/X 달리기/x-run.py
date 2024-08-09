x = int(input())

speed = 1
time = 0

left = 0
right = x

while True:
    if left + speed < right - speed:
        left += speed
        right -= speed
        speed += 1
        time += 2
    elif left + speed <= right: #속도 하나 더 올려서 한 번만 더 가기
        left += speed
        time += 1
        break
    else:
        break

if left != right:
    time += 1
    
print(time)


'''
231 280 22
253 258

'''