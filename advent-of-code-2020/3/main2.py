#!/usr/bin/python3

with open("data.txt") as data:
    lines = data.read().splitlines()

def traverse(x, y):

    position = 0
    width = None
    trees_encountered = 0
    
    line_number = 0
    
    for line in lines:
    
        print('{0}:{1}: {2}\n'.format(line_number, line_number % y, line))

        if line_number % y != 0:
            line_number += 1
            continue

        line_number += 1
    
        line = line.strip()
        # Width calc
        if width is None:
            width = len(line)
        else:
            assert(width == len(line))
    
        # Tree or not
        modified_line = line
        if modified_line[position] == '.':
            modified_line = line[:position] + 'O' + line[position+1:]
        else:
            modified_line = line[:position] + 'X' + line[position+1:]
            trees_encountered += 1
        print(modified_line)
    
        # Next iteration
        position += x
        position = position % width
    
    return trees_encountered


trees_1_1 = traverse(1,1)
trees_3_1 = traverse(3,1)
trees_5_1 = traverse(5,1)
trees_7_1 = traverse(7,1)
trees_1_2 = traverse(1,2)



print("1,1: {0}".format(trees_1_1))
print("3,1: {0}".format(trees_3_1))
print("5,1: {0}".format(trees_5_1))
print("7,1: {0}".format(trees_7_1))
print("1,2: {0}".format(trees_1_2))

print("total: {0}".format(trees_1_1 * trees_3_1 * trees_5_1 * trees_7_1 * trees_1_2))
