class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            if not hasattr(self, "_title"):
                self._title = title
        #     else:
        #         raise AttributeError("Title has already been set and cannot be changed")
        # else:
        #     raise TypeError("title must be non-empty string")


    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()])) 

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2,17):
            self._username = username
        # else:
        #     raise TypeError("username must be string with 2-16 characters")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        if self.played_game(game):
            return [result.game for result in self.results()].count(game)
        else:
            return 0


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        # else:
        #     raise TypeError("player must be instance of Player")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        # else:
        #     raise TypeError("game must be an instance of Game")

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and score in range(0,5001):
            if not hasattr(self, "_score"):
                self._score = score
        #     else:
        #         raise AttributeError("Score has already been set and cannot be changed")
        # else:
        #     raise ValueError("score must be an integer between 1 and 5000")
