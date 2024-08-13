class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1]

    def empty(self):
        return not self.items

s = Stack()

string = input()

for c in string:
    if c == "(":
        s.push("(")
    else:
        if s.empty():
            print("No")
            break
        else:
            s.pop()

if s.empty():
    print("Yes")
else:
    print("No")