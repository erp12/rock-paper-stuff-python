from .play import pair_players, trade


RESOURCE_NAMES = ['R', 'P', 'S', 'F', 'W']


def play_game(players: list) -> list:

    # Initialize resources
    for p in players:
        p.reset()
        p.accept_resources(RESOURCE_NAMES * len(players))

    # Perform trades
    n_turns = int(100 * ((len(players) - 1) / 2))
    for turn_ndx in range(n_turns):
        p1, p2 = pair_players(players)
        trade(p1, p2)

    return sorted(players, key=lambda x: x.score())


def play_games(n_games: int, players: list) -> dict:
    results = {}
    for player in players:
        results[player.name] = []

    for i in range(n_games):
        ranking = play_game(players)
        for rank, player in enumerate(ranking):
            results[player.name].append(rank + 1)
    return results
