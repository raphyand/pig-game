import random, pdb
import time
from Player import Player, Computer
from utils import gameState
from DisplayManager import DisplayManager
from playerQueue import playerQueue

"""Game Manager: Handles all things relating to Pig's internal execution."""

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
        self.userInput = input(">> ")

    def getUserInput(self):
        return self.userInput

    def rollDice(self, displayText):
        result = self.die.randint(1, 6)
        if displayText is True:
            print("Dice is being rolled...")
            print("Rolled a", result, "\n")
        return result

    def hold(self):
        self._currentPlayer.addToTotalScore(self._currentScore)
        self._currentPlayer.clearTimesRolled()
        self._currentScore = 0

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
            elif(self.getCurrentGameState() is gameState.MATCH_END):
                self.matchEndMenu()

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
        validInput2 = True
        while validInput2 is True:
            if self.userInput == '1':
                userName = input("Please enter your name.\n")
                self.playerTurnList.addPlayer(userName)
                while validInput is True:  
                    self.myDisplayManager.printPlayerSelection()
                    self.receiveInput()
                    #When user Input is valid.
                    if str.isalpha(self.userInput):
                        validInput2 = False
                    elif int(self.userInput) > 1 and int(self.userInput) <= 4:
                        for iterator in range(int(self.userInput) - 1):
                            self.playerTurnList.addComputer()
                        self.setCurrentGameState(gameState.WHO_GOES_FIRST)
                        break
                    #When user input is outside of range.
                    elif int(self.userInput) <= 1 or int(self.userInput) > 4:
                        validInput = False
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
                        self.setCurrentGameState(gameState.WHO_GOES_FIRST)
                        break
                    else:
                        validInput = False
                else:
                    validInput2 = False
            else:
                validInput2  = False


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
        self.myDisplayManager.printTransition(3, 0.5)
        self.playerTurnList.sort()
        displayNumber = 0
        for itera in self.playerTurnList:
            displayNumber += 1
            print(displayNumber, ".", itera.getName())

        self.setCurrentPlayer(self.playerTurnList.getFirstPlayer())
        #Sleep for a bit
        #time.sleep(1.5)
        self.myDisplayManager.printTransition(3, 1)        
        self.setCurrentGameState(gameState.TURN_MENU)

    def turnMenu(self, currentPlayer):
        self.playerTurnList.activateCircular()
        gameWon = False
        for players in self.playerTurnList:
            self._currentPlayer = players
            endTurnFlag = False
            #validInput = True
            while endTurnFlag is False:
                if players.isAComputer() is False:
                    self.myDisplayManager.printTurnMenu(players.getName(), players.getTotalScore(),  self._currentScore, players.getTimesRolled())
                    self.receiveInput()
                    
                    if self.userInput == '1':
                        result = self.rollDice(True)
                        players.incrementTimesRolled()                        
                        if result == 1:
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
                        if players.getTotalScore() >= 100:
                            print(players.getName(), "you win!")
                            gameWon = True
                            break
                        endTurnFlag = True
                    
                    

                elif players.isAComputer() is True:
                    self.userInput = players.actOnBehavior()
                    self.myDisplayManager.printTurnMenu(players.getName(), players.getTotalScore(),  self._currentScore, players.getTimesRolled())
                    if self.userInput == '1':
                        result = self.rollDice(True)
                        players.incrementTimesRolled()
                        if result == 1:
                            self._currentScore = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!\n")
                            endTurnFlag = True
                        else:
                            self._currentScore = self._currentScore + result
                            #time.sleep(1.5)
                            self.myDisplayManager.printTransition(3, .5)
                    elif self.userInput == '2':
                        endTurnFlag = True
                        #Program a Hold
                        self.hold()
                        if players.getTotalScore() >= 100:
                            print(players.getName(), "you win!")
                            gameWon = True
                            break                    
                        endTurnFlag = True

            if gameWon is True:
                break        
            self.myDisplayManager.printTransition(3, 0.5)
        # Terminate here
        self.setCurrentGameState(gameState.MATCH_END)

    def matchEndMenu(self):
        self.myDisplayManager.printMatchEndMenu()
        self.receiveInput()
        if self.userInput == '1':
            self.setCurrentGameState(gameState.MAIN_MENU)
        elif self.userInput == '2':
            self.setCurrentGameState(gameState.GAMEOVER)
        
