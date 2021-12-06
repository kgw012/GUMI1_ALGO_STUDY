# 프로그래머스 문제 '베스트앨범'
# https://programmers.co.kr/learn/courses/30/lessons/42579

class Song:

    def __init__(self, song_num, genre, play):
        self.song_num = song_num
        self.genre = genre
        self.play = play
    

def solution(genres, plays):
    genre_dict = {}
    genre_list = []

    for song_num, genre, play in zip(range(len(genres)), genres, plays):
        song = Song(song_num, genre, play)

        if not genre_dict.get(genre):
            genre_list.append(genre)
            genre_dict[genre] = {'total_plays': 0, 'song_list': []}
        
        genre_dict[genre]['total_plays'] += play
        genre_dict[genre]['song_list'].append(song)

    genre_list.sort(reverse=True, key=lambda genre: genre_dict[genre]['total_plays'])

    best_album = []
    for genre in genre_list:
        song_list = genre_dict[genre]['song_list']
        song_list.sort(reverse=True, key=lambda song: (song.play, -song.song_num))
        best_songs = song_list[:2]
        for song in best_songs:
            best_album.append(song.song_num)
    
    return best_album



def solution2(genres, plays):
    genre_dict = {}
    genre_list = []

    for song_num, genre, play in zip(range(len(genres)), genres, plays):
        song = Song(song_num, genre, play)

        if not genre_dict.get(genre):
            genre_dict[genre] = {'total_plays': 0, 'best_songs': [Song(-1, genre, -1), Song(-1, genre, -1)]}
            genre_list.append(genre)

        genre_dict[genre]['total_plays'] += play

        best_songs = genre_dict[genre]['best_songs']
        if best_songs[0].play < play:
            best_songs[1] = best_songs[0]
            best_songs[0] = song
            continue

        if best_songs[0].play == play:
            if best_songs[0].song_num > song_num:
                best_songs[1] = best_songs[0]
                best_songs[0] = song
                continue
        
        if best_songs[1].play < play:
            best_songs[1] = song
            continue
        
        if best_songs[1].play == play:
            if best_songs[1].song_num > song_num:
                best_songs[1] = song

    genre_list.sort(reverse=True, key=lambda genre: genre_dict[genre]['total_plays'])

    best_album = []

    for genre in genre_list:
        best_songs = genre_dict[genre]['best_songs']
        for song in best_songs:
            if song.play >= 0:
                best_album.append(song.song_num)

    return best_album


if __name__=='__main__':

    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    answer = [4, 1, 3, 0]
    my_answer = solution(genres, plays)

    print(f'answer: {answer}, my_answer: {my_answer}')