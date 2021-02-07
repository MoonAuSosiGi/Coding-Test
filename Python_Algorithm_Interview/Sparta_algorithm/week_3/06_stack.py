class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return None
        else:
            result_node = self.head
            self.head = result_node.next
            return result_node

    def peek(self):
        return self.head

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


stack = Stack()
if stack.is_empty():
    print("empty")
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)
if stack.is_empty():
    print("empty")
#stack.pop()
stack.push(500)
stack.push(600)

stack.print_all()