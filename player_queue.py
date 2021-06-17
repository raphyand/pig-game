"""Player Queue module custom player queue data structure, using a list."""
import random
from player import Player, Computer
from utils import AiBehaviors
class PlayerQueue:
    """Player Queue class."""
    def __init__(self, player_list):
        self._players = list(player_list)
        self._circular = False
        self._counter = 0
        self._should_stop = False

    def activate_circular(self):
        """Activate circular traversal of list."""
        self._circular = True
    def deactivate_circular(self):
        """Deactivate circular traversal of list."""
        self._circular = False

    def stop(self):
        """Stop for iteration"""
        self._should_stop = True
    def __iter__(self):
        """Custom Iterator"""
        return self
    def __next__(self):
        """Custom traversal __next__ to handle circular traversal options."""
        if self._should_stop:
            raise StopIteration
        if self._counter >= len(self._players) and self._circular is True:
            self._counter = 0
        elif self._counter >= len(self._players) and self._circular is False:
            self._counter = 0
            raise StopIteration
        player = self._players[self._counter]
        self._counter = self._counter + 1
        return player

    def get_index(self, index):
        """Get Index of list"""
        if self.is_empty():
            return None
        return self._players[int(index)]

    def is_empty(self):
        """Check if list is empty"""
        return bool(len(self._players) == 0)
        #if len(self._players) == 0:
        #    return True
        #else:
        #    return False

    def get_first_player(self):
        """Get first player of the list"""
        return self._players[0]

    def is_computer_generator(self, player):
        """Computer Generator for certain use-cases."""
        for _player in self._players:
            yield Player.is_a_computer(player)

    def sort(self):
        """Sort Player queue in descending order."""
        self._players.sort(key=lambda pq: pq.get_turn_number(), reverse= False)

    def print_all(self):
        """Print all players."""
        for iterator in self._players:
            print(iterator)

    def add_player(self, player_name):
        """Add a human player to the queue."""
        player_to_add = Player(None, 0, 0, False)
        player_to_add.set_name(player_name)
        self._players.append(player_to_add)

    def add_computer(self):
        """Add Computer Player to the queue"""
        computer_to_add = Computer(None, 0,0, True, random.choice(list(AiBehaviors)))
        #computer_to_add = Computer(None, 99,0, True, AiBehaviors.RESERVED)
        computer_to_add.instantiate_name()
        self._players.append(computer_to_add)
