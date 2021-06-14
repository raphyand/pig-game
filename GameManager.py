import random

# Holds the rules and back-end game setup
class GameManager():
    def __init__(self, m, hS):
        self.mode = m
        self.highestScore = hS
        self.turnList = []
        self.die = random

    def setMode(modeValue):
        self.mode = modeValue

    def rollDice(self):
        #result = random.randrange(0, 5)
        result = self.die.randint(1, 6)
        print("Dice is being rolled...")
        print("Rolled a", result)
        return result
