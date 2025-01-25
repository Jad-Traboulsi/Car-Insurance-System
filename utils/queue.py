class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def print_items(self):
        if self.is_empty():
            print("No items in queue.")
        else:
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")
