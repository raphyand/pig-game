from Player import Player, Computer
import random, time
class DisplayManager():
    def __init__(self):
        pass
        
    def printMainMenu(self):
        print("Hello! Welcome to Pig.")
        print("\t1.SinglePlayer")
        print("\t2.Multiplayer")
        print("\t3.Quit")

    #Instead of myGameManager, pass in an int
    def printTurnMenu(self, PlayerName, PlayerTotalScore, GameManagerCurrentScore, playerTimesRolled):
        print(PlayerName, "\'s Turn")
        print("Total Score:", PlayerTotalScore)
        print("Score for the turn:", GameManagerCurrentScore)
        print("Times Rolled:", playerTimesRolled)
        print("1. Roll")
        print("2. Hold")
        print("")

    def printPlayerSelection(self):
        print("How many players in total are there? (Including Yourself)")
        print("Maximum amount is 4 Players.")
        print("")

    def printTransition(self, dots, timeBetween):
        for i in range(dots):
            print(".")
            time.sleep(timeBetween)

    def printMatchEndMenu(self):
        print("1. Main Menu.")
        print("2. Exit.")