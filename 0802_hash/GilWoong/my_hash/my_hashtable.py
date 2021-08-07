class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __repr__(self):
        return f'({self.key}, {self.value})'

class MyHashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = list([None for i in range(capacity)])

    def hash_func(self, key):
        key = hash(key)
        return key % self.capacity

    def put(self, key, value):
        kv = KeyValue(key, value)
        idx = self.hash_func(key)
        if self.hash_table[idx] == None:
            self.hash_table[idx] = kv
            return True
        else:
            for i in range(idx, self.capacity):
                if self.hash_table[i] == None:
                    self.hash_table[i] = kv
                    return True
                if self.hash_table[i].key == key:
                    self.hash_table[i] = kv
                    return True
            print('공간이 부족합니다.')
            return False

    def get(self, key):
        idx = self.hash_func(key)
        for i in range(idx, self.capacity):
            if self.hash_table[i].key == key:
                return self.hash_table[i].value
        return None

    def remove(self, key):
        hash_value = self.hash_func(key)
        if self.hash_table[hash_value]:
            self.hash_table[hash_value] = None
            return True
        else:
            return False

    def print_table(self):
        print(self.hash_table)