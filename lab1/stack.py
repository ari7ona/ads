class Stack:

    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.container.pop()
        else:
            print("Stack is empty")
            return None
        
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.container)
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.container[-1]
    
    def show(self):
        return self.container

s = Stack()
s.push('a')
print(s.show())
s.push('b')
print(s.show())
s.pop()
print(s.show())
print(s.peek())
print(s.size())
print(s.isEmpty())