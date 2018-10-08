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


    def checkForPairInHand(self, mycards):
        if mycards[0]["rank"] == mycards[1]["rank"]:
            return True

    def checkForPairInHandAndCommunity(self, cards, communitycards):
        if communitycards.length == 0:
            return False
        for card in cards:
            for communitycard in communitycards:
                if card["rank"] == communitycard["rank"]:
                    return True

    def checkForPoker(self, cards, communitycards):
        player_and_community_cards = []
        for card in cards:
            player_and_community_cards += card["rank"]
        for card in communitycards:
            player_and_community_cards += card["rank"]
        if "A" in player_and_community_cards and "K" in player_and_community_cards and "Q" in player_and_community_cards and "J" in player_and_community_cards and "10" in player_and_community_cards:
            return True
        else: return False
        
    def betRequest(self, game_state):
        self.game_state = game_state
        try:
            me = self.getPlayer("Hold Em All")
            mycards = self.getCardsFromPlayer(me)
            communitycards = self.getCommunityCards()
            pair = self.checkForPairInHand(mycards)
            whole_pair = self.checkForPairInHandAndCommunity(mycards, communitycards)

            if (pair == True) or (whole_pair == True):
                return self.getMyCoinStack()/2
            else:
                return 10

        except Exception as e:
            traceback.print_exc()
            return 333
                
    def showdown(self, game_state):
        pass