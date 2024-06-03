class Stack:
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
    def remove(self):
        if self.container:
            return self.container.pop()
        else:
            print("Stack is empty")
            return None
    def show(self):
        return self.container

s = Stack()
s.add('a')
print(s.show())
s.add('b')
print(s.show())
s.remove()
print(s.show())