class MusicQueue:
    def __init__(self):
        self.queue = []
    def add_song(self,song):
        self.queue.append(song)
        print(f'add {song}')
    def play_next(self):
        if self.queue:
            print(f'playing {self.queue.pop(0)}')
        else:
            print('No more songs to play.')
    def show_queue(self):
        return self.queue
def test():
    mq = MusicQueue()
    mq.add_song('Song A')
    mq.add_song('Song B')
    mq.add_song('Song C')
    mq.add_song('Song D')
    mq.play_next()
    mq.play_next()
    print(mq.show_queue())
test()