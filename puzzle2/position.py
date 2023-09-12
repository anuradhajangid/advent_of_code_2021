
import sys
import os

def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        data = [x.strip() for x in myfile]
        return [tuple(item.split(" ")) for item in data]
    
def measureDistance(data):
    horizontal = depth = aim = 0
    for item in data:
        match item[0]:
            case 'forward':
                horizontal += int(item[1])
                depth += aim * int(item[1])
                break
            case 'up':
                aim -= int(item[1])
                break
            case 'down':
                aim += int(item[1])
                break
            case _:
                raise Exception(f"unknown: {item[0]}")
                return
    return (horizontal, depth)
            
    
if __name__ == '__main__':
    input = readInput("input.txt")
    measurement =  measureDistance(input)
    print(measurement)
    print(measurement[0] * measurement[1])