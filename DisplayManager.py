from Player import Player, Computer
#from GameManager import GameManager
import random
class DisplayManager():
    def __init__(self):
        pass
        
    def printMainMenu(self):
        print("Hello! Welcome to Pig.")
        print("\t1.SinglePlayer")
        print("\t2.Multiplayer")
        print("\t3.Quit")

    #Instead of myGameManager, pass in an int
    def printTurnMenu(self, PlayerName, PlayerTotalScore, GameManagerCurrentScore):
        print(PlayerName, "\'s Turn")
        print("Total Score:", PlayerTotalScore)
        print("Score for the turn:", GameManagerCurrentScore)
        print("1. Roll")
        print("2. Hold")

    def printPlayerSelection(self):
        print("How many players in total are there? (Including Yourself)")
        print("Maximum amount is 4 Players.")

    