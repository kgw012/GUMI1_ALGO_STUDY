from collections import deque
def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    now_weight = 0
    time = 0
    while bridge:
        time += 1
        arrive = bridge.popleft()
        now_weight -= arrive
        if queue:
            if now_weight + queue[0] > weight:
                bridge.append(0)
            else:
                # 차량을 올림과 동시에 무게를 갱신
                truck = queue.popleft()
                now_weight += truck
                bridge.append(truck)

    return time

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)