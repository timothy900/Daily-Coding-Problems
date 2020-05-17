''' Started on March 2 2020, finished March 3, 2020
This problem was asked by Google.

You are writing an AI for a 2D map game.
You are somewhere in a 2D grid, and there
are coins strewn about over the map.

Given the position of all the coins and
your current position, find the closest
coin to you in terms of Manhattan distance.
That is, you can move around up, down, left,
and right, but not diagonally. If there are
multiple possible closest coins, return any
of them.

For example, given the following map,
where you are x, coins are o, and empty
spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------
return (0, 4), since that coin is closest.
This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
'''


import random

coins_positions = []
player_position = []

# generate map
def generate_map(length, coins_chance):
    mapp = []
    player_position.append(random.randint(0,length-1))
    player_position.append(random.randint(0,length-1))
    for i in range(length):
        row = []
        for j in range(length):
            if player_position[1] == j and player_position[0] == i:
                row.append("x")
            elif random.randint(0,100) <= coins_chance:
                row.append("o")
                coins_positions.append((i, j))
            else:
                row.append(".")
        mapp.append(row)
    return mapp


# draw map
def draw_map(map_):
    map_width = len(map_)
    horizontal_line = "-" * ((map_width * 4) + 1)
    for h in range(map_width):
        print(horizontal_line)
        current_row = "| "
        for e in map_[h]:
            current_row += (e + " | ")
        print(current_row)
    print(horizontal_line)


# calculate distances to coins
def calculate_distance(map__):
    distances = [100]
    counts = 0
    closest_coin = []
    for coin in coins_positions:
        #calculate player distance to each coin
        distancex = abs(player_position[1]-coin[1])
        distancey = abs(player_position[0]-coin[0])
        distance = distancex + distancey
        if distance <= distances[counts]:# and distances[counts] != 0:
            closest_coin = (coin[0], coin[1])
            distances.append(distance)
            counts += 1
            closest_distance = distance
    return closest_coin, closest_distance

# run
def run_program():
    mappa = generate_map(5,15)
    draw_map(mappa)
    print("coins positions" + str(coins_positions))
    print("closest coin position, distance" + str(calculate_distance(mappa)))
    print("player position" + str(player_position))

run_program()
