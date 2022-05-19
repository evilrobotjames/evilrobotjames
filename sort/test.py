#!/usr/bin/python3

import random
import seed
from bubble import Bubble
from python_sorted import PythonSorted

ALGORITHMS = [
        PythonSorted(),
        Bubble(),
        ]

random.setstate(seed.SEED)

class Test:
    def __init__(self, length: int):
        self.name = 'random' + str(length)
        self.data = list(range(0, length))
        random.shuffle(self.data)
        self.answer = sorted(self.data)

TEST_DATA = [
        Test(5),
        Test(1000),
        ]



def main():
    # Seed the RNG with something fixed to ensure out test sets remain consistent.
    for alg in ALGORITHMS:
        print(alg.name())
        for test in TEST_DATA:
            response = alg.sort(list(test.data))
            if response != test.answer:
                print("FAIL: {0}".format(test.name))
                print("test.data:    {0}".format(test.data))
                print("test.answer:  {0}".format(test.answer))
                print("response {0}".format(response))
            else:
                print("pass")

if __name__ == '__main__':
    main()
