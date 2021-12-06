# 프로그래머스 문제 '완주하지 못한 선수'
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    p_dict = dict()

    for player in participant:
        p_dict[player] = p_dict.get(player, 0) + 1

    for player in completion:
        p_dict[player] = p_dict[player] - 1

        if p_dict[player] == 0:
            del p_dict[player]

    answer = p_dict.popitem()[0]
    return answer


if __name__=='__main__':

    test_cases = [
        {
            'participant': ["leo", "kiki", "eden"],
            'completion': ["eden", "kiki"],
            'answer': "leo"
        },
        {
            'participant': ["marina", "josipa", "nikola", "vinko", "filipa"],
            'completion': ["josipa", "filipa", "marina", "nikola"],
            'answer': "vinko"
        },
        {
            'participant': ["mislav", "stanko", "mislav", "ana"],
            'completion': ["stanko", "ana", "mislav"],
            'answer': "mislav"
        }
    ]

    for test_case in test_cases:
        participant = test_case['participant']
        completion = test_case['completion']
        answer = test_case['answer']
        my_answer = solution(participant, completion)
        print(f'answer: {answer}, my_answer: {my_answer}')
        