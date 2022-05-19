from typing import List
from algorithm import Algorithm

class PythonSorted(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)

    def sort(self, data: List[int]) -> List[int]:
        return sorted(data)
