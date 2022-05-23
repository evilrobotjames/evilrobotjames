#!/usr/bin/python

MAX = 10240

primes = [ True for _ in range(0, MAX) ]

def print_primes(primes):
    render = []
    for i in range(0, MAX):
        if primes[i]:
            render.append(i)
    print(render)

for i in range(2, MAX): # ignore zero and one
    print("doing {}".format(i))
    if primes[i]:
        j = i + i
        while j < MAX:
            if primes[i]:
                print("eliminating {}".format(j))
            else:
                print("{} already eliminated".format(j))
            primes[j] = False
            j = j + i
        print_primes(primes)
    else:
        pass
        print("{} already not a prime".format(i))
