x = int(input())

speed = 1
time = 0

left = 0
right = x

#양쪽에서 좁혀가기
#만약 속도를 더 높였을 때
#왼쪽은 갈 수 있고 오른쪽은 못 가면, 왼쪽이라도 가기
#부딪히면 그냥 나오고, 나머지 거리를 가기 위해 +1

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