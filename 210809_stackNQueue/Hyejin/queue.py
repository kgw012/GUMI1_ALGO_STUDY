class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = -1
        self.q = [None] * size

    def enqueue(self, data):
        try:
            if self.is_full():
                raise Exception("큐가 가득찼습니다.")

            self.rear += 1
            self.q[self.rear] = data
            self.monitor()
        except Exception as e:
            print(f"에러 발생 : {e}")

    def dequeue(self):
        try:
            if self.is_empty():
                raise Exception("큐가 비어있습니다.")

            data = self.q[self.front]
            self.q[self.front] = None
            self.front += 1
            return data
        except Exception as e:
            print(f"에러 발생 : {e}")

    def peek(self):
        try:
            if self.is_empty():
                raise Exception("큐가 비어있습니다.")
            return self.q[self.front]
        except Exception as e:
            print(f"에러 발생 : {e}")

    def is_empty(self):
        if self.front == self.rear is None:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.size - 1:
            return True
        else:
            return False

    def monitor(self):
        print(self.q)


if __name__ == "__main__":
    q = Queue(5)  # 사이즈 5인 큐 생성

    print("----------- 삽입 -----------")
    print("비어있니? ", q.is_empty())
    q.enqueue("첫번째 원소")
    q.enqueue(2)
    q.enqueue(3)

    print("피크결과 ", q.peek())

    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print("가득 차있니? ", q.is_full())
    print()

    print("----------- 삭제 -----------")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("가득 차있니?", q.is_full())
    print(q.dequeue())
    print("피크결과 ", q.peek())
    print(q.dequeue())
    print(q.dequeue())
