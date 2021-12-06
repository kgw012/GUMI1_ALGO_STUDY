MAX_QSIZE = 10
class CircularQueue :
    def __init__(self):
        self.front = 0
        self.rear = 0
        # 초기화 빈 리스트로 
        self.items = [None] * MAX_QSIZE

        # front와 rear 가같으면 비었다. 
    def isEmpty(self):
        return self.front == self.rear

        # fornt가 real의 인덱스오ㅓㅏ 
    def isFull(self):
        return self.front == (self.rear+1)%MAX_QSIZE

        #다시 초기화 시킴
    def clear(self):
        self.front = self.rear
    
    def __len__(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]


    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    
    def print(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]

        print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)

class CircularDeque(CircularQueue):
    
    def __init__(self):
        super().__init__()

    def addRear (self, item):
        self.enqueue(item)

    def deleteFront (self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + MAX_QSIZE) % MAX_QSIZE

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear - 1 + MAX_QSIZE) % MAX_QSIZE
            return item

    def getRear(self):
        return self.items[self.rear]
