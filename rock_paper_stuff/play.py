import random

from .player import Player


def _tie_breaker(offer1: str, offer2: str) -> (list, list):
    return random.choice([([offer1, offer2], []), ([], [offer1, offer2])])


def trade_outcome(offer1: str, offer2: str) -> (list, list):
    # TODO: This is ugly. Attempt to clean up later.
    if offer1 == 'R':
        if offer2 == 'R':
            return _tie_breaker(offer1, offer2)
        elif offer2 == 'P':
            return (['P'], ['R'])
        elif offer2 == 'S':
            return (['F'], ['R'])
        elif offer2 == 'W':
            return ([], ['W', 'W'])
        elif offer2 == 'F':
            return (['R'], ['S'])
    elif offer1 == 'P':
        if offer2 == 'R':
            return (['R'], ['P'])
        elif offer2 == 'P':
            return _tie_breaker(offer1, offer2)
        elif offer2 == 'S':
            return (['P', 'P'], ['S'])
        elif offer2 == 'W':
            return (['P'], [])
        elif offer2 == 'F':
            return ([], ['F', 'F'])
    elif offer1 == 'S':
        if offer2 == 'R':
            return (['R'], ['F'])
        elif offer2 == 'P':
            return (['S'], ['P', 'P'])
        elif offer2 == 'S':
            return _tie_breaker(offer1, offer2)
        elif offer2 == 'W':
            return (['W'], ['R'])
        elif offer2 == 'F':
            return (['S', 'S'], ['F'])
    elif offer1 == 'F':
        if offer2 == 'R':
            return (['S'], ['R'])
        elif offer2 == 'P':
            return (['F', 'F'], [])
        elif offer2 == 'S':
            return (['F'], ['S', 'S'])
        elif offer2 == 'W':
            return ([], ['W'])
        elif offer2 == 'F':
            return _tie_breaker(offer1, offer2)
    elif offer1 == 'W':
        if offer2 == 'R':
            return (['W', 'W'], [])
        elif offer2 == 'P':
            return ([], ['P'])
        elif offer2 == 'S':
            return (['R'], ['W'])
        elif offer2 == 'W':
            return _tie_breaker(offer1, offer2)
        elif offer2 == 'F':
            return (['W'], [])


def trade(player1: Player, player2: Player):
    p1_offer = player1.take_turn(player2)
    p2_offer = player2.take_turn(player1)
    result = trade_outcome(p1_offer, p2_offer)
    player1.accept_resources(result[0])
    player2.accept_resources(result[1])


def pair_players(players: list) -> list:
    alive_players = [p for p in players if p.is_alive()]
    p1 = random.choice(alive_players)
    alive_players.remove(p1)
    p2 = random.choice(alive_players)
    return (p1, p2)
