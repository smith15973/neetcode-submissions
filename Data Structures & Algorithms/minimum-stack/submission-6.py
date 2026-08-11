class MinStack:

    def __init__(self):
        self.prefix = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefix) == 0 or val <= self.prefix[-1]:
            self.prefix.append(val)
        
        

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.prefix) > 0 and val == self.prefix[-1]:
            self.prefix.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1] if len(self.prefix)  else 0

        
