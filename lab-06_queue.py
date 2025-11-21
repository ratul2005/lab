class queue:
    def __init__(self):
        self.data = []

    def enque(self, value):
        self.data.append(value)

    def deque(self):
        if self.empty():
            print("Queue is empty")
            return
        return self.data.pop(0)

    def traverse(self):
        for x in self.data:
            print(x, end=" ")
        print()

    def empty(self):
        return len(self.data) == 0
q = queue()

q.enque(10)
q.enque(20)
q.enque(30)

print("Queue:")
q.traverse()

print("Deque:", q.deque())

print("After deque:")
q.traverse()
