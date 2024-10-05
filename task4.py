class Music:
    def __init__(self, all_songs):
        self.all_songs = all_songs
    
    def find_song(self):
        self.song = input()

class Playlist:

    def __init__(self, N, N_f, name):
        self.N = N
        self.name = name
        self.N_f = N_f
        self.len_song = 3
        self.songs = []
        self.favorite = []

    def add_song(self):
        self.song = input()
        self.songs.append(self.song)
        self.N +=1
        
    def change_favorites(self):
        self.favorite.append(self.song)
        self.N_f +=1

    
    def change_len_song(self):
        self.len_song = int(input())

    def change_name_playlist(self):
        self.name = str(input())

class Information:

    def print_information(self):
        print(self.name)
        print(self.N)
        print(self.N_f)
        print(self.songs)
        print(self.favorite)

s1 = Music(13)
s1.find_song()
s2 = Playlist(32,14, 'Любимое')
s2.add_song()
s2.change_favorites()
s2.change_len_song()
s2.change_name_playlist()

i = Information()
i.print_information()
