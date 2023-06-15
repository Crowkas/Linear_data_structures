class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def target_item(self):
        self.next = probe
        while probe != None:
            print(probe.data)
            probe = probe.next
            
        self.next = probe
        
        while probe != None and self.data != probe.data:
            probe = probe.next
        if probe != None:
            print(f'Target item {self.data} has been found')
        else:
            print(f'Target item {self.data} is not in the linked list')

