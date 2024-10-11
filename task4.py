class Music:
    def __init__(self, all_songs):
        self.all_songs = all_songs
    
    def find_song(self):
        self.song = input('Искать песню:')
        return self.song

class Playlist:
    history = []

    def __init__(self, qty, qty_fav, name):
        self.s1 = Music(600)
        self.qty = qty
        self.name = name
        self.qty_fav = qty_fav
        self.len_song = 3
        self.songs = []
        self.favorite = []
        self.history = []

    def add_song(self):
        self.song = self.s1.find_song()
        self.songs.append(self.song)
        self.qty +=1
        
    def change_favorites(self):
        self.favorite.append(self.song)
        self.qty_fav +=1

    
    def change_len_song(self):
        self.len_song = int(input('Обрезать песню '))

    def change_name_playlist(self):
        self.name = str(input('Новое название песни:'))

class Information:

    def __init__(self):
        self.s2 = Playlist(32,14, 'Любимое')

    def print_information(self):
        print(self.s2.name)
        print(self.s2.qty)
        print(self.s2.qty_fav)
        print(self.s2.songs)
        print(self.s2.favorite)

s1 = Music(600)
s1.find_song()
s2 = Playlist(32,14, 'Любимое')
s2.add_song()
s2.change_favorites()
s2.change_len_song()
s2.change_name_playlist()

i = Information()
i.print_information()
