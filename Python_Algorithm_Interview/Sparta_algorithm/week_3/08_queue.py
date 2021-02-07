class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        print(value, " ", self.is_empty())
        if self.is_empty():
            self.head = Node(value)
            self.head.next = self.tail
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            if self.head == self.tail:
                self.tail = None
            head = self.head
            self.head = head.next
        return head

    def peek(self):
        if self.is_empty():
            return None
        return self.head

    def is_empty(self):
        return self.head is None and self.tail is None

    def print_all(self):
        if self.is_empty() is False:
            cur = self.head
            while cur is not None:
                print(cur.data)
                cur = cur.next

test = Queue()
test.enqueue(3)
#test.enqueue(5)
#test.enqueue(6)
print("!!")
print(test.dequeue().data)
print("!!")
test.enqueue(8)
test.print_all()