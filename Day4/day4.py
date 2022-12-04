import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read().splitlines()

def part1():

    overlaps = 0

    for line in input:
        pairs = line.split(",")
        sections1 = pairs[0].split("-")
        sections2 = pairs[1].split("-")

        lower_bounds = (int(sections1[0]), int(sections2[0]))
        upper_bounds = (int(sections1[1]), int(sections2[1]))

        if (lower_bounds[0] <= lower_bounds[1]) and (upper_bounds[0] >= upper_bounds[1]):
            overlaps += 1
        elif (lower_bounds[1] <= lower_bounds[0]) and (upper_bounds[1] >= upper_bounds[0]):
            overlaps += 1

    print(overlaps)




def part2():
    overlaps = 0

    for line in input:
        pairs = line.split(",")
        sections1 = pairs[0].split("-")
        sections2 = pairs[1].split("-")

        lower_bounds = (int(sections1[0]), int(sections2[0]))
        upper_bounds = (int(sections1[1]), int(sections2[1]))

        if (lower_bounds[0] <= lower_bounds[1]) and (upper_bounds[0] >= upper_bounds[1]):
            overlaps += 1
        elif (lower_bounds[1] <= lower_bounds[0]) and (upper_bounds[1] >= upper_bounds[0]):
            overlaps += 1

    print(overlaps)

if __name__ == '__main__':
    part1()
    part2()