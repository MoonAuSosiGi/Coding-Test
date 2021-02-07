class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append(key,value)

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = [LinkedTuple()] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)].add(key, value)

    def get(self, key):
        self.items[hash(key) % len(self.items)].get(key)