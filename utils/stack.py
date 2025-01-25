class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def print_items(self):
        if self.is_empty():
            print("No items in stack.")
        else:
            for i, item in enumerate(reversed(self.items), start=1):
                print(f"{i}. {item}")
