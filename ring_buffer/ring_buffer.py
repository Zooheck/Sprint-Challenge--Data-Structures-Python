class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
        elif self.current == self.capacity:
            self.storage.append(item)
            self.storage.pop(0)

    def get(self):
        return self.storage
