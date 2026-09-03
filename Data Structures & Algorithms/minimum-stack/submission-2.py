class MinStack:

    def __init__(self):
        self.stack = [] #implementing with a list
        self.minStack = [] #for getMin

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        


    def pop(self) -> None:
        removed = self.stack.pop()
        #only pop the minStack top if its equal to the popped value from stack 
        if removed == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
