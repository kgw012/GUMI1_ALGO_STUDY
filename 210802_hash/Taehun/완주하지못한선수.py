def solution(participant, completion):
    parti_dict = {}
    answer = ''

    for i in participant:
        if i not in parti_dict.keys():
            parti_dict[i] = 1
        else:
            parti_dict[i] += 1

    for j in completion:
        parti_dict[j] -= 1

    for x in parti_dict.keys():
        if parti_dict[x] > 0:
            answer += x
    
    return answer





# print(f'{}는 참여자 명단에는 있지만, 완주자 명단에는 없기 땜문에 완주하지 못했습니다.')