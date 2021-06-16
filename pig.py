#!/usr/bin/env python3


#Should have classes: 
#   Dice
#   Game Manager
#   Player
#       Computer
#   Score Board
#   Display Manager


from GameManager import GameManager

def main():

    myGameManager = GameManager(0,0)
    myGameManager.coreGamePlayLoop()

if __name__ == "__main__":
    # execute only if run as a script
    main()

