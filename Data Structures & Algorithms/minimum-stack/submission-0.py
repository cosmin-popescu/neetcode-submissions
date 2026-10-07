class StackNode:
    def __init__(self, value: int):
        self.next_item : StackNode | None = None
        self.known_min : int = 2**31 - 1 # should be big enough
        self.val : int = value

class MinStack:
    def __init__(self):
        self.top_item : StackNode | None = None
        self.minimum : int | float = float('inf')
        
    def push(self, val: int) -> None:
        new_node = StackNode(val)
        new_node.known_min = min(val, self.top_item.known_min) if self.top_item is not None else val 
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
        
