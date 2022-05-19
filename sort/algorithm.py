from typing import List

class Algorithm():
    def __init__(self):
        pass

    def name(self):
        return self.__class__.__name__

    def sort(self, data: List[int]):
        raise NotImplementedError
