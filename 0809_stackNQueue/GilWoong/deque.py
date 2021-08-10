class Deque:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.q_list = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def push_front(self, item):
        try:
            if self.size >= self.capacity:
                raise Exception('큐가 가득 찼습니다.')
            
            self.front -= 1
            if self.front < 0:
                self.front = self.capacity - 1

            self.q_list[self.front] = item
            self.size += 1

        except Exception as e:
            print(e)

    def push_rear(self, item):
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
        
    def pop_front(self):
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

    def pop_rear(self):
        try:
            if self.size <= 0:
                raise Exception('큐가 비어있습니다.')
            
            self.rear -= 1
            if self.rear < 0:
                self.rear = self.capacity - 1

            pop_item = self.q_list[self.rear]
            self.size -= 1
                
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
    my_deque = Deque(5)
    print(my_deque)
    my_deque.push_front(1)
    print(my_deque)
    my_deque.push_front(2)
    print(my_deque)
    my_deque.push_front(3)
    print(my_deque)

    my_deque.push_rear(4)
    print(my_deque)
    my_deque.push_rear(5)
    print(my_deque)
    my_deque.push_rear(6)
    print(my_deque)

    print('--------------------------')

    print(f'pop : {my_deque.pop_rear()}')
    print(my_deque)
    print(f'pop : {my_deque.pop_rear()}')
    print(my_deque)
    print(f'pop : {my_deque.pop_rear()}')
    print(my_deque)

    print(f'pop : {my_deque.pop_front()}')
    print(my_deque)
    print(f'pop : {my_deque.pop_front()}')
    print(my_deque)
    print(f'pop : {my_deque.pop_front()}')
    print(my_deque)