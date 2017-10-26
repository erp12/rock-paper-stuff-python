from abc import ABC, abstractmethod
import numpy as np
import random

from .util import deviance


class Player(ABC):

    def __init__(self, name):
        self.inventory = {'R': 0, 'P': 0, 'S': 0, 'F': 0, 'W': 0}
        self.name = name

    def is_alive(self):
        for resource in self.inventory:
            if self.inventory[resource] > 0:
                return True
        return False

    def accept_resources(self, resources):
        for resource in resources:
            self.inventory[resource] += 1

    def take_turn(self, other_player):
        offer = self.strategy(other_player)
        if self.inventory[offer] <= 0:
            raise ValueError("Player {n} offered resource it does not have.".format(n=self.name))
        self.inventory[offer] -= 1
        return offer

    def score(self):
        if not self.is_alive():
            return 1e10
        return deviance(np.array(list(self.inventory.values())))

    @abstractmethod
    def strategy(self, other_player):
        ...

    def __repr__(self):
        return '{n}<{i}>'.format(
            n=self.name,
            i=self.inventory.__repr__().replace(" ", "").replace("'", "")[1:-1])


class RandomPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def strategy(self, other_player):
        options = []
        for resource in self.inventory.keys():
            if self.inventory[resource] > 0:
                options.append(resource)
        return random.choice(options)


class UserPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def strategy(self, other_player):
        ...


class UserDefinedPlayer(Player):

    def __init__(self, name, strategy_function):
        super().__init__(name)
        self.strategy_function = strategy_function

    def strategy(self, other_player):
        return self.strategy_function(self.inventory,
                                      self.other_player.inventory,
                                      self.other_player.name)
