#!/usr/bin/python3

# Part 1
def points_per_round(round_string):
    opp_shape = map_input1[round_string[0]]
    player_shape = map_input1[round_string[2]]

    if opp_shape == player_shape:
        return points_per_outcome['Draw'] + points_per_shape[player_shape]
    elif (opp_shape, player_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return points_per_outcome['Lose'] + points_per_shape[player_shape]
    else:
        return points_per_outcome['Win'] + points_per_shape[player_shape]

# Part 2
def points_per_round2(round_string):
    opp_shape = map_input2[round_string[0]]
    player_goal = map_input2[round_string[2]]

    if (opp_shape, player_goal) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
        return points_per_outcome[player_goal] + points_per_shape['Rock']
    elif (opp_shape, player_goal) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
        return points_per_outcome[player_goal] + points_per_shape['Paper']
    else:
        return points_per_outcome[player_goal] + points_per_shape['Scissors']

map_input1 = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
map_input2 = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

with open('d2.txt', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

print("Part 1:")
print(sum([points_per_round(round_string) for round_string in rounds]))
print("Part 2:")
print(sum([points_per_round2(round_string) for round_string in rounds]))
f.close()