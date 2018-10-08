import traceback

class Player:
    VERSION = "Default Python folding player"

    def getPlayersList(self): # RETURNS PLAYERS IN LIST
        return self.game_state["players"]

    def getPlayer(self, player_name): # RETURNS PLAYER AS DICT
        players_list = self.getPlayersList()
        for player in players_list:
            if player_name == player["name"]:
                return player

    def getCardsFromPlayer(self, player): # RETURNS CARDS IN LIST
        return player["hole_cards"]

    def getCommunityCards(self): # RETURNS COMMUNITY CARDS
        return self.game_state["community_cards"]

    def getMyCoinStack(self): # RETURNS MY COINS IN INT
        return self.getPlayer("Hold Em All")["stack"]

    def checkColors(self, mycards, communitycards):
        cards = mycards + communitycards
        hearts = 0
        spades = 0
        clubs = 0
        diamonds = 0
        colors = [hearts, spades, clubs, diamonds]
        for card in cards:
            if card["suit"] == "hearts":
                hearts += 1
            elif card["suit"] == "spades":
                spades += 1
            elif card["suit"] == "clubs":
                clubs += 1
            elif card["suit"] == "diamonds":
                diamonds += 1

        for color in colors:
            if color >= 4:
                return self.getMyCoinStack(self)
            elif color == 3:
                return self.getMyCoinStack(self) / 2
            elif color == 2:
                return self.getMyCoinStack() / 5
        return 10

    def betRequest(self, game_state):
        self.game_state = game_state
        try:
            me = self.getPlayer("Hold Em All")
            mycards = self.getCardsFromPlayer(me)
            if mycards[0]["rank"] == mycards[1]["rank"]:
                return self.getMyCoinStack()/2
            return self.getMyCoinStack()/6
        except Exception as e:
            traceback.print_exc()
            return 1000


    def showdown(self, game_state):
        pass