import utils
import random
class Player():
    def __init__(self, name, currentScore, totalScore, timesRolled, isComputer):
        self.name = name
        self.currentScore = currentScore
        self.totalScore = totalScore
        self.timesRolled = timesRolled
        self.isComputer = isComputer
        self.turnNumber = None
    #Remove currentScore and move it to Game Manager; once the turnScore in Game Manager is finished, THEN you should add it to playerScore
    def printPlayerSheet(self):
        print("Name: ", self.name)
        print("Current Score: ", self.currentScore)
        print("Total Score: ", self.totalScore)
        print("Times rolled this turn: ", self.timesRolled)
        print("Is a Computer? : ", self.isComputer)

    def setName(self, name):
        self.name = name
        return self.name

    def getName(self):
        return self.name

    def getCurrentScore(self):
        return self.currentScore
    
    def getTotalScore(self):
        return self.totalScore

    def getTimesRolled(self):
        return self.timesRolled

    def isAComputer(self):
        return self.isComputer
    
    def setTurnNumber(self, turnNumber):
        self.turnNumber = turnNumber
    
    def getTurnNumber(self):
        return self.turnNumber
        
    #def updatePlayerTurn(self, scoreToAdd):
    #    pass
class Computer(Player):
    def __init__(self, name, currentScore, totalScore, timesRolled, isComputer, Behavior):
        super().__init__(name, currentScore, totalScore, timesRolled, isComputer)
        self._nameList = list("Alexa the Despacito", "SkyNet", "Johnny 5", "Terminator", "Henry the Robot")
        self.Behavior = Behavior

    def instantiateName(self):
        self.name = random.choice(self._nameList)