class MusicQueue:
    def __init__(self):
        self.songs = []
    def add_song(self,song):
        self.songs.append(song)
        print(f'Add: {song}')
    def play_next(self):
        if self.songs is not None:
            next_song = self.songs.pop(0)
            print(f'Playing:{next_song}')
        else:
            print('No songs in queue')
    def show_queue(self):
        if self.songs is not None:
            print(f'Queue:{self.songs}')
        else:
            print('No songs in queue')
def test():
    mq = MusicQueue()
    mq.add_song('SongA')
    mq.add_song('SongB')
    mq.add_song('SongC')
    mq.add_song('SongD')
    mq.play_next()
    mq.play_next()
    mq.show_queue()
test()
