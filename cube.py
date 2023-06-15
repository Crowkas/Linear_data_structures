from array_1 import Array
import random

class Cube():
    
    def __init__(self, rows, columns, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns)
            for col in range(columns):
                self.data[row][col] = Array(depth, fill_value)
            
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def get_depth(self):
        return len(self.data[0][0])
    
    def __getitem__ (self, index):
        return self.data[index]
    
    def __str__(self):
        result = ''
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][col][depth]) + ' '
                result += '\n'
        return str(result)
    
    def random_items(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    self.data[col][row][depth] = random.randint(1, 11)      
        return str(self.data)
        
    def sum_items(self):
        suma = 0
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    suma += self.data[row][col][depth]
        return suma