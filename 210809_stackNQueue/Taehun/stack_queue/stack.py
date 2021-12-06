class Stack:

    length = 0
    top = 0 
    stack = []
    full = False
    empty = False

    def __init__(self, length):
        self.length = length 
        self.stack = [0] * length


    def push(self, num):
        self.Full()
        if self.full == False:
            self.stack[self.top] = num
            self.top += 1
        else:
            print('overflow')


    def pop(self):
        self.Empty()
        if self.empty == False:
            data = self.stack[self.top -1]
            self.stack[self.top - 1] = 0
            self.top -= 1
            return data
        else:
            print('underflow')


    def Full(self):
        if self.top == self.length:
            self.full = True
            return True
        return False

    def Empty(self):
        if self.top == 0:
            self.empty = True
            return True
        return False

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.stack)
stack.push(6)
print(stack.stack)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.pop())
print(stack.stack)
stack.pop()
print(stack.stack)




