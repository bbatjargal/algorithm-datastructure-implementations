class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty():
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.enqueue(3)
print(q.dequeue())
