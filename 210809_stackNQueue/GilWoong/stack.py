class Stack:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_list = [None] * capacity
        self.top = 0

    def push(self, item):
        try:
            if self.top >= self.capacity:
                raise Exception('스택이 가득 찼습니다.')
            
            self.stack_list[self.top] = item
            self.top += 1
        except Exception as e:
            print('예외발생 : ', e)

    def pop(self):
        try:
            if self.top == 0:
                raise Exception('스택이 비었습니다.')

            self.top -= 1
            pop_item = self.stack_list[self.top]
            return pop_item

        except Exception as e:
            print('예외발생 : ', e)

    def showItems(self):
        print(self.stack_list[:self.top])


my_stack = Stack(5)
my_stack.showItems()
my_stack.push(1)
my_stack.showItems()
my_stack.push(2)
my_stack.showItems()
my_stack.push(3)
my_stack.showItems()

my_stack.push(4)
my_stack.showItems()
my_stack.push(5)
my_stack.showItems()
my_stack.push(6)
my_stack.showItems()

print('--------------------------')

print(f'pop : {my_stack.pop()}')
my_stack.showItems()
print(f'pop : {my_stack.pop()}')
my_stack.showItems()
print(f'pop : {my_stack.pop()}')
my_stack.showItems()

print(f'pop : {my_stack.pop()}')
my_stack.showItems()
print(f'pop : {my_stack.pop()}')
my_stack.showItems()
print(f'pop : {my_stack.pop()}')
my_stack.showItems()