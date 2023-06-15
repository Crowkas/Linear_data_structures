class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self,data):
        self.items.insert(0,data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse(self):
        for i, item in enumerate(reversed(self.items)):
            print(f"{i}.- {item}")
            
food = ListQueue()
food.enqueue('eggs')
food.enqueue('ham')
food.enqueue('spam')
food.traverse()
print(food.dequeue())
food.traverse()

