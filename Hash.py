class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        new_hash = 0
        for letter in key:
            new_hash = (new_hash + ord(letter) * 23) % len(self.data_map)
        return new_hash

    def all(self):
        for i, j in enumerate(self.data_map):
            print(i, ':', j)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        # return self.all()

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        keys = []
        if self.data_map is None:
            return None
        for i in self.data_map:
            if i is not None:
                keys.append(i[0][0])
        return keys

hashh = HashTable()
# hashh.all()
print('----new----')
hashh.set_item('item1', 1)
hashh.set_item('item2', 2)
hashh.set_item('item3', 3)
# hashh.all()

# print(hashh.get_item('item3'))
# print(hashh.get_item('item4'))
print(hashh.keys())
