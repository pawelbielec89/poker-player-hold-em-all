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
        if len(communitycards) == 0:
            return False
        for card in cards:
            for communitycard in communitycards:
                if card["rank"] == communitycard["rank"]:
                    return True

    def checkForPoker(self, cards, communitycards):
        player_and_community_cards = self.getSevenCardsRanks(cards, communitycards)
        if "A" in player_and_community_cards and "K" in player_and_community_cards and "Q" in player_and_community_cards and "J" in player_and_community_cards and "10" in player_and_community_cards:
            return True
        else: return False

    def checkForFiveColours(self, cards, communitycards):
        player_and_community_cards = self.getSevenCardsColours(cards, communitycards)
        red = 0
        black = 0
        for card in player_and_community_cards:
            print(card)
            if card == "spades" or card == "clubs":
                black += 1
            else:
                red +=1
        if red == 5 or black == 5:
            return True
        else:
            return False
    def checkFourSameCards(self, cards, communitycards):
        player_and_community_cards = self.getSevenCardsRanks(cards, communitycards)
        allCards = {}
        for card in player_and_community_cards:
            allCards[card] = 'value'
        if len(allCards) < 2:
            return False
        else:
            return True

    def getSevenCardsRanks(self, cards, communitycards):
        player_and_community_cards = []
        for card in cards:
            player_and_community_cards += card["rank"]
        for card in communitycards:
            player_and_community_cards += card["rank"]
        return player_and_community_cards

    def getSevenCardsColours(self, cards, communitycards):
        player_and_community_cards = []
        for card in cards:
            player_and_community_cards.append(card["suit"])
        for card in communitycards:
            player_and_community_cards.append(card["suit"])
        return player_and_community_cards

    def checkScore(self, cards, communitycards):
        if self.checkForPoker(cards,communitycards):
            return 9
        elif self.checkForFiveColours(cards, communitycards):
            return 8
        elif self.checkFourSameCards(cards, communitycards):
            return 7
        elif self.checkForPairInHandAndCommunity(cards, communitycards):
            return 2
        return 0
    def betRequest(self, game_state):

        self.game_state = game_state
        try:
            me = self.getPlayer("Hold Em All")
            noDemocracy = self.getPlayer("NO democracy")
            probablyJS = self.getPlayer("Probably JS")
            mycards = self.getCardsFromPlayer(me)
            communitycards = self.getCommunityCards()
            if len(communitycards) > 0:
                noDemocracyCards = self.getCardsFromPlayer(noDemocracy)
                probablyJSCards = self.getCardsFromPlayer(probablyJS)
                myScore = self.checkScore(mycards, communitycards)
                noDemocracyScore = self.checkScore(noDemocracyCards, communitycards)
                probablyJSScore = self.checkScore(probablyJSCards, communitycards)
                if myScore > noDemocracyScore and myScore > probablyJSScore:
                    return self.getMyCoinStack()
                else:
                    return 0
            else:
                if self.checkForPairInHand(mycards):
                    return self.game_state["minimum_raise"]

                else:
                    return 10

        except Exception as e:
            return self.game_state["minimum_raise"]

    def showdown(self, game_state):
        pass