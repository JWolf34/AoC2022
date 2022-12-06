import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read().splitlines()

def part1():

    matches = []
    for rucksack in input:
        comp_1 = rucksack[len(rucksack)//2:]
        comp_2 = rucksack[:len(rucksack)//2]
        
        for item in comp_1:
            if item in comp_2:
                matches.append(get_priority(item))
                break

    print(sum(matches))
            

    

def part2():
    matches = []
    for i in range(0, len(input), 3):
        rucksack1 = input[i]
        rucksack2 = input[i+1]
        rucksack3 = input[i+2]
        
        for item in rucksack1:
            if (item in rucksack2) and (item in rucksack3):
                matches.append(get_priority(item))
                break

    print(sum(matches))

def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

if __name__ == '__main__':
    part1()
    part2()