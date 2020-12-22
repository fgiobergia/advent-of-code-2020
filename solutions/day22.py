import sys
# first time (probably ever) where increasing the
# recursion limit actually makes a difference between 
# finishing and hitting RecursionError. 
# (Not that I have spent ~1h trying to figure out what 
# else could be the problem...)
sys.setrecursionlimit(12000)

def play(players):
    while True: # until one wins
        cards = players[0].pop(0), players[1].pop(0)
        round_winner = cards[1]>cards[0] # round winner
        players[round_winner].extend([cards[round_winner], cards[not round_winner]])
        if not players[not round_winner]:
            return players[round_winner]

def recursive_play(players, prev_states):
    if (tuple(players[0]), tuple(players[1])) in prev_states:
        return 0
    prev_states.add((tuple(players[0]), tuple(players[1])))
    
    cards = players[0].pop(0), players[1].pop(0)   

    if len(players[0])<cards[0] or len(players[1])<cards[1]:
        # print("at least one player cannot continue")
        round_winner = cards[1]>cards[0]
    else:
        # else, play a subgame!
        p = {
            0: players[0][:cards[0]],
            1: players[1][:cards[1]]
        }
        round_winner = recursive_play(p, set())

    players[round_winner].extend([cards[round_winner], cards[not round_winner]])
    if not players[not round_winner]:
        return round_winner
    
    return recursive_play(players, prev_states)

if __name__ == "__main__":
    with open("day22.input") as f:
        players = {0: [], 1: []}
        for i in [0,1]:
            f.readline() # Player [i]
            while True:
                line = f.readline().strip()
                if not line:
                    break
                players[i].append(int(line))
    
    players_copy = { k: v.copy() for k,v in players.items() }
    winner = play(players)
    print(sum([b*(len(winner)-a) for a,b in enumerate(winner) ]))

    players = players_copy
    winner = recursive_play(players, set())
    print(sum([b*(len(players[winner])-a) for a,b in enumerate(players[winner]) ]))
