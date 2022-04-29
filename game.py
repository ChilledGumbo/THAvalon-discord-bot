class Game():

    def __init__(self):

        self.started = False
        self.round = 0
        self.missions_failed = 0
        self.players = []
        self.num_players = 0

    def add_player(self, player_id):

        self.players.append(player_id)
        self.num_players += 1

    def has_player(self, player_id):

        return player_id in self.players

    def list_players(self):

        return self.players


class Player():

    def __init__(self, player_id):

        self.player_id = player_id
        self.can_see = []

class Arthur(Player):

    def __init__(self, player_id):

        Player.__init__(self, player_id)
        self.evil = 0

class Mordred(Player):

    def __init__(self, player_id):

        Player.__init__(self, player_id)
        self.evil = 1
        
