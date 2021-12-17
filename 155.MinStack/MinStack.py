from typing import List, Text

class MinStack:

    def __init__(self):
        self.sta = []
        self.minsta = [float('inf')]

    def push(self, val: int) -> None:
        self.sta.append(val)
        self.minsta.append(min(val,self.minsta[-1]))

    def pop(self) -> None:
        self.minsta.pop()
        self.sta.pop()

    def top(self) -> int:
        return self.sta[-1]

    def getMin(self) -> int:
        return self.minsta[-1]



if __name__ == '__main__':
    arr = [1,0,2,3,4]
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()