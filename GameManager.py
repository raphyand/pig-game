import random
from DisplayManager import DisplayManager

# Holds the rules and back-end game setup
class GameManager():
    def __init__(self, m, hS):
        self.mode = m
        self.highestScore = hS
        self.turnList = []
        self.die = random
        self.myDisplayManager = DisplayManager()
        self.userInput = None

    def setMode(self, modeValue):
        self.mode = modeValue

    def receiveInput(self):
        self.userInput = input("Please Enter a choice.")
        print("Debug: User Input is: ", self.userInput)

    def rollDice(self):
        #result = random.randrange(0, 5)
        result = self.die.randint(1, 6)
        print("Dice is being rolled...")
        print("Rolled a", result)
        return result

    def mainMenu(self):
        self.myDisplayManager.printMainMenu()
        self.receiveInput()

    def turnMenu(self, currentPlayer):

        
        self.myDisplayManager.printTurnMenu(currentPlayer)
        self.receiveInput()
        if self.userInput == 1:
            #Throw dice, then update 
            pass
        elif self.userInput == 2:
            #Program a Hold
            pass

        