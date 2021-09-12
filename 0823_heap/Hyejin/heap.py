class Heap:
    """
    최솟값/최댓값 이라는 특정 기준을 만족시키는 완전이진트리

    cf. 완전이진트리
    자식노드가 최대 2개이면서 노드가 왼쪽부터 빈틉없이 채워진 트리
    """

    def __init__(self):
        self.heap = [0]  # 루트노드를 인덱스 1로 설정
        self.size = 0


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def set_valid(self, heap_pop=True):
        """삽입/삭제 후 heap 재배치, 자식노드가 부모노드보다 커야한다."""
        if not heap_pop:  # 삽입
            i = self.size
            while 1 <= i <= self.size:
                child = self.heap[i]
                if child >= self.heap[i // 2]:
                    return
                else:
                    self.heap[i], self.heap[i // 2] = self.heap[i // 2], child
                    i //= 2
        else:  # 삭제
            i = 1
            while True:
                min_data, idx = self.heap[i], i  # 좌/우 노드 중 더 작은 값과 교체예정
                swap = False
                if 1 <= i * 2 <= self.size and self.heap[i * 2] < self.heap[idx]:
                    min_data, idx = self.heap[i * 2], i * 2
                    swap = True

                if 1 <= i * 2 + 1 <= self.size and self.heap[i * 2 + 1] < self.heap[idx]:
                    min_data, idx = self.heap[i * 2 + 1], i * 2 + 1
                    swap = True

                if not swap:
                    # 자식노드보다 부모노드가 작거나 같다면
                    return

                self.heap[i], self.heap[idx] = self.heap[idx], self.heap[i]
                i = idx

    def push(self, data):
        self.heap.append(data)
        self.size += 1
        self.set_valid(False)
        self.monitor(data)

    def pop(self) -> int:
        try:
            if not self.size:
                raise Exception("비어있는 힙입니다.")
            if self.size == 1:
                return self.heap.pop()

            ret = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.size -= 1
            self.set_valid()
            return ret
        except Exception as e:
            print(f"에러발생 : {e}")
            return

    def monitor(self, data):
        print(data, self.heap)


if __name__ == "__main__":
    test_data = [3, 5, 8, 0, 100, 35, 2, 17, 5]  # 5 중복

    min_heap = MinHeap()
    print("------------- push -------------")
    for data in test_data:
        min_heap.push(data)

    print("------------- pop -------------")
    sorted_data = []
    for _ in range(min_heap.size):
        sorted_data.append(min_heap.pop())
    print(sorted_data)
