class MyQueue:

    def __init__(self):
        self.stIn = []
        self.stOut = []

    def push(self, x: int) -> None:
        self.stIn.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stOut:
            return self.stOut.pop()
        else:
            for i in range(len(self.stIn)):
                self.stOut.append(self.stIn.pop())
            return self.stOut.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stOut.append(ans)
        return ans

    def empty(self) -> bool:
        return not self.stIn and not self.stOut


obj = MyQueue()
obj.push()
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
