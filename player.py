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