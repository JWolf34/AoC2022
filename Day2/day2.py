import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read().splitlines()

def part1():
    WIN = 6
    DRAW = 3
    LOSS = 0

    my_plays = {
        'X': {'loses_to':'B', "draws_to":'A', "points":1 },
        'Y': {'loses_to':'C', "draws_to":'B', "points":2 },
        'Z': {'loses_to':'A', "draws_to": 'C', "points":3 }
    }

    matchups = []

    for line in input:
        matchup = line.split()
        matchups.append((matchup[0], matchup[1]))

    total_score = 0
    for matchup in matchups:
        elf_hand = matchup[0]
        my_hand = matchup[1]

        if elf_hand == my_plays.get(my_hand).get("draws_to"):
            total_score += DRAW + my_plays.get(my_hand).get("points")
        elif elf_hand == my_plays.get(my_hand).get("loses_to"):
            total_score += LOSS + my_plays.get(my_hand).get("points")
        else:
            total_score += WIN + my_plays.get(my_hand).get("points")


    print(total_score)

def part2():
    WIN = 6
    DRAW = 3
    LOSS = 0

    points = {
        "A":1,
        "B":2,
        "C":3
    }

    my_plays = {
        'X': {'A':'C', 'B':'A', 'C':'B'}, #lose
        'Y': {'A':'A', 'B':'B', 'C':'C'}, #draw
        'Z': {'A':'B', 'B': 'C', 'C':'A' } #win
    }

    matchups = []

    for line in input:
        matchup = line.split()
        matchups.append((matchup[0], matchup[1]))

    total_score = 0
    for matchup in matchups:
        elf_hand = matchup[0]
        result = matchup[1]

        if result == 'X':
            total_score += LOSS + points.get(my_plays.get(result).get(elf_hand))
        elif result == 'Y':
            total_score += DRAW + points.get(my_plays.get(result).get(elf_hand))
        else:
            total_score += WIN + points.get(my_plays.get(result).get(elf_hand))


    print(total_score)


if __name__ == '__main__':
    part1()
    part2()