class MyQueue:

    s1:list[int]
    s2:list[int]
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        pass

    def push(self, x: int) -> None:
        self.s1.append(x)
        pass

    def pop(self) -> int:
        while(len(self.s1) > 1):
            self.s2.append(self.s1.pop())
        
        val = self.s1.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return val
        pass

    def peek(self) -> int:
        while(len(self.s1) > 1):
            self.s2.append(self.s1.pop())
        
        val = self.s1[0]
        while self.s2:
            self.s1.append(self.s2.pop())
        return val
        pass

    def empty(self) -> bool:
        if len(self.s1) >= 1:
            return False
        else:
            return True
        pass

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())