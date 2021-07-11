



class Stack():

    def __init__(self):
        self.stack = [];
        

    def push(self, val):
        self.stack.append(val)
        

    def pop(self):
        value = len(self.stack)
        self.stack.pop()
        

    def top(self):
        value = len(self.stack)
        return(self.stack[value - 1])
        

    def getMin(self):
        min = self.stack[0]
        for x in self.stack:
            if min > x:
                min = x
        return(min)

        
currentStack = Stack()
currentStack.push(-100)
currentStack.push(0)
currentStack.push(-3)
currentStack.push(-5)
currentStack.push(-100)
currentStack.push(-3)


for i in currentStack.stack:
    print(i)


print(currentStack.getMin())

currentStack.pop()
currentStack.pop()


print(currentStack.top())

print(" BREAK LINE ")

for i in currentStack.stack:
    print(i)


print(" BREAK LINE ")
print(currentStack.getMin())