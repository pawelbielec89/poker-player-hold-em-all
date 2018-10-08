
class Player:
    VERSION = "Default Python folding player"

    def panicMode(self): #DEFAULT GAME MODE
        return 1000

    def getPlayersList(game_state): # RETURNS PLAYERS IN LIST
        return game_state["players"]

    def getPlayer(name, game_state): # RETURNS PLAYER AS DICT
        players_list = Player.getPlayersList(game_state)
        for player in players_list:
            if name == player["name"]:
                return player

    def getCardsFromPlayer(player): # RETURNS CARDS IN LIST
        return player["hole_cards"]

    def getCommunityCards(game_state): # RETURNS COMMUNITY CARDS
        return game_state["community_cards"]

    def getMyCoinStack(game_state): # RETURNS MY COINS IN INT
        return Player.getPlayer("Hold Em All", game_state)["stack"]

    def betRequest(self, game_state):
        try:
            me = Player.getPlayer("Hold Em All", game_state)
            mycards = Player.getCardsFromPlayer(me)

            if mycards[0]["rank"] == mycards[1]["rank"]:
                return Player.getMyCoinStack(game_state)/2
            return Player.getMyCoinStack(game_state)/6
        except Exception:
            return Player.panicMode()

    def showdown(self, game_state):
        pass

