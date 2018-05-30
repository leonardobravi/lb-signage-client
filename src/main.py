import logging
from subprocess import Popen, PIPE, DEVNULL

# __player_name__ = "mplayer"
__player_name__ = "omxplayer"

start_command = 'z'  # f
quit_command = 'q'
toggle_command = 'p'

logger = logging.getLogger(__name__)

print('Class init')


class Player:
    def __init__(self, movie):
        self.movie = movie
        self.process = None

    def start(self):
        print('Player start')
        self.stop()
# self.process = Popen([__player_name__, "-o", "hdml", "--win", "0 0 1920 1080", self.movie], stdin=PIPE,
#                     stdout=DEVNULL, close_fds=True, bufsize=0)
        self.process = Popen([__player_name__, self.movie], stdin=PIPE,
                             stdout=DEVNULL, close_fds=True, bufsize=0)
        print(__player_name__, self.movie)
        # self.process.stdin.write(start_command.encode('UTF-8'))  # start playing

    def stop(self):
        p = self.process
        if p is not None:
            try:
                p.stdin.write(quit_command.encode('UTF-8'))  # send quit command
                p.terminate()
                p.wait()  # -> move into background thread if necessary
            except EnvironmentError as e:
                logger.error("can't stop %s: %s", self.movie, e)
            else:
                self.process = None

    def toggle(self):
        p = self.process
        if p is not None:
            try:
                p.stdin.write(toggle_command.encode('UTF-8'))  # pause/unpause
            except EnvironmentError as e:
                logger.warning("can't toggle %s: %s", self.movie, e)


print('Prepare')
# Test Begin
names = 'one', 'two'
movies = ['resources/video/{name}.mp4'.format(name=name) for name in names]
players = [Player(movie=movie) for movie in movies]
player = players[0]
# Test ends

if __name__ == '__main__':
    print('Main init')
    player.start()
