from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0
    
    def append(self, data):
        node = Node(data)
        
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next
                
            current.next = node
            
        self.size += 1
        
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail
        
        while current:
            value = current.data
            current = current.next
            yield value
            
    def delete(self, data):
        current = self.tail
        previous = self.tail
        
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -=1
                    return current.data
                
            previous = current
            current = current.next
            
    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')
                
    def clear(self):
        self.tail = None
        self.head = 0
        self.size = 0
        
        
# Reto
array = [2, 4, 6]
datos = SinglyLinkedList()

for i in array:
    datos.append(i)
current = datos.tail

while current:
    print(current.data)
    current = current.next