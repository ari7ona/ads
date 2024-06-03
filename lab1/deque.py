class Deque:

    def __init__(self):
        self.container = []

    def add_front(self, item):
        self.container.insert(0, item)

    def add_rear(self, item):
        self.container.append(item)

    def remove_front(self):
        if self.container:
            return self.container.pop(0)
        else:
            print("Deque is empty")
            return None
        
    def remove_rear(self):
        if self.container:
            return self.container.pop()
        else:
            print("Deque is empty")
            return None
        
    def show(self):
        return self.container

d = Deque()
d.add_front('a')
print(d.show())
d.add_rear('b')
print(d.show())
d.add_front('c')
print(d.show())
d.remove_rear()
print(d.show())
d.remove_front()
print(d.show())