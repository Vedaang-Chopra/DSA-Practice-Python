class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        print(self.stack)
        self.stack.append(val)
        
    def pop(self) -> None:
        print(self.stack)
        return  self.stack.pop()
        
        
    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)
        # for j in range(len(self.stack), -1, -1):
        return min(self.stack)


        
