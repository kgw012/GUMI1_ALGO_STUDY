class Queue:
    # 초기화
    def __init__(self):
        self.queue = []
        
    # Enqueue 기능 구현
    def Enqueue(self,a):
        self.queue(a)
        return 0
    
    # Dequeue 기능 구현
    def Dequeue(self):
        item_length = len(self.queue)
        if item_length < 1:
            print("큐가 비었습니다")
            return False
        #나오고 출력
        result = self.queue[0]
        del self.queue[0]
        return result
    
    # isEmpty 기능 구현
    def isEmpty(self):
        # True False로 반환
        return not self.queue


