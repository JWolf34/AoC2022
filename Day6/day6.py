import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"input.txt"))) as f:
    input = f.read()

def part1():
    marker = []

    for i in range(0, len(input)):
        marker.insert(0, input[i])
        if len(marker) > 4:
            marker.pop()
        
            valid_marker = True
            for char in marker:
                if marker.count(char) > 1:
                    valid_marker = False
                    break
            
            if valid_marker:
                print(i+1)
                print(marker)
                break
        

def part2():
    marker = []

    for i in range(0, len(input)):
        marker.insert(0, input[i])
        if len(marker) > 14:
            marker.pop()
        
            valid_marker = True
            for char in marker:
                if marker.count(char) > 1:
                    valid_marker = False
                    break
            
            if valid_marker:
                print(i+1)
                print(marker)
                break

if __name__ == '__main__':
    part1()
    part2()