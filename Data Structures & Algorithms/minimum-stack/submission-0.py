class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            if (self.minstack[-1]>=val):
                self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            v = self.stack.pop()
        
        if self.minstack:
            if self.minstack[-1]==v:
                self.minstack.pop()
                

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1
    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        else:
            return -1
        
