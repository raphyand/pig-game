import random, pdb
from Player import Player, Computer
from utils import gameState, playerQueue
from DisplayManager import DisplayManager

# Holds the rules and back-end game setup
class GameManager():
    def __init__(self, m, hS):
        self.mode = m
        self.highestScore = hS
        self.playerTurnList = playerQueue(list())
        self.turnList = []
        self.die = random
        self.myDisplayManager = DisplayManager()
        self.userInput = None
        self._currentGameState = gameState.MAIN_MENU
        self._currentPlayer = self.playerTurnList.getIndex(0)

    def setCurrentGameState(self, gameStateToChange):
        self._currentGameState = gameStateToChange

    def getCurrentGameState(self):
        return self._currentGameState

    def setMode(self, modeValue):
        self.mode = modeValue

    def getCurrentPlayer(self):
        return self._currentPlayer

    def setCurrentPlayer(self, player):
        self._currentPlayer = player

    def setCurrentPlayerByIndex(self, playerIndex):
        self._currentPlayer = self.playerTurnList.getIndex(playerIndex)

    def receiveInput(self):
        self.userInput = input("Please Enter a choice.")
        #print("Debug: User Input is: ", self.userInput)
        #print (type(self.userInput))
        #return self.userInput

    def getUserInput(self):
        return self.userInput

    def rollDice(self):
        #result = random.randrange(0, 5)
        result = self.die.randint(1, 6)
        print("Dice is being rolled...")
        print("Rolled a", result)
        return result

    def mainMenu(self):
        self.myDisplayManager.printMainMenu()
        self.receiveInput()
        if self.getUserInput() == '1':
            print("SinglePlayer")
            self.setCurrentGameState(gameState.PLAYER_SELECTION_MENU)

        elif self.getUserInput() == '2':
            print("Multiplayer")
            self.setCurrentGameState(gameState.PLAYER_SELECTION_MENU)

        elif self.getUserInput() == '3':
            self.setCurrentGameState(gameState.GAMEOVER)
            print("Game Over!")


    def playerSelectionMenu(self):
        validInput = True
        if self.userInput == '1':
            userName = input("Please enter your name.")
            self.playerTurnList.addPlayer(userName)
            while validInput is True:  
                self.myDisplayManager.printPlayerSelection()
                self.receiveInput()
                #When user input is outside of range.
                if int(self.userInput) <= 1 or int(self.userInput) > 4:
                    validInput = False

                #When user Input is valid.
                if int(self.userInput) > 1 and int(self.userInput) <= 4:
                    for iterator in range(int(self.userInput) - 1):
                        self.playerTurnList.addComputer()
                    self.setCurrentGameState(gameState.WHO_GOES_FIRST)
                    break

                #When user input is completely invalid
                else:    
                    validInput = False

        elif self.userInput == '2':
            while validInput is True:
                self.myDisplayManager.printPlayerSelection()
                self.receiveInput()
                amountOfPlayers = int(self.userInput)
                if int(self.userInput) <= 1 or int(self.userInput) > 4:
                    validInput = False
                else:
                    validInput = False                
                print("How many computers?")
                self.receiveInput()
                if int(self.userInput) - amountOfPlayers < 0:
                    print("Invalid amount of players.")
                    validInput = False
                elif int(self.userInput) - amountOfPlayers > 0:
                    humanPlayers = int(self.userInput) - amountOfPlayers
                    iterator = 0
                    #for iterator in range()
                    #self.playerTurnList.a
                    self.setCurrentGameState(gameState.WHO_GOES_FIRST)
                    break
                else:
                    validInput = False
            
    def whoGoesFirst_Menu(self):
        #pdb.set_trace()
        for iterator in self.playerTurnList:
            if iterator.isAComputer() is False:
                print("Debug: ", iterator)
                print("Debug: ", iterator.isAComputer())
                print("Debug: " , self.playerTurnList.printAll())
                print("Press 1 to roll.")
                self.receiveInput()
                if self.userInput == '1':
                    iterator.setTurnNumber(self.rollDice())
                    #iterator.self.rollDice()

            elif iterator.isAComputer() is True:
                iterator.setTurnNumber(self.rollDice())
            
        print("Now adjusting turn order.")
        self.playerTurnList.sort()
        iterator = 0
        displayNumber = 0
        for iterator in self.playerTurnList:
            iterator += 1
            print(displayNumber, " ", iterator.getName())
        self.setCurrentPlayer(self.playerTurnList.getFirstPlayer())
        self.setCurrentGameState(gameState.TURN_MENU)


    def turnMenu(self, currentPlayer):
        self.myDisplayManager.printTurnMenu(currentPlayer)
        self.receiveInput()
        if self.userInput == 1:
            #Throw dice, then update 
            pass
        elif self.userInput == 2:
            #Program a Hold
            pass

        