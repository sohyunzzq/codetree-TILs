from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def pop(self):
        return self.dq.popleft()

    def size(self):
        return len(self.dq)

q = Queue()

n, k = map(int, input().split())
for i in range(1, n+1):
    q.push(i)

while q.size() != 1:
    for i in range(k-1):
        q.push(q.pop())
    print(q.pop(), end = " ")
print(q.pop())