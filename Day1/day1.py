import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read().splitlines()

def part1():
    max_calories = 0
    current_calories = 0
    for i in range(0, len(input)):
        
        if input[i] == '':
            max_calories = max(max_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(input[i])

    print(max_calories)

def part2():
    max_calories = [0,0,0]
    current_calories = 0
    for i in range(0, len(input)):
        if input[i] == '':
            if(current_calories > min(max_calories)):
                max_calories[0] = current_calories
                max_calories.sort()
            current_calories = 0
        else:
            current_calories += int(input[i])

    print(str(sum(max_calories)))

if __name__ == '__main__':
    part1()
    part2()