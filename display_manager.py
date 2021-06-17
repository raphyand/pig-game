"""Display Manager: Handles all things relating to Pig's core display features."""
import time

def print_main_menu():
    """Prints Main Menu"""
    print("Hello! Welcome to Pig.")
    print("\t1.SinglePlayer")
    print("\t2.Multiplayer")
    print("\t3.Quit")
    #Instead of myGameManager, pass in an int

def print_turn_menu(player_name, player_total_score,
game_manager_current_score, player_times_rolled):
    """Prints Turn Menu"""
    print(player_name, "\'s Turn")
    print("Total Score:", player_total_score)
    print("Score for the turn:", game_manager_current_score)
    print("Times Rolled:", player_times_rolled)
    print("1. Roll")
    print("2. Hold")
    print("")
def print_player_selection():
    """Prints Player Selection Menu"""
    print("How many players in total are there? (Including Yourself)")
    print("Maximum amount is 4 Players.")
    print("")
def print_transition(dots, time_between):
    """Prints Transition Menu"""
    for _i in range(dots):
        print(".")
        time.sleep(time_between)
def print_match_end_menu():
    """Prints Match End Menu"""
    print("1. Main Menu.")
    print("2. Exit.")
