# 프로그래머스 문제 '위장'
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):

    cloth_dict = dict()

    for name, kind in clothes:
        cloth_dict[kind] = cloth_dict.get(kind, 0) + 1
    
    answer = 1
    for cloth_len in cloth_dict.values():
        answer *= (cloth_len + 1)

    return answer - 1


if __name__=='__main__':

    test_cases = [
        {
            'clothes': [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
            'answer': 5 
        },
        {
            'clothes': [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]],
            'answer': 3
        }
    ]
    
    for test_case in test_cases:
        clothes = test_case['clothes']
        answer = test_case['answer']
        my_answer = solution(clothes)

        print(f'answer: {answer}, my_answer: {my_answer}')