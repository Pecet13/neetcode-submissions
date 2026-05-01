class MinStack:

    def __init__(self):
        self.items = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.min_val is None or val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        top = self.items.pop()
        if not self.items:
            self.min_val = None
        elif top == self.min_val:
            self.min_val = min(self.items)

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_val
