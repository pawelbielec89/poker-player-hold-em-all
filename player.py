
class Player:
    VERSION = "Default Python folding player"

    def getPlayersList(game_state): # RETURNS PLAYERS IN LIST
        return game_state["players"]

    def getPlayer(self, name, game_state): # RETURNS PLAYER AS DICT
        players_list = self.getPlayersList(game_state)
        for player in players_list:
            if name == player["name"]:
                return player

    def getCardsFromPlayer(player): # RETURNS CARDS IN LIST
        return player["hole_cards"]

    def getCommunityCards(game_state): # RETURNS COMMUNITY CARDS
        return game_state["community_cards"]

    def getMyCoinStack(self, game_state): # RETURNS MY COINS IN INT
        return self.getPlayer("Hold Em All", game_state)["stack"]

    def betRequest(self, game_state):
        try:
            my_cards = game_state["players"][0]["hole_cards"]
            if my_cards[0]["rank"] == my_cards[1]["rank"]:
                return 200
            elif my_cards[0]["suits"] == my_cards[1]["suits"]:
                return  100
            return self.getMyCoinStack(game_state)/6

        except Exception:
            return 1000

    def showdown(self, game_state):
        pass

