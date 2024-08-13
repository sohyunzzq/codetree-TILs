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

ans = "Yes"
for c in string:
    if c == "(":
        s.push("(")
    else:
        if s.empty():
            ans = "No"
            break
        else:
            s.pop()

if s.empty() and ans != "No":
    ans = "Yes"
else:
    ans = "No"

print(ans)