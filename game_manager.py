"""Game Manager: Handles all things relating to Pig's internal execution."""
import random
from utils import gameState
from display_manager import DisplayManager
from playerQueue import playerQueue



# Holds the rules and back-end game setup
class GameManager():
    """Game Manager: Handles all things relating to Pig's internal execution."""
    def __init__(self):
        self.player_turn_list = playerQueue(list())
        self.die = random
        self.my_display_manager = DisplayManager()
        self.user_input = None
        self._current_game_state = gameState.MAIN_MENU
        self._current_score = 0
        self._current_player = None

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
        self._current_player = self.player_turn_list.getIndex(player_index)
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
        self._current_player.addToTotalScore(self._current_score)
        self._current_player.clearTimesRolled()
        self._current_score = 0

    def core_game_play_loop(self):
        """Core Gameplay Loop method where states are determined and executed"""
        while self.get_current_game_state() is not gameState.GAMEOVER:
            if self.get_current_game_state() is gameState.MAIN_MENU:
                self.main_menu()
            elif self.get_current_game_state() is gameState.PLAYER_SELECTION_MENU:
                self.player_selection_menu()
            elif self.get_current_game_state() is gameState.WHO_GOES_FIRST:
                self.who_goes_first_menu()
            elif self.get_current_game_state() is gameState.TURN_MENU:
                self.turn_menu()
            elif self.get_current_game_state() is gameState.MATCH_END:
                self.match_end_menu()

    def main_menu(self):
        """Main Menu method where Main Menu display and inputs are handled"""
        self.my_display_manager.print_main_menu()
        self.receive_input()
        if self.get_user_input() == '1':
            print("SinglePlayer")
            self.set_current_game_state(gameState.PLAYER_SELECTION_MENU)

        elif self.get_user_input() == '2':
            print("Multiplayer")
            self.set_current_game_state(gameState.PLAYER_SELECTION_MENU)

        elif self.get_user_input() == '3':
            self.set_current_game_state(gameState.GAMEOVER)
            print("Game Over!")

    def player_selection_menu(self):
        """Player Selection Menu method where Player Selection display and inputs are handled"""
        valid_input = True
        valid_input2 = True
        should_change_state = False
        while valid_input2 is True and should_change_state is False:
            if self.user_input == '1':
                user_name = input("Please enter your name.\n")
                self.player_turn_list.addPlayer(user_name)
                while valid_input is True:
                    self.my_display_manager.print_player_selection()
                    self.receive_input()
                    #When user Input is valid.
                    if str.isalpha(self.user_input):
                        valid_input2 = False
                    elif int(self.user_input) > 1 and int(self.user_input) <= 4:
                        for _iterator in range(int(self.user_input) - 1):
                            self.player_turn_list.addComputer()
                        self.set_current_game_state(gameState.WHO_GOES_FIRST)
                        should_change_state = True
                        break
                    #When user input is outside of range.
                    elif int(self.user_input) <= 1 or int(self.user_input) > 4:
                        valid_input = False
                    #When user input is completely invalid
                    else:
                        valid_input = False
            elif self.user_input == '2':
                while valid_input is True:
                    self.my_display_manager.print_player_selection()
                    self.receive_input()
                    amount_of_players = int(self.user_input)
                    if int(self.user_input) <= 1 or int(self.user_input) > 4:
                        valid_input = False
                    else:
                        valid_input = False
                    print("How many computers?")
                    self.receive_input()
                    amount_of_computers = int(self.user_input)
                    human_players = amount_of_players - int(amount_of_computers)
                    if (int(amount_of_computers) + int(human_players) > 4
                    or int(amount_of_computers) + int(human_players) < 0):
                        print("Invalid amount of players.")
                        valid_input = False
                    elif (int(amount_of_computers) + int(human_players) > 0
                    or int(amount_of_computers) + int(human_players) < 5):
                        for _i in range(human_players):
                            user_name = input("Please enter your name.\n")
                            self.player_turn_list.addPlayer(user_name)
                        for _i in range(int(amount_of_computers)):
                            self.player_turn_list.addComputer()
                        self.set_current_game_state(gameState.WHO_GOES_FIRST)
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
            if iterator.isAComputer() is False:
                print("Press 1 to roll.")
                self.receive_input()
                if self.user_input == '1':
                    iterator.setTurnNumber(self.roll_dice(True))
            elif iterator.isAComputer() is True:
                iterator.setTurnNumber(self.roll_dice(False))
        print("Now adjusting turn order.")
        self.my_display_manager.print_transition(3, 0.5)
        self.player_turn_list.sort()
        display_number = 0
        for itera in self.player_turn_list:
            display_number += 1
            print(display_number, ".", itera.getName())

        self.set_current_player(self.player_turn_list.getFirstPlayer())
        self.my_display_manager.print_transition(3, 1)
        self.set_current_game_state(gameState.TURN_MENU)

    def turn_menu(self):
        """Turn Menu method where Turn Menu Selection display and inputs are handled"""
        self.player_turn_list.activateCircular()
        game_won = False
        for players in self.player_turn_list:
            self._current_player = players
            end_turn_flag = False
            #valid_input = True
            while end_turn_flag is False:
                if players.isAComputer() is False:
                    self.my_display_manager.print_turn_menu(players.getName(),
                    players.getTotalScore(),self._current_score, players.getTimesRolled())
                    self.receive_input()
                    if self.user_input == '1':
                        result = self.roll_dice(True)
                        players.incrementTimesRolled()
                        if result == 1:
                            self._current_score = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!")
                            #return True
                            end_turn_flag = True
                        else:
                            self._current_score = self._current_score + result
                            print("Your current score:", self._current_score)
                        #end_turn_flag = self.resolve_rolling(players)
                    elif self.user_input == '2':
                        end_turn_flag = True
                        #Program a Hold
                        self.hold()
                        if players.getTotalScore() >= 100:
                            print(players.getName(), "you win!")
                            game_won = True
                            break
                        end_turn_flag = True
                elif players.isAComputer() is True:
                    self.user_input = players.actOnBehavior()
                    self.my_display_manager.print_turn_menu(players.getName(),
                    players.getTotalScore(),self._current_score, players.getTimesRolled())
                    if self.user_input == '1':
                        result = self.roll_dice(True)
                        players.incrementTimesRolled()
                        if result == 1:
                            self._current_score = 0
                            self.hold()
                            print("You rolled a 1! Tough Luck!\n")
                            end_turn_flag = True
                            #return True
                        else:
                            self._current_score = self._current_score + result
                            #time.sleep(1.5)
                            self.my_display_manager.print_transition(3, .5)
                    elif self.user_input == '2':
                        end_turn_flag = True
                        self.hold()
                        if players.getTotalScore() >= 100:
                            print(players.getName(), "you win!")
                            #game_won = True
                            self.set_current_game_state(gameState.MATCH_END)
                            break
                        end_turn_flag = True
            if game_won is True:
                break
            self.my_display_manager.print_transition(3, 0.5)
        # Terminate here
        self.set_current_game_state(gameState.MATCH_END)
    def match_end_menu(self):
        """Match End Menu method where Matche End display and inputs are handled"""
        self.my_display_manager.print_match_end_menu()
        self.receive_input()
        if self.user_input == '1':
            self.set_current_game_state(gameState.MAIN_MENU)
        elif self.user_input == '2':
            self.set_current_game_state(gameState.GAMEOVER)
