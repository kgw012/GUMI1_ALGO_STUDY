import random

class hash:
    def __init__(self, num):
        self.hashTable = [None] * num
    # key 값을 넣는 과정 임의 hash화 거쳐서 그 값을 반환
    def hash_function(self, key): 
        if type(key) != int:
            key = ord(key)
        return key % 9


    # 값을 넣을 때 만약 key 값의 dix가 값이 이미 존재한다면 none 인 부분까지 반복문을 돌려
    # 가장 가까운 None에 값을 넣는다 : Linear Probing  기법
    def insert(self, key, value): 
        hash_key = self.hash_function(key) 
        if self.hashTable[hash_key] == None:
            self.hashTable[hash_key] = value
        else:
            for idx in range( self.hashTable.index(hash_key) + 1 ,len(self.hashTable)):
                if self.hashTable[idx] == None:
                    self.hashTable[idx] = value
                    break

    # 읽어오는 과정 
    def read(self, key): 
        value = self.hash_function(key)
        return value

    # 내부 요소를 검사 후 있다면 삭제 
    def remove(self, key): 
        hash_key = self.hash_function(key)
        if self.hashTablep[hash_key]:
            self.hashTablep[hash_key] = None
            return True
        else:
            return False
        
    
    def print(self):
        print(self.hashTable)
    
temp= hash(20)
temp.insert(1, 1)
temp.print()
temp.insert(2, 2)
temp.print()
temp.insert(3, 3)
temp.print()
temp.insert(4, 4)
temp.print()
temp.insert(11, 5)
temp.print()
