class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

d = Deque()
d.addFront(1)
d.addFront(2)
d.addRear(3)
d.addRear(4)
print(d.removeFront())
print(d.removeRear())

