#!/usr/bin/python3

with open('data.txt') as file:
   program_original = file.read().splitlines()


class Broken(Exception):
    pass


def run(program):
    
    pc_already_seen = set()
    pc = 0
    acc = 0
    
    while True:
    
        # Loop detected
        if pc in pc_already_seen:
            print("Loop.  acc:{0}".format(acc))
            raise Broken()
    
        # Reached the end
        if pc >= len(program):
            print('End.  acc:{0}'.format(acc))
            import sys
            sys.exit(0)
    
        # SigSegv
        if pc not in range(len(program)):
            print("SigSegv")
            raise Broken()

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


for inst_to_modify in range(len(program_original)):
    program = list(program_original)
    inst = program[inst_to_modify]
    op = inst[:3]
    param = inst[3:]
    print("{0}: {1} {2}".format(inst_to_modify, op, param))
   
    if op == 'acc':
        print('Ignoring.')
        continue 
    elif op == 'nop':
        program[inst_to_modify] = 'jmp' + param
    elif op == 'jmp':
        program[inst_to_modify] = 'nop' + param

    try:        
        run(program)
    except Broken:
        pass
    
