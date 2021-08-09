class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.lst = [0] * size

    def push(self, data):
        try:
            self.top += 1
            self.lst[self.top] = data
            self.lst_print()
        except IndexError as e:
            self.top -= 1
            print(f"오버플로우 발생 : {e}")

    def pop(self):
        try:
            data = self.lst[self.top]
            self.lst[self.top] = 0
            self.top -= 1
            return data
        except IndexError as e:
            print("top ", self.top)
            print(f"언더플로우 발생 : {e}")

    def is_full(self):
        if self.size == self.top + 1:
            return True
        else:
            return False

    def is_empty(self):
        if not self.top:
            return True
        else:
            return False

    def lst_print(self):
        print(self.lst)


if __name__ == "__main__":
    print("size = 5 인 스택 인스턴스 생성")
    stack = Stack(5)
    print("--------")
    print("push")
    stack.push(3)
    stack.push(10)
    stack.push(4)
    stack.push("hi")
    stack.push("bye")
    stack.push("err")
    print("--------")
    print("비어있는지 확인 ", end=" ")
    flag = stack.is_empty()
    print(flag)
    print("--------")
    print("가득 차있는지 확인", end=" ")
    flag = stack.is_full()
    print(flag)
    print("--------")
    for _ in range(2):
        print("pop ", stack.pop())
