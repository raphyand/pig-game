from enum import Enum 
from Player import Player, Computer
import pdb

class AIBehaviors(Enum):
    NEUTRAL = 0
    COCKY = 1
    RESERVED = 2
    OPTIMAL = 3
    AVERAGE = 4

class gameState(Enum):
    MAIN_MENU = 0
    PLAYER_SELECTION_MENU = 1
    WHO_GOES_FIRST = 2
    TURN_MENU = 3
    MATCH_END = 4
    GAMEOVER = 5

class playerQueue:
    def __init__(self, player_list):
        self._players = list(player_list)
        self._circular = False
        self._counter = 0
        self._should_stop = False 

    def activateCircular(self):
        self._circular = True
    def deactivateCircular(self):
        self._circular = False
    
    def stop(self):
        self._should_stop = True 

    def __iter__(self):
        return self 
    def __next__(self):

        if self._should_stop:
            raise StopIteration
        if self._counter >= len(self._players) and self._circular is True:
            self._counter = 0
        elif self._counter >= len(self._players) and self._circular is False:
            raise StopIteration 

        player = self._players[self._counter]
        self._counter = self._counter + 1
        return player
    
    def getIndex(self, index):
        if self.isEmpty():
            return None
        return self._players[int(index)]

    def isEmpty(self):
        if len(self._players) == 0:
            return True
        else:
            return False

    def getFirstPlayer(self):
        #pdb.set_trace()
        return self._players[0]

    def isComputer_Generator(self, player):
        for player in self._players:
            yield Player.isAComputer(player)

    def sort(self):
        self._players.sort(key=lambda pq: pq.getTurnNumber(), reverse=True)
    
    def printAll(self):
        for iterator in self._players:
            print(iterator)

    def addPlayer(self, playerName):
        playerToAdd = Player(None, 0, 0, 0, False)
        playerToAdd.setName(playerName)
        self._players.append(playerToAdd)

    def addComputer(self):
        computerToAdd = Computer(None, 0,0,0, True, AIBehaviors.NEUTRAL)
        self._players.append(computerToAdd)

