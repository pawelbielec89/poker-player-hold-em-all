

class Player:
    VERSION = "Default Python folding player"
    def panicMode(self): #default game mode
        return 1000

    def betRequest(self, game_state):
        return self.panicMode(self)

    def showdown(self, game_state):
        pass

