from collections import deque


class PlayList(deque):
    """
    Playlist deque.  Songs are added to the front of the list, allowing it to
    to grow indefinitely, or to the specificed ``maxlen``.  Songs are popped
    off of the queue by the player, using the ``next()`` method.
    """

    def __init__(self, maxlen=None):
        super().__init__(maxlen=maxlen)
        self.current_song = None

    def __call__(self, song=None):
        if song is not None:
            self.appendleft(song)

    def next(self):
        """ Pops the last url off of the deque.  This url is directly picked up
        by the player.  Once this has been called the url is gone from the
        queue.

        :return: The next song to play
        :rtype: str
        """
        self.current_song = self.pop()
        return self.current_song


#: Initialized version of the playist for use in other modules.
playlist = PlayList()
