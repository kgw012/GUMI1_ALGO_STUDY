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

    def set_valid(self, up_down):
        """삽입/삭제 후 heap 재배치, 자식노드가 부모노드보다 커야한다."""
        i = 0  # 삭제
        if up_down < 0:
            i = self.size  # 삽입

        while 1 <= i <= self.size:
            child = self.heap[i]
            if child >= self.heap[i // 2]:
                return
            else:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], child
            i += up_down

    def push(self, data):
        self.heap.append(data)
        self.size += 1
        self.set_valid(-1)

    def pop(self) -> int:
        try:
            if not self.size:
                raise Exception("비어있는 힙입니다.")
            if self.size == 1:
                return self.heap.pop()

            ret = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.size -= 1
            self.set_valid(1)
            return ret
        except Exception as e:
            print(f"에러발생 : {e}")
            return

    def monitor(self):
        pass


if __name__ == "__main__":
    test_data = [3, 5, 8, 0, 100, 35, 2, 17, 5]  # 5 중복

    min_heap = MinHeap()
    print("------------- push -------------")
    for data in test_data:
        min_heap.push(data)
    min_heap.monitor()

    print("------------- pop -------------")
    sorted_data = []
    for _ in range(min_heap.size):
        sorted_data.append(min_heap.pop())
    print(sorted_data)
