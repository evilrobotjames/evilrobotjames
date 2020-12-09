#!/usr/bin/python3

with open('data.txt') as file:
    lines = file.read().splitlines()

numbers = []
for line in lines:
    numbers.append(int(line))

PREAMBLE = 25

def permute(lower, upper):
    sums = set()
    for i in range(lower, upper):
        for j in range(lower, upper):
            if i != j:
                sums.add(numbers[i] + numbers[j])
    return sums


for i in range(PREAMBLE, len(numbers)):
    valid_numbers = permute(i-PREAMBLE, i)
    print('{0}: {1}'.format(numbers[i], valid_numbers))
    if numbers[i] not in valid_numbers:
        print('FAIL: {0}', numbers[i])
        import sys
        sys.exit()
     





