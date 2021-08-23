from queue import Queue


class Circle_Queue(Queue):
    def __init__(self, size: int) -> None:
        super().__init__(size=size + 1)
        self.rear = self.front

    def enqueue(self, data):
        try:
            if self.is_full():
                raise Exception("큐가 가득찼습니다.")

            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = data
            self.monitor()
        except Exception as e:
            print(f"에러 발생 : {e}")

    def dequeue(self):
        try:
            if self.is_empty():
                raise Exception("큐가 비어있습니다.")

            self.front = (self.front + 1) % self.size
            data = self.q[self.front]
            self.q[self.front] = None
            return data
        except Exception as e:
            return f"에러 발생 : {e}"

    def peek(self):
        try:
            if self.is_empty():
                raise Exception("큐가 비어있습니다.")
            return self.q[self.front + 1]
        except Exception as e:
            print(f"에러 발생 : {e}")

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if self.front == (self.rear + 1) % self.size:
            return True
        else:
            return False


if __name__ == "__main__":
    q = Circle_Queue(5)
    print("----------- 삽입 -----------")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    print("\n----------- 피크 -----------")
    print(q.peek())
    print("\n----------- 삭제 -----------")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
