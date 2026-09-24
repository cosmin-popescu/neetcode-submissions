class ListNode:
    def __init__(self, data = 0):
        self.data = data
        self.next_node : ListNode | None = None # Or use Optional like advanced mammals

class LinkedList:
    
    def __init__(self):
        self.head : ListNode | None = None
    
    def get(self, index: int) -> int:
        # ensure we have what to work with
        if self.head is not None:
            node = self.head
        else:
            return -1
        # Traverse list using .next_node
        for _ in range(0, index):
            # Out of bounds!
            if node.next_node is not None:
                node = node.next_node
            else:
                return -1
        return node.data

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next_node = self.head
        self.head = new_node
        return

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        # check for empty list
        if self.head is None:
            self.head = new_node
            return
        else:
            # go to the end
            node = self.head
            while node.next_node is not None:
                node = node.next_node
            node.next_node = new_node
            return

    def remove(self, index: int) -> bool:
        # Empty list
        if self.head is None:
            return False

        dummy = ListNode()
        dummy.next_node = self.head

        chaser = dummy
        walker = self.head
        
        for _ in range(index):
            if walker is not None:
                chaser = walker
                walker = walker.next_node
            else:
                # Out of bounds
                return False

        # walked off
        if walker is None:
            return False

        chaser.next_node = walker.next_node
        self.head = dummy.next_node

        return True

    def getValues(self) -> List[int]:
        walker = self.head
        values = []
        while walker is not None:
            values.append(walker.data)
            walker = walker.next_node
        return values
