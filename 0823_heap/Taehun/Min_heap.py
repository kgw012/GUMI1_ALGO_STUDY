
class Heap:
    heap = []

    def __init__(self):
        self.heap = [0]

    def __str__(self):
        return str(self.heap[1])

    def insert(self, num):
        self.heap.append(num)
        self.sort()

    def delete(self):
        self.deletesort()

    def sort(self):
        now_index = len(self.heap) - 1
        now_value = self.heap[-1]
        while(1):
            parent_vaule = self.heap[(now_index) // 2]
            if now_index == 1:
                break
            # 부모 값보다 크면
            if now_value >= parent_vaule:
                break
            before_index = now_index
            now_index = (now_index) // 2
            self.heap[before_index] = parent_vaule
            self.heap[now_index] = now_value

    def deletesort(self):
        self.heap[1], self.heap[-1] = self.heap[-1] , self.heap[1]
        del self.heap[-1]
        now_index = 1
        while(1):
            left = now_index * 2
            right = (now_index * 2) + 1
            # 자식이 둘다 없는 경우
            if left > len(self.heap) - 1:
                break
            # 왼쪽 값만 있는 경우
            if right > len(self.heap) - 1:
                if self.heap[now_index] > self.heap[now_index * 2]:
                    self.heap[now_index], self.heap[now_index * 2] = self.heap[now_index * 2], self.heap[now_index]
                break
            # 둘다  있는 경우
            min_value = min(left, right)
            if self.heap[now_index] > self.heap[min_value]:
                if min_value == left:
                    self.heap[now_index], self.heap[now_index * 2] = self.heap[now_index * 2], self.heap[now_index]
                    now_index = now_index * 2
                else:
                    self.heap[now_index], self.heap[(now_index * 2) - 1] = self.heap[(now_index * 2) - 1], self.heap[
                        now_index]
                    now_index = (now_index * 2) - 1

    def view(self):
        return self.heap[1:]




heap = Heap()
heap.insert(13)
heap.insert(25)
heap.insert(11)
heap.insert(8)
heap.insert(17)
heap.delete()

array = heap.view()
print(array)
print(heap)