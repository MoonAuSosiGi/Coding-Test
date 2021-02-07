class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        if index < 0:
            return None
        i = 0
        cur = self.head
        while i < index:
            cur = cur.next
            i += 1
        return cur

    def add_node(self,index, value):
        if index < 0:
            return
        if index == 0:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        else:
            cur = self.get_node(index-1)
            if cur is not None:
                temp = cur.next
                new_node = Node(value)
                cur.next = new_node
                new_node.next = temp

    def delete_node(self, index):
        if index < 0:
            return
        if index == 0:
            temp = self.head.next
            self.head = temp
        else:
            cur = self.get_node(index-1)
            if cur is not None:
                temp = cur.next
                cur.next = temp.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.append(1)
linked_list.add_node(0,32)
linked_list.delete_node(0)
linked_list.print_all()