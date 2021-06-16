#!/usr/bin/env python3

"""The main program for Pig."""

from GameManager import GameManager

#Main Function
def main():
    """Main Method"""
    my_game_manager = GameManager(0,0)
    my_game_manager.coreGamePlayLoop()

if __name__ == "__main__":
    # execute only if run as a script
    main()
