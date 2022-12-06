import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read()

def part1():

    crates, instructions = input.split("\n\n")
    
    crates_rows = crates.splitlines()
    bottom = len(crates_rows) - 1
    columns = 0
    for c in crates_rows[bottom]:
        try:
            int(c)
            columns = max(columns, int(c))
        except:
            pass
    
    stacks = [] 
    for c in range(0, columns):
        stacks.append([])

    for row in crates_rows:
        for col in range(1, len(row), 2):
            if row[col].isalpha():
                stacks[int(crates_rows[bottom][col])-1].append(row[col])

    for line in instructions.splitlines():
        pieces = line.split(" ")
        num_to_move = int(pieces[1])
        from_column = int(pieces[3]) - 1
        to_column = int(pieces[5]) - 1

        for i in range(0, num_to_move):
            crate = stacks[from_column].pop(0)
            stacks[to_column].insert(0, crate)

    for i in range(0, len(stacks)):
        print(stacks[i][0], end="")

    

    
def part2():
    crates, instructions = input.split("\n\n")
    
    crates_rows = crates.splitlines()
    bottom = len(crates_rows) - 1
    columns = 0
    for c in crates_rows[bottom]:
        try:
            int(c)
            columns = max(columns, int(c))
        except:
            pass
    
    stacks = [] 
    for c in range(0, columns):
        stacks.append([])

    for row in crates_rows:
        for col in range(1, len(row), 2):
            if row[col].isalpha():
                stacks[int(crates_rows[bottom][col])-1].append(row[col])

    for line in instructions.splitlines():
        pieces = line.split(" ")
        num_to_move = int(pieces[1])
        from_column = int(pieces[3]) - 1
        to_column = int(pieces[5]) - 1

        crates_to_move = []
        for i in range(0, num_to_move):
            crates_to_move.append(stacks[from_column].pop(0))
        
        for crate in range (0, len(crates_to_move)):
            stacks[to_column].insert(0, crates_to_move.pop())


    for i in range(0, len(stacks)):
        print(stacks[i][0], end="")

if __name__ == '__main__':
    part1()
    print("\n")
    part2()