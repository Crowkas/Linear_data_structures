from array_1 import Array
import random

class Grid():
    
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__ (self, index):
        return self.data[index]
    
    def __str__(self):
        result = ''
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + ' '
            result += '\n'
            
        return str(result)
    
    def random_items(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[col][row] = random.randint(1, 11)      
        return str(self.data)
        
    def sum_items(self):
        suma = 0
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                suma += self.data[row][col]
        return suma