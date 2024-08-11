class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, ndata):
        new_node = Node(ndata)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.node_num += 1
    
    def push_back(self, ndata):
        new_node = Node(ndata)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.node_num += 1
    
    def pop_front(self):
        if self.head.next == None:
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        else:
            temp = self.head

            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1

            return temp.data
    
    def pop_back(self):
        if self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        else:
            temp = self.tail
            
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1

            return temp.data
    
    def size(self):
        return self.node_num
    
    def empty(self):
        if not self.node_num:
            return 1
        return 0
            
    def front(self):
        return self.head.data
    
    def back(self):
        return self.tail.data

n = int(input())

dll = DLL()
for i in range(n):
    cmd = list(input().split())
    if len(cmd) == 2:
        num = cmd[1]
    cmd = cmd[0]

    if cmd == "push_front":
        dll.push_front(num)
    elif cmd == "push_back":
        dll.push_back(num)
    elif cmd == "pop_front":
        print(dll.pop_front())
    elif cmd == "pop_back":
        print(dll.pop_back())
    elif cmd == "size":
        print(dll.size())
    elif cmd == "empty":
        print(dll.empty())
    elif cmd == "front":
        print(dll.front())
    else:
        print(dll.back())