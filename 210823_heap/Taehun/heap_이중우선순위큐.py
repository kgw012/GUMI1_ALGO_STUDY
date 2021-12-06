import heapq

# def solution(operations):
#     answer = []
#     heap = []
#     status = 0 # 0 : min 1 : max
#     for i in operations:
#         order, number = i.split()
#         number = int(number)
#         if order == 'I':
#             if status:
#                 heapq.heappush(heap, (-number, number))
#             else:
#                 heapq.heappush(heap, number)
#         # 최대 삭제
#         elif number == 1:
#             if heap:
#                 if status: # 최대 힙일때
#                     heapq.heappop(heap)
#                 else: #  최소 힙일때 전환 후 제거
#                     temp = []
#                     for i in heap:
#                         heapq.heappush(temp, (-i, i))
#                     heapq.heappop(temp)
#                     heap = temp
#                     status = 1
#
#         # 최소 삭제
#         elif number == -1:
#             if heap:
#                 if status: # 최대 힙일때
#                     temp = []
#                     for i in heap:
#                         heapq.heappush(temp, i[1])
#                     heapq.heappop(temp)
#                     heap = temp
#                     status = 0
#                 else:
#                     heapq.heappop(heap)
#
#
#     if not heap:
#         answer = [0,0]
#         return answer
#     elif len(heap) == 1:
#         if status:
#             answer = [heap[1], heap[1]]
#         else:
#             answer = [heap[0], heap[0]]
#         return answer
#     else:
#         if status:
#             max_value = heapq.heappop(heap)[1]
#             temp = []
#             for i in heap:
#                 heapq.heappush(temp, i[1])
#             min_value = heapq.heappop(temp)
#             answer = [max_value, min_value]
#             return answer
#         else:
#             min_value = heapq.heappop(heap)
#             temp = []
#             for i in heap:
#                 heapq.heappush(temp, (-i, i))
#             max_value = heapq.heappop(temp)[1]
#             answer = [max_value, min_value]
#             return answer

def solution(operations):
    max_heap = []
    min_heap = []
    for i in operations:
        order, number = i.split()
        number = int(number)
        if order == 'I':
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
    # 최대 삭제
        elif number == 1:
            if len(max_heap) < 1:
                continue
            a = heapq.heappop(max_heap)
            min_heap.remove(-a)
        else:
            if len(min_heap) < 1:
                continue
            a = heapq.heappop(min_heap)
            max_heap.remove(-a)

    if not min_heap:
        return [0,0]
    else:
        a = heapq.heappop(max_heap)
        b = heapq.heappop(min_heap)
        return [-a, b]


    return answer

operations = ["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]

a = solution(operations)
print(a)
