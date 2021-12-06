class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.clear()

    def clear(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == self.tail is None:
            return True
        return False

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
            return

        if data < self.head.data:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return

        if self.tail.data <= data:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            return

        tmp = self.head.next
        while True:
            if data < tmp.data:
                node.prev = tmp.prev
                node.next = tmp
                tmp.prev = node
                tmp.prev.next = node
                return
            tmp = tmp.next

    def delete(self, flag="max"):
        if self.is_empty():
            return

        if self.head == self.tail:
            ret = self.head.data
            self.clear()
            return ret

        if flag == "min":
            ret = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return ret
        elif flag == "max":
            ret = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return ret

    def show(self):
        if self.is_empty():
            print("비어있습니다.")
            return

        tmp = self.head
        while True:
            print(tmp.data, end=" ")
            if tmp.next is None:
                break
            tmp = tmp.next
        print()
        return


def solution(operations):
    linkedlist = LinkedList()
    for operation in operations:
        op, num = operation.split()

        if op == "I":  # 삽입
            linkedlist.append(int(num))
        else:  # 삭제
            if num == "1":  # 최댓값
                linkedlist.delete()
            else:
                linkedlist.delete("min")
        # print("출력 : ", end="")
        # linkedlist.show()

    if linkedlist.is_empty():
        return [0, 0]

    M, m = linkedlist.tail.data, linkedlist.head.data
    return [M, m]


if __name__ == "__main__":
    # operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    s = solution(operations)
    print(s)
