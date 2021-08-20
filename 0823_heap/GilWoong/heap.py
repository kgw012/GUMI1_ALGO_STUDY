class Heap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, item):
        if len(self.heap) == 1:
            self.heap.append(item)
            return
        
        self.heap.append(item)

        idx = len(self.heap) - 1

        while idx != 1:
            if self.heap[idx] >= self.heap[idx // 2]:
                break
            
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx //= 2
        
        return
    
    def pop(self):
        if len(self.heap) == 1:
            raise Exception('힙이 비었습니다.')
            return
        
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        pop_item = self.heap.pop()

        idx = 1
        while True:
            if 2*idx >= len(self.heap):
                break
            
            if 2*idx + 1 >= len(self.heap):
                if self.heap[idx] <= self.heap[2*idx]:
                    break
                else:
                    self.heap[idx], self.heap[2*idx] = self.heap[2*idx], self.heap[idx]
                    continue

            min_value, min_idx = min((self.heap[idx], idx), (self.heap[2*idx], 2*idx), (self.heap[2*idx + 1], 2*idx + 1))

            if min_value == self.heap[idx]:
                break

            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            idx = min_idx

        return pop_item
    
    def __repr__(self) -> str:
        return str(self.heap[1:])


if __name__ == '__main__':
    heap = Heap()

    lst = [5, 3, 4, 6, 8, 1, 2, 7]

    for num in lst:
        heap.push(num)
    
    print(heap)

    for _ in range(len(lst)):
        print(heap.pop(), end=' ')

    print()
    
    try:
        heap.pop()
    except Exception as e:
        print(e)
