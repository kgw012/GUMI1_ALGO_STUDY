lst = [3, 7, 5, 2, 1, 9]

class queue():

    def __init__(self):
        self.queue = []
        self.rear = 0
        self.front = 0

    def enqueue(self, x):
        self.queue.append(x)
        self.rear += 1

    def dequeue(self):
        value = self.queue[self.front]
        self.front += 1
        return value

    def is_empty(self):
        if self.rear - self.front == 0:
            return True
        return False

    def __len__(self):
        return self.rear - self.front

a = queue()

for i in lst:
    a.enqueue(i)
    print('enqueue {}'.format(a.queue))

for i in range(3):
    ret = a.dequeue()
    print('dequeue {}'.format(ret))

print('len : {}'.format(len(a)))