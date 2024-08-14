from collections import deque

dq = deque()

n = int(input())
for i in range(n):
    cmd = list(input().split())
    if len(cmd) >= 2:
        num = cmd[1]
    cmd = cmd[0]

    if cmd == "push_front":
        dq.appendleft(num)
    elif cmd == "push_back":
        dq.append(num)
    elif cmd == "pop_front":
        print(dq.popleft())
    elif cmd == "pop_back":
        print(dq.pop())
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        print(dq[0])
    else:
        print(dq[-1])