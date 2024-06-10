class PriorityQueue:

    def __init__(self, max_size):
        self.container = []
        self.max_size = max_size

    def enqueue(self, item, priority):
        if not self.isFull():
            self.container.append((priority, item))
            self.container.sort(key=lambda x: x[0], reverse=True)
        else:
            print("Priority Queue is full")

    def dequeue(self):
        if not self.isEmpty():
            return self.container.pop(0)[1]
        else:
            print("Priority Queue is empty")
            return None

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return len(self.container) >= self.max_size

    def peek(self):
        if self.isEmpty():
            raise Exception("Priority Queue is empty")
        return self.container[0][1]

    def show(self):
        return [item for priority, item in self.container]

pq = PriorityQueue(5)
print(pq.isFull())
pq.enqueue('a', 2)
print(pq.show())
pq.enqueue('b', 1)
print(pq.show())
pq.enqueue('c', 3)
print(pq.show())
pq.dequeue()
print(pq.show())
pq.dequeue()
print(pq.show())