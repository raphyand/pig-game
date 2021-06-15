from enum import Enum 
class AIBehaviors(Enum):
    NEUTRAL = 0
    COCKY = 1
    RESERVED = 2
    OPTIMAL = 3
    AVERAGE = 4

class playerQueue:
    def __init__(self, player_list):
        self._players = player_list
        self._counter = 0
        self._should_stop = False 

    def stop(self):
        self._should_stop = True 
    def __iter__(self):
        return self 
    def __next__(self):
        if self._should_stop:
            raise StopIteration
        if self._counter >= len(self._players):
            self._counter = 0
        player = self._players[self._counter]
        self._counter = self._counter + 1
        return player