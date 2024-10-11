class Music:
    def __init__(self, all_songs):
        self.all_songs = all_songs
    
    def find_song(self):
        self.song = input('Искать песню:')

class Playlist:
    history = []

    def __init__(self, qty, qty_fav, name):
        self.qty = qty
        self.name = name
        self.qty_fav = qty_fav
        self.len_song = 3
        self.songs = []
        self.favorite = []
        self.history = []

    def add_song(self):
        self.song = s1.find_song()
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

    def print_information(self):
        i = Playlist(32, 14, 'Любимое')
        print(i.name)
        print(i.qty)
        print(i.qty_fav)
        print(i.songs)
        print(i.favorite)

s1 = Music(600)
s1.find_song()
s2 = Playlist(32,14, 'Любимое')
s2.add_song()
s2.change_favorites()
s2.change_len_song()
s2.change_name_playlist()

i = Information()
i.print_information()
