def solution(genres, plays):
    genres_dict = {}
    sort_album_dict ={}
    result_ls = []
    idx = 0
    #장르 sort
    for key in genres:
        if key not in genres_dict.keys():
            genres_dict[key] =plays[idx]
            idx += 1
        else:
            genres_dict[key] += plays[idx]
            idx += 1
    genres_dict = dict(reversed(sorted(genres_dict.items(), key=lambda x: x[1])))

    #장르 내부값 sort
    idx = 0
    for key in genres:
        if key not in sort_album_dict.keys():
            sort_album_dict[key] = [[idx, plays[idx]]]
            idx += 1
        else:
            sort_album_dict[key].append([idx, plays[idx]])
            idx += 1
    for key in sort_album_dict.keys():
        sort_album_dict[key] = list(reversed(sorted(sort_album_dict[key], key=lambda x : x[1])))


    #전체 sort된 dict 만들기
    for key in genres_dict.keys():
        genres_dict[key] =sort_album_dict[key]
        if len(genres_dict) == 1:
            result_ls.append(genres_dict[key][0][0])
        else:
            for i in range(2):
                result_ls.append(genres_dict[key][i][0])
    return  result_ls

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))










#####

