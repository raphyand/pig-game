import random, pdb
from Player import Player, Computer
from utils import gameState
from DisplayManager import DisplayManager
from playerQueue import playerQueue

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
        self._currentScore = 0

    def setCurrentGameState(self, gameStateToChange):
        self._currentGameState = gameStateToChange

    def getCurrentGameState(self):
        return self._currentGameState

    def setCurrentScore(self, score):
        self._currentScore = score
    
    def getCurrentScore(self):
        return self._currentScore

    def getMode(self):
        return self.mode

    def setMode(self, modeValue):
        self.mode = modeValue

    def getCurrentPlayer(self):
        return self._currentPlayer

    def setCurrentPlayer(self, player):
        self._currentPlayer = player

    def setCurrentPlayerByIndex(self, playerIndex):
        self._currentPlayer = self.playerTurnList.getIndex(playerIndex)

    def receiveInput(self):
        self.userInput = input(">>")

    def getUserInput(self):
        return self.userInput

    def rollDice(self, displayText):
        result = self.die.randint(1, 6)
        if displayText is True:
            print("Dice is being rolled...")
            print("Rolled a", result)
        return result

    def hold(self):
        self._currentPlayer.addToTotalScore(self._currentScore)

    def coreGamePlayLoop(self):
       while self.getCurrentGameState() is not gameState.GAMEOVER:
            if (self.getCurrentGameState() is gameState.MAIN_MENU):
                self.mainMenu()
            elif(self.getCurrentGameState() is gameState.PLAYER_SELECTION_MENU):
                self.playerSelectionMenu()
            elif(self.getCurrentGameState() is gameState.WHO_GOES_FIRST):
                self.whoGoesFirst_Menu()
            elif(self.getCurrentGameState() is gameState.TURN_MENU):
                self.turnMenu(self.getCurrentPlayer())
       exit()

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
        for iterator in self.playerTurnList:
            if iterator.isAComputer() is False:
                print("Press 1 to roll.")
                self.receiveInput()
                if self.userInput == '1':
                    iterator.setTurnNumber(self.rollDice(True))

            elif iterator.isAComputer() is True:
                iterator.setTurnNumber(self.rollDice(False))
            
        print("Now adjusting turn order.")
        self.playerTurnList.sort()
        displayNumber = 0
        pdb.set_trace()
        for itera in self.playerTurnList:
            displayNumber += 1
            print(displayNumber, ".", itera.getName())

        self.setCurrentPlayer(self.playerTurnList.getFirstPlayer())
        self.setCurrentGameState(gameState.TURN_MENU)

    def turnMenu(self, currentPlayer):
        self.playerTurnList.activateCircular()
        for players in self.playerTurnList:
            endTurnFlag = False
            while endTurnFlag is False:
                if players.isAComputer() is False:
                    self.myDisplayManager.printTurnMenu(currentPlayer.getName(), currentPlayer.getTotalScore(),  self._currentScore)
                    self.receiveInput()
                    if self.userInput == '1':
                        result = self.rollDice(True)
                        if result is 1:
                            self._currentScore = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!")
                            endTurnFlag = True
                        else:
                            self._currentScore = self._currentScore + result
                            print("Your current score:", self._currentScore)
                        
                    elif self.userInput == '2':
                        endTurnFlag = True
                        #Program a Hold
                        self.hold()
                        endTurnFlag = True

                elif players.isAComputer() is True:
                    self.userInput = players.actOnBehavior()
                    self.myDisplayManager.printTurnMenu(currentPlayer.getName(), currentPlayer.getTotalScore(),  self._currentScore)
                    if self.userInput == '1':
                        result = self.rollDice(True)
                        if result is 1:
                            self._currentScore = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!")
                            endTurnFlag = True
                        else:
                            self._currentScore = self._currentScore + result
                    elif self.userInput == '2':
                        endTurnFlag = True
                        #Program a Hold
                        self.hold()
                        endTurnFlag = True

        # Terminate here