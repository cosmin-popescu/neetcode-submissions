class StackNode:
    __slots__ = ('next_item', 'known_min', 'val')

    def __init__(self, value: int, known_min: int):
        self.next_item : StackNode | None = None
        self.known_min : int = min(value, known_min)
        self.val : int = value

class MinStack:
    def __init__(self):
        self.top_item : StackNode | None = None
        self.minimum : int = 2**31 - 1 # should be big enough
        
    def push(self, val: int) -> None:
        if self.top_item is not None:
            new_node = StackNode(val, self.top_item.known_min)
        else:
            new_node = StackNode(val, self.minimum)
            
        new_node.next_item = self.top_item
        self.top_item = new_node

    def pop(self) -> None:
        if self.top_item is not None:
            self.top_item = self.top_item.next_item

    def top(self) -> int:
        assert self.top_item is not None
        return self.top_item.val

    def getMin(self) -> int:
        assert self.top_item is not None
        return self.top_item.known_min
        
