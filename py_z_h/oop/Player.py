class Player:
    def __init__(self, name):
        self.name = name
        self._level = 1
        self._lives = 3
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score = delta * 1000
            self._level = level
        else:
            print("Level cannot be less then 1")

    def _del_level(self):
        print("deeeeeeeeeeel")
        del self._level

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    level = property(_get_level, _set_level, _del_level)
    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Level: {0.level}, Lives: {0.lives}, Score: {0.score}".format(self)

