from typing import List
from algorithm import Algorithm

class Bubble(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)

    def sort(self, data: List[int]) -> List[int]:
        switch_happened = True
        while switch_happened:
            switch_happened = False
            for index in range(0, len(data) - 1):
                if data[index] > data[index+1]:
                    temp = data[index+1]
                    data[index+1] = data[index]
                    data[index] = temp
                    switch_happened = True
        return data
