from .play import pair_players, trade


def play_game(players: list) -> list:

    # Initialize resources
    for p in players:
        p.accept_resources(['R', 'P', 'S', 'F', 'W']*len(players))

    # Perform trades
    n_turns = int(100 * ((len(players) - 1) / 2))
    for turn_ndx in range(n_turns):
        p1, p2 = pair_players(players)
        trade(p1, p2)

    return sorted(players, key=lambda x: x.score())
