import random
from utils import AIBehaviors
class Player():
    def __init__(self, name, totalScore, timesRolled, isComputer):
        self.name = name
        #self.currentScore = currentScore
        self.totalScore = totalScore
        self.timesRolled = timesRolled
        self.isComputer = isComputer
        self.turnNumber = None
    #Remove currentScore and move it to Game Manager; once the turnScore in Game Manager is finished, THEN you should add it to playerScore
    def printPlayerSheet(self):
        print("Name: ", self.name)
        print("Total Score: ", self.totalScore)
        print("Times rolled this turn: ", self.timesRolled)
        print("Is a Computer? : ", self.isComputer)

    def setName(self, name):
        self.name = name
        return self.name

    def getName(self):
        return self.name
    
    def getTotalScore(self):
        return self.totalScore

    def addToTotalScore(self, turnScore):
        self.totalScore = self.totalScore + turnScore

    def getTimesRolled(self):
        return self.timesRolled

    def clearTimesRolled(self):
        self.timesRolled = 0

    def isAComputer(self):
        return self.isComputer
    
    def setTurnNumber(self, turnNumber):
        self.turnNumber = turnNumber
    
    def getTurnNumber(self):
        return self.turnNumber

class Computer(Player):
    def __init__(self, name, totalScore, timesRolled, isComputer, Behavior):
        super().__init__(name, totalScore, timesRolled, isComputer)
        self._nameList = list(["Alexa the Despacito", "SkyNet", "Johnny 5", "Terminator", "Henry the Robot"])
        self.Behavior = Behavior
        self.isComputer = True

    def instantiateName(self):
        self.name = random.choice(self._nameList)

    def actOnBehavior(self):
        if self.Behavior is AIBehaviors.TESTING:
            if self.getTimesRolled() < 5:
                return '1'
            else:
                return '2'
        if self.Behavior is AIBehaviors.NEUTRAL:
            pass
        #pass