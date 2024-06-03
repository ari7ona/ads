class Queue:

    def __init__(self, max_size):
        self.container = []
        self.max_size = max_size

    def enqueue(self, item):
        if not self.isFull():
            self.container.append(item)
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.isEmpty():
            return self.container.pop(0)
        else:
            print("Queue is empty")
            return None
        
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return self.size() == 0
    
    def isFull(self):
        return len(self.container) >= self.max_size
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.container[-1]
    
    def show(self):
        return self.container

q = Queue(5)
print(q.isFull())
q.enqueue('a')
print(q.show())
q.enqueue('b')
print(q.show())
q.dequeue()
print(q.show())