class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)
        
            


    def pop(self) -> None:
        val = self.stack.pop()

        if val < 0:
            self.min -= val
            
        

    def top(self) -> int:
        return self.stack[-1] + self.min if self.stack[-1] > 0 else self.min

    def getMin(self) -> int:
        return self.min
