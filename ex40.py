class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    def things_with_list(self):
        self.lyrics.reverse()
        print "%s" % self.lyrics
        print "%i" % len(self.lyrics)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to ge sued",
                    "So i'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

horra = Song(["Aho, aho, copii si frati",
                "Stati putin si nu minati",
                "Pe linga noi va alaturati",
                "Si cuvintul mi'l ascultati!"])

hora2 = ["Vine iarna",
            "Toamna trece!"]

hora3 = Song(hora2)

happy_bday.things_with_list()
