class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expression):
    stack = Stack()
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.is_empty() or brackets[char] != stack.pop():
                return False

    return stack.is_empty()
