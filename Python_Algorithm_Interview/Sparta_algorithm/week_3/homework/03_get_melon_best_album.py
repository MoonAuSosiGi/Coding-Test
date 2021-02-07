genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 두개씩 모아서 베스트 앨범을 만든다.
    # 속한 노래가 많이 재생된 장르부터 넣어야 함
    # 팝이 젤 많이 재생되었다면, 팝먼저 두개,다른장르 두개 이런식
    result = []
    many_play_dic = {}
    genre_dict = {}

    for i in range(len(genre_array)):
        if genre_array[i] in many_play_dic:
            many_play_dic[genre_array[i]] += play_array[i]
        else:
            many_play_dic[genre_array[i]] = play_array[i]

        if genre_array[i] in genre_dict:
            genre_dict[genre_array[i]].append(play_array[i])
        else:
            genre_dict[genre_array[i]] = []
            genre_dict[genre_array[i]].append(play_array[i])

    many_play_list = sorted(many_play_dic.items(),key=(lambda x: x[1]),reverse=True)

    # 장르별로 체크함
    while len(many_play_list) > 0:
        item = many_play_list.pop(0)
        genre_dict[item[0]].sort(reverse=True)
        genre_dict[item[0]] = genre_dict[item[0]][:2]
        while len(genre_dict[item[0]]) > 0:
            result.append(play_array.index(genre_dict[item[0]].pop(0)))

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!