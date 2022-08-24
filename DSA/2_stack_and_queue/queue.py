class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[0]

    def delete(self):
        self.items = None

    def is_empty(self):
        return self.items == []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)


if __name__ == "__main__":
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)

