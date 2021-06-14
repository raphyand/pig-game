import utils
class Player():
    def __init__(self, name, currentScore, totalScore, timesRolled, isComputer):
        self.name = name
        self.currentScore = currentScore
        self.totalScore = totalScore
        self.timesRolled = timesRolled
        self.isComputer = isComputer
    
    def printPlayerSheet(self):
        print("Name: ", self.name)
        print("Current Score: ", self.currentScore)
        print("Total Score: ", self.totalScore)
        print("Times rolled this turn: ", self.timesRolled)
        print("Is a Computer? : ", self.isComputer)

    def getCurrentScore(self):
        return self.currentScore
    
    def getTotalScore(self):
        return self.totalScore

    def getTimesRolled(self):
        return self.timesRolled

class Computer(Player):
    def __init__(self, name, currentScore, totalScore, timesRolled, isComputer, Behavior):
        super().__init__(name, currentScore, totalScore, timesRolled, isComputer)
        self.Behavior = Behavior

    