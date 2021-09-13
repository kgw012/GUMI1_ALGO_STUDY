class Queue:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.q_list = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = 0


    def push(self, item):
        try:
            if self.size >= self.capacity:
                raise Exception('큐가 가득 찼습니다.')

            self.q_list[self.rear] = item
            self.rear += 1
            self.size += 1
            if self.rear >= self.capacity:
                self.rear = 0

        except Exception as e:
            print(e)
        

    def pop(self):
        try:
            if self.size <= 0:
                raise Exception('큐가 비어있습니다.')
            
            pop_item = self.q_list[self.front]
            self.front += 1
            self.size -= 1

            if self.front >= self.capacity:
                self.front = 0
                
            return pop_item

        except Exception as e:
            print(e)


    def __repr__(self):
        repr_list = []

        if self.size > self.rear:
            repr_list = self.q_list[self.front:]
            repr_list.extend(self.q_list[:self.rear])
        else:
            repr_list = self.q_list[self.front:self.rear]

        return str(repr_list)


if __name__=='__main__':
    my_queue = Queue(5)
    print(my_queue)
    my_queue.push(1)
    print(my_queue)
    my_queue.push(2)
    print(my_queue)
    my_queue.push(3)
    print(my_queue)

    my_queue.push(4)
    print(my_queue)
    my_queue.push(5)
    print(my_queue)
    my_queue.push(6)
    print(my_queue)

    print('--------------------------')

    print(f'pop : {my_queue.pop()}')
    print(my_queue)
    print(f'pop : {my_queue.pop()}')
    print(my_queue)
    print(f'pop : {my_queue.pop()}')
    print(my_queue)

    print(f'pop : {my_queue.pop()}')
    print(my_queue)
    print(f'pop : {my_queue.pop()}')
    print(my_queue)
    print(f'pop : {my_queue.pop()}')
    print(my_queue)