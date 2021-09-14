class Node:
    def __init__(self, value, p_node, c_node):
        self.value = value
        self.p_node = p_node
        self.c_node = c_node


def solution(operations):
    min_node = None
    max_node = None
    size = 0
    for operation in operations:
        op = operation.split()
        cmd, num = op[0], int(op[1])

        if cmd == 'I':
            size += 1

            if min_node is None:
                node = Node(num, None, None)
                min_node = node
                max_node = node
                continue

            else:
                # 최소 노드부터 순환 시작
                node = min_node

                while True:
                    # 끝까지 갔는데 더 큰 노드가 없을 때(본인이 최대노드)
                    if node is None:
                        new_node = Node(num, max_node, None)
                        max_node.c_node = new_node

                        max_node = new_node
                        break
                    
                    if node.value >= num:
                        # 처음부터 더 큰 노드를 만났을 때(본인이 최소노드)
                        if node.value == min_node.value:
                            new_node = Node(num, None, min_node)
                            min_node.p_node = new_node

                            min_node = new_node
                            break
                        
                        # 중간에서 더 큰 노드를 만났을 때
                        new_node = Node(num, node.p_node, node)

                        # 원래 부모노드의 자식노드로 삽입
                        node.p_node.c_node = new_node

                        # 현재 노드의 부모노드로 삽입
                        node.p_node = new_node
                        break
                    
                    # 어떤 경우도 아닐 때 다음 노드로 이동
                    node = node.c_node
                    
        else:
            if size == 0:
                continue


            if size == 1:
                min_node = max_node = None
                size = 0
                continue

            size -= 1

            if num > 0:
                max_node.p_node.c_node = None
                max_node = max_node.p_node
            else:
                min_node.c_node.p_node = None
                min_node = min_node.c_node
    
    if size == 0:
        answer = [0, 0]
    else:
        answer = [max_node.value, min_node.value]
    return answer


if __name__ == '__main__':
    operations = ["I 16","D 1"]
    print(solution(operations))