class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        else:
            return self.items[-1]


