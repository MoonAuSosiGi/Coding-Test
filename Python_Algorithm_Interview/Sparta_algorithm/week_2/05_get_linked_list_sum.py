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

    def getNode(self,index):
        if index < 0:
            return None
        if index == 0:
            return self.head
        else:
            i = 0
            cur = self.head

            while i < index:
                cur = cur.next
                i += 1
            return cur




def get_linked_list_sum(linked_list_1, linked_list_2):
    index = 0
    sum1 = 0
    sum2 = 0
    while True:
        node1 = linked_list_1.getNode(index)
        node2 = linked_list_2.getNode(index)

        if node1 is not None and node2 is not None:
            sum1 = sum1 * 10 + node1.data
            sum2 = sum2 * 10 + node2.data
            index += 1
        else:
            break
    return sum1 + sum2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))