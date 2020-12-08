#!/usr/bin/python3

with open('data.txt') as file:
   program = file.read().splitlines()

pc_already_seen = set()
pc = 0
acc = 0

while True:

    # Do we stop?
    if pc in pc_already_seen:
        print("pc:{0}, acc:{1}".format(pc, acc))
        raise Exception()

    # process instructions
    pc_already_seen.add(pc)
    instruction = program[pc]
    op = instruction[:3]
    param = int(instruction[3:])
    if op == 'nop':
        pc += 1
    elif op == 'acc':
        acc += param
        pc += 1
    elif op == 'jmp':
        pc += param

