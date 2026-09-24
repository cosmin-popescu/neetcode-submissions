from typing import Optional

# It's python, therefore we can use a lot of pre-built stuff.
# Which I don't like, because it takes the fun out.

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.elements: list[Optional[int]] = [None] * capacity

    def get(self, i: int) -> Optional[int]:
        return self.elements[i]

    def set(self, i: int, n: int) -> None:
        self.elements[i] = n

    def pushback(self, n: int) -> None:
        # Check capacity
        if self.size == self.capacity:
            self.resize()
        self.elements[self.size] = n
        self.size += 1

    def popback(self) -> Optional[int]:
        # Remove last elem and decrease size
        value = self.elements[self.size-1]
        self.elements[self.size-1] = None
        self.size -= 1
        return value

    def resize(self) -> None:
        # Double capacity
        self.elements += [None] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
