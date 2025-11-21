class stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.empty():
            print("Stack is empty")
            return
        return self.data.pop()

    def print(self):
        for x in reversed(self.data):
            print(x, end=" ")
        print()

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


s = stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:")
s.print()

print("Pop:", s.pop())

print("After pop:")
s.print()

print("Empty ?", s.empty())
print("Size:", s.size())
