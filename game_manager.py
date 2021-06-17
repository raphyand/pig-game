"""Game Manager: Handles all things relating to Pig's internal execution."""
import random
import display_manager
import pdb
from utils import GameState
from player_queue import PlayerQueue



# Holds the rules and back-end game setup
class GameManager():
    """Game Manager: Handles all things relating to Pig's internal execution."""
    def __init__(self):
        self.player_turn_list = PlayerQueue(list())
        self.die = random
        self.user_input = None
        self._current_game_state = GameState.MAIN_MENU
        self._current_score = 0
        self._current_player = None
        self._isolated_input = None

    def set_current_game_state(self, game_state_to_change):
        """Set current Game State"""
        self._current_game_state = game_state_to_change

    def get_current_game_state(self):
        """Get current Game State"""
        return self._current_game_state

    def set_current_score(self, score):
        """Set current score of the turn"""
        self._current_score = score

    def get_current_score(self):
        """Get current score of the turn"""
        return self._current_score

    def get_current_player(self):
        """Get the currently active player"""
        return self._current_player

    def set_current_player(self, player):
        """Set the currently active player"""
        self._current_player = player

    def set_current_player_by_index(self, player_index):
        """Set the currently active player by index"""
        self._current_player = self.player_turn_list.get_index(player_index)

    def receive_input(self):
        """Handle User Input"""
        self.user_input = input(">> ")

    def get_user_input(self):
        """Get User Input Cached Value"""
        return self.user_input

    def roll_dice(self, display_text):
        """Roll dice, with option to display affirmation text."""
        result = self.die.randint(1, 6)
        if display_text is True:
            print("Dice is being rolled...")
            print("Rolled a", result, "\n")
        return result

    def hold(self):
        """Hold the turn, adding current score to total score
        and then setting times rolled to zero"""
        self._current_player.add_to_total_score(self._current_score)
        self._current_player.clear_times_rolled()
        self._current_score = 0

    def core_game_play_loop(self):
        """Core Gameplay Loop method where states are determined and executed"""
        while self.get_current_game_state() is not GameState.GAMEOVER:
            if self.get_current_game_state() is GameState.MAIN_MENU:
                self.main_menu()
            elif self.get_current_game_state() is GameState.PLAYER_SELECTION_MENU:
                self.player_selection_menu()
            elif self.get_current_game_state() is GameState.WHO_GOES_FIRST:
                self.who_goes_first_menu()
            elif self.get_current_game_state() is GameState.TURN_MENU:
                self.turn_menu()
            elif self.get_current_game_state() is GameState.MATCH_END:
                self.match_end_menu()

    def main_menu(self):
        """Main Menu method where Main Menu display and inputs are handled"""
        display_manager.print_main_menu()
        self.receive_input()
        if self.get_user_input() == '1':
            print("SinglePlayer")
            self._mode = 1
            self.set_current_game_state(GameState.PLAYER_SELECTION_MENU)

        elif self.get_user_input() == '2':
            print("Multiplayer")
            self._mode = 2
            self.set_current_game_state(GameState.PLAYER_SELECTION_MENU)

        elif self.get_user_input() == '3':
            self._mode = 3
            self.set_current_game_state(GameState.GAMEOVER)
            print("Game Over!")
        self._isolated_input = self.get_user_input()

    def player_selection_menu(self):
        """Player Selection Menu method where Player Selection display and inputs are handled"""
        valid_input = True
        valid_input2 = True
        should_change_state = False
        #remember_choice = self.user_input

        #While loop for sanity check and determine if Game State should be changed
        while valid_input2 is True and should_change_state is False:
            if self._mode == 1:
                #Register Name if List is empty
                if self.player_turn_list.is_empty():
                    user_name = input("Please enter your name.\n")
                    self.player_turn_list.add_player(user_name)
                valid_input = True
                #While loop sanity check for menu choice
                while valid_input is True:
                    display_manager.print_player_selection()
                    self.receive_input()
                    #When user Input is valid.
                    if str.isalpha(self.user_input):
                        valid_input2 = False
                    #Check if number of Players is valid
                    elif int(self.user_input) > 1 and int(self.user_input) <= 4:
                        for _iterator in range(int(self.user_input) - 1):
                            self.player_turn_list.add_computer()
                        self.set_current_game_state(GameState.WHO_GOES_FIRST)
                        should_change_state = True
                        break
                    #When user input is outside of range.
                    elif int(self.user_input) <= 1 or int(self.user_input) > 4:
                        valid_input = False
                    #When user input is completely invalid
                    else:
                        valid_input = False


            elif self._mode == 2:
                #While loop sanity check for menu choice
                while valid_input is True:
                    display_manager.print_player_selection()
                    self.receive_input()
                    if (str.isalpha(self.user_input)):
                        valid_input = False
                        break
                    amount_of_players = int(self.user_input)
                    if self.user_input == '1':
                        valid_input = False
                        break
                    if int(self.user_input) <= 1 or int(self.user_input) > 4:
                        valid_input = False
                        break
                    else:
                        pass
                    print("How many computers?")
                    self.receive_input()
                    amount_of_computers = int(self.user_input)
                    human_players = amount_of_players - int(amount_of_computers)
                    if human_players <= 0:
                        valid_input = False
                        break
                    #pdb.set_trace()
                    if int(amount_of_computers) + int(human_players) > 4:
                    #or int(amount_of_computers) + int(human_players) < 0):
                        print("Invalid amount of players.")
                        valid_input = False
                        break
                    elif (int(amount_of_computers) + int(human_players) > 0
                    and int(amount_of_computers) + int(human_players) < 5):
                        for _i in range(human_players):
                            user_name = input("Please enter your name.\n")
                            self.player_turn_list.add_player(user_name)
                        for _i in range(int(amount_of_computers)):
                            self.player_turn_list.add_computer()
                        self.set_current_game_state(GameState.WHO_GOES_FIRST)
                        should_change_state = True
                        break
                    else:
                        valid_input = False
                else:
                    valid_input2 = False
            else:
                valid_input2  = False


    def who_goes_first_menu(self):
        """Who-Goes-First Menu method where Who-Goes-First display and inputs are handled"""
        for iterator in self.player_turn_list:
            if iterator.is_a_computer() is False:
                print("Press 1 to roll.")
                self.receive_input()
                if self.user_input == '1':
                    iterator.set_turn_number(self.roll_dice(True))
            elif iterator.is_a_computer() is True:
                iterator.set_turn_number(self.roll_dice(False))

        print("Now adjusting turn order.")
        display_manager.print_transition(3, 0.5)
        self.player_turn_list.sort()
        display_number = 0

        for itera in self.player_turn_list:
            display_number += 1
            print(display_number, ".", itera.get_name())

        self.set_current_player(self.player_turn_list.get_first_player())
        display_manager.print_transition(3, 1)
        self.set_current_game_state(GameState.TURN_MENU)

    def turn_menu(self):
        """Turn Menu method where Turn Menu Selection display and inputs are handled"""
        self.player_turn_list.activate_circular()
        game_won = False
        #Circular For loop to continue until win condition
        for players in self.player_turn_list:
            self._current_player = players
            end_turn_flag = False
            #While loop to repeat rolling and holding
            while end_turn_flag is False:
                if players.is_a_computer() is False:
                    display_manager.print_turn_menu(players.get_name(),
                    players.get_total_score(),self._current_score, players.get_times_rolled())
                    self.receive_input()
                    if self.user_input == '1':
                        result = self.roll_dice(True)
                        players.increment_times_rolled()
                        if result == 1:
                            self._current_score = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!")
                            end_turn_flag = True
                        else:
                            self._current_score = self._current_score + result
                            print("Your current score:", self._current_score)
                    elif self.user_input == '2':
                        if players.get_times_rolled() >= 1:
                            end_turn_flag = True
                            self.hold()
                            if players.get_total_score() >= 100:
                                print(players.get_name(), "you win!")
                                game_won = True
                                break
                            end_turn_flag = True
                        else:
                            print("You must roll at least once.")

                # Handle Computer Turn
                elif players.is_a_computer() is True:
                    self.user_input = players.act_on_behavior()
                    display_manager.print_turn_menu(players.get_name(),
                    players.get_total_score(),self._current_score, players.get_times_rolled())
                    if self.user_input == '1':
                        result = self.roll_dice(True)
                        players.increment_times_rolled()
                        if result == 1:
                            self._current_score = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!\n")
                            display_manager.print_transition(2, 2)
                            end_turn_flag = True
                        else:
                            self._current_score = self._current_score + result
                            display_manager.print_transition(3, 1)
                    elif self.user_input == '2':
                        end_turn_flag = True
                        self.hold()
                        if players.get_total_score() >= 100:
                            print(players.get_name(), "you win!")
                            game_won = True
                            self.set_current_game_state(GameState.MATCH_END)
                            break
                        end_turn_flag = True
            #Break outside external while loop
            if game_won is True:
                break
            display_manager.print_transition(3, 0.8)
        #Terminate match and switch to MATCH_END Menu
        self.set_current_game_state(GameState.MATCH_END)

    def match_end_menu(self):
        """Match End Menu method where Matche End display and inputs are handled"""
        display_manager.print_match_end_menu()
        self.receive_input()
        if self.user_input == '1':
            self.set_current_game_state(GameState.MAIN_MENU)
        elif self.user_input == '2':
            self.set_current_game_state(GameState.GAMEOVER)
