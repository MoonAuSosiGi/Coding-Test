class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        cur_index = len(self.items)-1
        self.items[cur_index], self.items[1] = self.items[1], self.items[cur_index]
        cur_index = 1
        root = self.items.pop()
        item_size = len(self.items)
        while cur_index <= item_size -1:
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1

            if left_index >= item_size or right_index >= item_size:
                break

            cur = self.items[cur_index]
            left = self.items[left_index]
            right = self.items[right_index]

            if left > cur and right > cur:
                if left > right:
                    self.items[cur_index], self.items[left_index] = self.items[left_index], self.items[cur_index]
                    cur_index = left_index
                else:
                    self.items[cur_index], self.items[right_index] = self.items[right_index], self.items[cur_index]
                    cur_index = right_index
            elif left > cur:
                self.items[cur_index], self.items[left_index] = self.items[left_index], self.items[cur_index]
                cur_index = left_index
            elif right > cur:
                self.items[cur_index], self.items[right_index] = self.items[right_index], self.items[cur_index]
                cur_index = right_index
            else:
                break



        # 구현해보세요!
        return root  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]