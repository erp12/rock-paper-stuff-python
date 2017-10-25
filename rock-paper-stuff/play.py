import random


def _tie_breaker(offer1, offer2):
    return random.choice([([offer1, offer2], []), ([], [offer1, offer2])])


def trade_outcome(offer1, offer2) -> (dict, dict):
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
