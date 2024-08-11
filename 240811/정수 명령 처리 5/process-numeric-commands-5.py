n = int(input())
lst = []
for i in range(n):
    cmd = list(input().split())
    if len(cmd) == 2:
        num = int(cmd[1])
    cmd = cmd[0]
    
    if cmd == "push_back":
        lst.append(num)
    elif cmd == "pop_back":
        lst.pop()
    elif cmd == "size":
        print(len(lst))
    else:
        print(lst[num-1])