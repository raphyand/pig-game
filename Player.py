class Player():
    def __init__(self, name, currentScore, totalScore, timesRolled):
        self.name = name
        self.currentScore = currentScore
        self.totalScore = totalScore
        self.timesRolled = timesRolled
    
    def printPlayerSheet(self):
        print("Name: ", self.name)
        print("Current Score: ", self.currentScore)
        print("Total Score: ", self.totalScore)
        print("Times rolled this turn: ", self.timesRolled)

    def getCurrentScore(self):
        return self.currentScore
    
    def getTotalScore(self):
        return self.totalScore

    def getTimesRolled(self):
        return self.timesRolled
    