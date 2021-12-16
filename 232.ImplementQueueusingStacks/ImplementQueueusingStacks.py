from typing import List, Text

class MyQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if not self.queue1:
            while(self.queue2):
                self.queue1.append(self.queue2.pop())
        self.queue1.append(x)

    def pop(self) -> int:
        # 如果 stack2 为空 --> 倒叙
        if not self.queue2:
            while(self.queue1):
                self.queue2.append(self.queue1.pop())
        return self.queue2.pop()

    def peek(self) -> int:
        if not self.queue2:
            while(self.queue1):
                self.queue2.append(self.queue1.pop())
        return self.queue2[-1]

    def empty(self) -> bool:
        if (self.queue1 == [] and self.queue2 == []):
            return True
        else:
            return False

if __name__ == '__main__':
    arr = [1,0,2,3,4]
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.peek()
    queue.pop()
    queue.empty()