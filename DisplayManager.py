from Player import Player, Computer

class DisplayManager():
    def __init__(self):
        pass
        
    def printMainMenu(self):
        print("Hello! Welcome to Pig.")
        print("\t1.SinglePlayer")
        print("\t2.Multiplayer")
        print("\t3.Quit")

    def printTurnMenu(self, Player):
        print(Player.getName(), "\'s Turn")
        print("1. Roll")
        print("2. Hold")