class Queue:
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
    def remove(self):
        if self.container:
            return self.container.pop(0)
        else:
            print("Queue is empty")
            return None
    def show(self):
        return self.container

q = Queue()
q.add('a')
print(q.show())
q.add('b')
print(q.show())
q.remove()
print(q.show())