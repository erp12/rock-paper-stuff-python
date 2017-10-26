from rock_paper_stuff import play_game
from rock_paper_stuff.player import RandomPlayer

if __name__ == '__main__':
    players = [RandomPlayer('Alice'), RandomPlayer('Bob'), RandomPlayer('Cathy')]
    ranked_players = play_game(players)

    print(ranked_players)
    print([p.score() for p in ranked_players])
