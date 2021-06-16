#!/usr/bin/env python3

"""The main program for Pig."""

from game_manager import GameManager

#Main Function
def main():
    """Main Method"""
    my_game_manager = GameManager()
    my_game_manager.core_game_play_loop()

if __name__ == "__main__":
    # execute only if run as a script
    main()
