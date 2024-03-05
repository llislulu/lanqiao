from collections import deque
class MyStack:

    def __init__(self):
            self.dequeIn = deque()
            self.dequeOut = deque()
    def push(self, x: int) -> None:
        self.dequeIn.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.dequeIn) - 1):
            self.dequeOut.append(self.dequeIn.popleft())
        self.dequeIn, self.dequeOut = self.dequeOut, self.dequeIn
        return self.dequeOut.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.dequeIn)-1):
            self.dequeOut.append(self.dequeIn.popleft())
        self.dequeIn, self.dequeOut = self.dequeOut, self.dequeIn
        temp = self.dequeOut.popleft()
        self.dequeIn.append(temp)
        return temp

    def empty(self) -> bool:
        return len(self.dequeIn) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()