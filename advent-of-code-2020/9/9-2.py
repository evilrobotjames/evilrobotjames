#!/usr/bin/python3

target = 85848519
#target = 127

with open('data.txt') as file:
    lines = file.read().splitlines()

numbers = []
for line in lines:
    numbers.append(int(line))

def check_range(lower, upper):
    sublist = numbers[lower:upper]
    print(sublist)
    return sum(sublist), sum((min(sublist), max(sublist)))


seq_len = 2

while seq_len < len(numbers):
    print('seq_len: {0}'.format(seq_len))
    for i in range(len(numbers) - seq_len):
        lower = i
        upper = i + seq_len
        sum_all, sum_minmax = check_range(lower, upper)
        if sum_all == target:
            print("awooga")
            print(sum_minmax)
            import sys
            sys.exit()
    seq_len += 1 





