class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if not self.items:
            return 1
        return 0

    def size(self):
        return len(self.items)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
       return self.items[-1]

s = Stack()

n = int(input())
for i in range(n):
    cmd = list(input().split())
    if len(cmd) >= 2:
        num = int(cmd[1])
    cmd = cmd[0]

    if cmd == "push":
        s.push(num)
    elif cmd == "pop":
        print(s.pop())
    elif cmd == "size":
        print(s.size())
    elif cmd == "empty":
        print(s.empty())
    else:
        print(s.top())