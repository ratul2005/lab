class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class llist:
    def __init__(self):
        self.head = None

    def add(self, value):
        new = node(value)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new


    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def count(self):
        c = 0
        temp = self.head
        while temp:
            c = c + 1
            temp = temp.next
        return c

    def insert_begin(self, value):
        new = node(value)
        new.next = self.head
        self.head = new

    
    def insert_pos(self, value, pos):
        if pos == 0 or self.head is None:
            self.insert_begin(value)
            return

        new = node(value)
        temp = self.head
        i = 0

        while temp is not None and i < pos - 1:
            temp = temp.next
            i = i + 1

        if temp is None:
            self.add(value)
        else:
            new.next = temp.next
            temp.next = new

    def update(self, pos, new_value):
        temp = self.head
        i = 0

        while temp is not None and i < pos:
            temp = temp.next
            i = i + 1

        if temp is not None:
            temp.value = new_value


    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        prev = self.head
        temp = self.head.next

        while temp is not None and temp.value != value:
            prev = temp
            temp = temp.next

        if temp is not None:
            prev.next = temp.next


ll = llist()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)

print("List:")
ll.traverse()

print("Count:", ll.count())

ll.insert_begin(5)          
ll.insert_pos(25, 3)        
print("After insert:")
ll.traverse()

ll.update(2, 99)            
print("After update:")
ll.traverse()

ll.delete(25)               
print("After delete 25:")
ll.traverse()
