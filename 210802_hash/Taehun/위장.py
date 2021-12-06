def solution(clothes):
    cloth_dict = {}
    # 딕셔너리에 추가 
    for cloth in clothes:
        if cloth[1] not in cloth_dict.keys():
            cloth_dict[cloth[1]] = [cloth[0]]
        else:
            cloth_dict[cloth[1]].append(cloth[0])

    answer = 1

    # 경우의 수 구한 후 아무것도 안 입는 경우를 제외해야하니 -1을 해줌 
    # 만약 경우가 하나라면 바로 갯수를 리턴함 
    for num in cloth_dict.keys():
        if (len(cloth_dict)) == 1 :
            answer = len(cloth_dict[num])
            return answer
        else:
            answer *= (len(cloth_dict[num]) + 1)
    answer -= 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))