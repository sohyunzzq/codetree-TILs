from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def empty(self):
        if not self.dq:
            return 1
        return 0

    def pop(self):
        return self.dq.popleft()

    def size(self):
        return len(self.dq)

    def front(self):
        return self.dq[0]

q = Queue()

n = int(input())
for i in range(n):
    cmd = list(input().split())
    if len(cmd) >= 2:
        num = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        q.push(num)
    elif cmd == "pop":
        print(q.pop())
    elif cmd == "size":
        print(q.size())
    elif cmd == "empty":
        print(q.empty())
    else:
        print(q.front())