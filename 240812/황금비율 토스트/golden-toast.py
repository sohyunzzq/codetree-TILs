class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, ndata):
        new_node = Node(ndata)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
    
    def push_back(self, ndata):
        if self.begin() == self.end():
            self.push_front(ndata)
        
        else:
            new_node = Node(ndata)
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev = new_node
    
    def erase(self, node):
        if node == self.begin(): #head 삭제
            tmp = self.head
            self.head.next.prev = None
            self.head = self.head.next
            tmp.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
    
    def insert(self, node, ndata):
        if node == self.begin():
            self.push_front(ndata)
        elif node == self.end():
            self.push_back(ndata)
        else:
            new_node = Node(ndata)
            node.prev.next = new_node
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
    
    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

n, m = map(int, input().split())
bread = input()

DLL = DoublyLinkedList()
it = DLL.begin()

for i in range(n):
    DLL.push_back(bread[i])

while it != DLL.end():
    it = it.next

for i in range(m):
    cmd = list(input().split())
    if len(cmd) >= 2:
        c = cmd[1]
    cmd = cmd[0]
    
    if cmd == "L": #앞으로 가기
        if it != DLL.begin():
            it = it.prev
    elif cmd == "R":
        if it != DLL.end():
            it = it.next
    elif cmd == "D":
        if it != DLL.end():
            DLL.erase(it)
    else:
        DLL.insert(it, c)

it = DLL.begin()
while it != DLL.end():
    print(it.data, end = "")
    it = it.next