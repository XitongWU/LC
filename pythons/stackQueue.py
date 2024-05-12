class MyStack:

    q1:list[int]
    q2:list[int]
    
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)
        return None

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append((self.q1.pop(0)))
        
        val = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append((self.q1.pop(0)))
        
        val = self.q1[0]
        self.q2.append((self.q1.pop(0)))
        self.q1, self.q2 = self.q2, self.q1
        return val      

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        else:
            return False


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())
print(myStack.pop())
print(myStack.empty())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()