from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push_front(self, item):
        self.dq.appendleft(item)
    
    def push_back(self, item):
        self.dq.append(item)
    
    def empty(self):
        if not self.dq:
            return 1
        return 0
    
    def pop_front(self):
        return self.dq.popleft()
    
    def pop_back(self):
        return self.dq.pop()

    def size(self):
        return len(self.dq)
    
    def front(self):
        return self.dq[0]

    def back(self):
        return self.dq[-1]

dq = Queue()
n = int(input())
for i in range(n):
    cmd = list(input().split())
    if len(cmd) >= 2:
        num = cmd[1]
    cmd = cmd[0]

    if cmd == "push_front":
        dq.push_front(num)
    elif cmd == "push_back":
        dq.push_back(num)
    elif cmd == "pop_front":
        print(dq.pop_front())
    elif cmd == "pop_back":
        print(dq.pop_back())
    elif cmd == "size":
        print(dq.size())
    elif cmd == "empty":
        print(dq.empty())
    elif cmd == "front":
        print(dq.front())
    else:
        print(dq.back())