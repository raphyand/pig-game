"""Game Manager: Handles all things relating to Pig's internal execution."""
import random, pdb
from utils import gameState
from DisplayManager import DisplayManager
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

    def set_current_game_state(self, game_state_to_change):
        self._current_game_state = game_state_to_change
    def get_current_game_state(self):
        return self._current_game_state
    def set_current_score(self, score):
        self._current_score = score
    def get_current_score(self):
        return self._current_score
    def get_current_player(self):
        return self._current_player
    def set_current_player(self, player):
        self._current_player = player
    def set_current_player_by_index(self, player_index):
        self._current_player = self.player_turn_list.getIndex(player_index)
    def receive_input(self):
        self.user_input = input(">> ")

    def get_user_input(self):
        return self.user_input

    def roll_dice(self, display_text):
        result = self.die.randint(1, 6)
        if display_text is True:
            print("Dice is being rolled...")
            print("Rolled a", result, "\n")
        return result

    def hold(self):
        self._current_player.addToTotalScore(self._current_score)
        self._current_player.clearTimesRolled()
        self._current_score = 0

    def core_game_play_loop(self):
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
        self.my_display_manager.printMainMenu()
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
        valid_input = True
        valid_input2 = True
        shouldChangeState = False
        while valid_input2 is True and shouldChangeState is False:
            if self.user_input == '1':
                user_name = input("Please enter your name.\n")
                self.player_turn_list.addPlayer(user_name)
                while valid_input is True:
                    self.my_display_manager.printPlayerSelection()
                    self.receive_input()
                    #pdb.set_trace()
                    #When user Input is valid.
                    if str.isalpha(self.user_input):
                        valid_input2 = False
                    elif int(self.user_input) > 1 and int(self.user_input) <= 4:
                        for iterator in range(int(self.user_input) - 1):
                            self.player_turn_list.addComputer()
                        self.set_current_game_state(gameState.WHO_GOES_FIRST)
                        shouldChangeState = True
                        break
                    #When user input is outside of range.
                    elif int(self.user_input) <= 1 or int(self.user_input) > 4:
                        valid_input = False
                    #When user input is completely invalid
                    else:
                        valid_input = False
            elif self.user_input == '2':
                while valid_input is True:
                    self.my_display_manager.printPlayerSelection()
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
                    
                    if int(amount_of_computers) + int(human_players) > 4 or int(amount_of_computers) + int(human_players) < 0:
                        print("Invalid amount of players.")
                        valid_input = False
                    elif int(amount_of_computers) + int(human_players) > 0 or int(amount_of_computers) + int(human_players) < 5:
                        for i in range(human_players):
                            user_name = input("Please enter your name.\n")
                            self.player_turn_list.addPlayer(user_name)
                            #pdb.set_trace()
                        for i in range(int(amount_of_computers)):
                            self.player_turn_list.addComputer()
                        self.set_current_game_state(gameState.WHO_GOES_FIRST)
                        shouldChangeState = True
                        break
                    else:
                        valid_input = False
                else:
                    valid_input2 = False
            else:
                valid_input2  = False


    def who_goes_first_menu(self):
        for iterator in self.player_turn_list:
            if iterator.isAComputer() is False:
                print("Press 1 to roll.")
                self.receive_input()
                if self.user_input == '1':
                    iterator.setTurnNumber(self.roll_dice(True))

            elif iterator.isAComputer() is True:
                iterator.setTurnNumber(self.roll_dice(False))
        print("Now adjusting turn order.")
        self.my_display_manager.printTransition(3, 0.5)
        self.player_turn_list.sort()
        display_number = 0
        for itera in self.player_turn_list:
            display_number += 1
            print(display_number, ".", itera.getName())

        self.set_current_player(self.player_turn_list.getFirstPlayer())
        #Sleep for a bit
        #time.sleep(1.5)
        self.my_display_manager.printTransition(3, 1)
        self.set_current_game_state(gameState.TURN_MENU)

    def turn_menu(self):
        self.player_turn_list.activateCircular()
        game_won = False
        for players in self.player_turn_list:
            self._current_player = players
            end_turn_flag = False
            #valid_input = True
            while end_turn_flag is False:
                if players.isAComputer() is False:
                    self.my_display_manager.printTurnMenu(players.getName(),
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
                    self.my_display_manager.printTurnMenu(players.getName(),
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
                            self.my_display_manager.printTransition(3, .5)
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
            self.my_display_manager.printTransition(3, 0.5)
        # Terminate here
        self.set_current_game_state(gameState.MATCH_END)

    def resolve_rolling(self, players):
        result = self.roll_dice(True)
        players.incrementTimesRolled()
        if result == 1:
            self._current_score = 0
            self.hold()
            print("You rolled a 1! Tough Luck!")
            return True
            #end_turn_flag = True
        else:
            self._current_score = self._current_score + result
            print("Your current score:", self._current_score)       
    
    def resolve_rolling_computer(self, players):
        result = self.roll_dice(True)
        players.incrementTimesRolled()
        if result == 1:
            self._current_score = 0
            self.hold()
            print("You rolled a 1! Tough Luck!\n")
            #end_turn_flag = True
            return True
        else:
            self._current_score = self._current_score + result
            #time.sleep(1.5)
            self.my_display_manager.printTransition(3, .5)

    def player_turn(self):
        pass
    def computer_turn(self):
        pass
    def match_end_menu(self):
        self.my_display_manager.printMatchEndMenu()
        self.receive_input()
        if self.user_input == '1':
            self.set_current_game_state(gameState.MAIN_MENU)
        elif self.user_input == '2':
            self.set_current_game_state(gameState.GAMEOVER)
