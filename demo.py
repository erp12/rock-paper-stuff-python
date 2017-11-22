from rock_paper_stuff import play_games
from rock_paper_stuff.player import RandomPlayer, SimplePlayer


# --- Play games with all random players ---

# if __name__ == '__main__':
#     players = [RandomPlayer('Random' + str(i)) for i in range(5)]
#     results = play_games(10000, players)
#
#     print(','.join([k for k in results.keys()]))
#     for i in range(len(results['Random1'])):
#         print(','.join([str(results[k][i]) for k in results.keys()]))


# --- Play games with one simple player ---

# if __name__ == '__main__':
#     simple_player = SimplePlayer("Simple")
#     players = [RandomPlayer('Random' + str(i)) for i in range(4)]
#     players.append(simple_player)
#     results = play_games(10000, players)
#
#     print(','.join([k for k in results.keys()]))
#     for i in range(len(results['Random0'])):
#         print(','.join([str(results[k][i]) for k in results.keys()]))


# --- Play games with all simple players ---

if __name__ == '__main__':
    players = [SimplePlayer('Simple' + str(i)) for i in range(5)]
    results = play_games(10000, players)

    print(','.join([k for k in results.keys()]))
    for i in range(len(results['Simple1'])):
        print(','.join([str(results[k][i]) for k in results.keys()]))
