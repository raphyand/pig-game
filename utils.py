from enum import Enum 

class AIBehaviors(Enum):
    TESTING = -1
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

