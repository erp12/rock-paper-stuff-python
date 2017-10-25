from abc import ABC, abstractmethod
import random


class Player(ABC):

    inventory = {'R': 0, 'P': 0, 'S': 0, 'F': 0, 'W': 0}

    def __init__(self, name):
        self.name = name

    def change_inventory(self, delta):
        for resource in delta['-']:
            self.inventory[resource] -= 1
        for resource in delta['+']:
            self.inventory[resource] += 1

    def take_turn(self, other_player):
        offer = self.strategy(other_player)
        if self.inventory[offer] <= 0:
            raise ValueError("Player {n} offered resource it does not have.".format(n=self.name))
        self.inventory[offer] -= 1
        return offer

    @abstractmethod
    def strategy(self, other_player):
        ...


class RandomPlayer(Player):

    def strategy(self, other_player):
        options = []
        for resource in self.inventory.keys():
            if self.inventory[resource] > 0:
                options.append(resource)
        return random.choice(options)
