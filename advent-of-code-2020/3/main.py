#!/usr/bin/python3

with open("data.txt") as data:
    lines = data.readlines()

position = 0
width = None
trees_encountered = 0

for line in lines:

    line = line.strip()
    # Width calc
    if width is None:
        width = len(line)
        print("width: {0}".format(width))
    else:
        assert(width == len(line))

    # Tree or not
    modified_line = line
    if modified_line[position] == '.':
        modified_line = line[:position] + 'O' + line[position+1:]
    else:
        modified_line = line[:position] + 'X' + line[position+1:]
        trees_encountered += 1
    print(line)
    print(modified_line)

    # Next iteration
    position += 3
    position = position % width

print(trees_encountered)
