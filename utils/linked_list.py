class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node at the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def remove(self, target, key=lambda x: x):
        """
        Remove the first node whose key(node.data) == target.
        Returns True if removal was successful, False otherwise.
        """
        current = self.head
        prev = None
        while current:
            if key(current.data) == target:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def find(self, target, key=lambda x: x):
        """
        Return the first node's data where key(node.data) == target, else None.
        """
        current = self.head
        while current:
            if key(current.data) == target:
                return current.data
            current = current.next
        return None
