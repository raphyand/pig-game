"""Player Module which handles data of human and computer players"""
import random
from utils import AiBehaviors
class Player():
    """Player Super Class"""
    def __init__(self, name, total_score, times_rolled, is_computer):
        self.name = name
        self.total_score = total_score
        self.times_rolled = times_rolled
        self.is_computer = is_computer
        self.turn_number = None

    def print_player_sheet(self):
        """Debugging function to print Player Information"""
        print("Name: ", self.name)
        print("Total Score: ", self.total_score)
        print("Times rolled this turn: ", self.times_rolled)
        print("Is a Computer? : ", self.is_computer)

    def set_name(self, name):
        """Set player name"""
        self.name = name
        return self.name

    def get_name(self):
        """Get player name"""
        return self.name

    def get_total_score(self):
        """Get total score of player"""
        return self.total_score

    def add_to_total_score(self, turn_score):
        """Add the turn score to player's total score"""
        self.total_score = self.total_score + turn_score

    def increment_times_rolled(self):
        """Increment times player rolled, by one"""
        self.times_rolled = self.times_rolled + 1

    def get_times_rolled(self):
        """Get times rolled"""
        return self.times_rolled

    def clear_times_rolled(self):
        """Reset roll value to zero"""
        self.times_rolled = 0

    def is_a_computer(self):
        """Check if player is a computer/AI"""
        return self.is_computer

    def set_turn_number(self, turn_number):
        """Set player turn number"""
        self.turn_number = turn_number

    def get_turn_number(self):
        """Get player turn number"""
        return self.turn_number

class Computer(Player):
    """Computer class, which is a subclass of Player"""
    def __init__(self, name, total_score, times_rolled, is_computer, behavior):
        super().__init__(name, total_score, times_rolled, is_computer)
        self._name_list = list(["Alexa the Despacito", "SkyNet",
        "Johnny 5", "Terminator", "Henry the Robot"])
        self.behavior = behavior
        self.is_computer = True

    def instantiate_name(self):
        """Instantiate a name for Computer"""
        self.name = random.choice(self._name_list)

    def act_on_behavior(self):
        """Act on a specific behavior based on Ai Behavior Enums"""
        if self.behavior is AiBehaviors.TESTING:
            if self.get_times_rolled() < 5:
                return '1'
        if self.behavior is AiBehaviors.NEUTRAL:
            if self.get_times_rolled() < 3:
                return '1'
        if self.behavior is AiBehaviors.COCKY:
            if self.get_times_rolled() < 8:
                return '1'
        if self.behavior is AiBehaviors.RESERVED:
            if self.get_times_rolled() < 2:
                return '1'
        if self.behavior is AiBehaviors.AVERAGE:
            if self.get_times_rolled() < 4:
                return '1'
        return '2'
