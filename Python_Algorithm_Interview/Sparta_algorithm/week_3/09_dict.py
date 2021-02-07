
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value
        return

    def get(self, key):
        return self.items[hash(key) % len(self.items)]


test_dict = Dict()
test_dict.put("test",5)
print(test_dict.get("test"))