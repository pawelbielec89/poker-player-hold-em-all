import traceback

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
            return self.getMyCoinStack() / 4
                
    def showdown(self, game_state):
        pass