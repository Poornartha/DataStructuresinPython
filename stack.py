# Stack Data Structure:


class Stack:


    def __init__(self):
    	self.items = []

    
    def push(self, item):    
    	self.items.append(item)

    
    def pop(self):    
    	re = self.top()    
    self.items.remove(re)    
    return re

    
    def top(self):    
    	i = len(self.items)    
    re = self.items[i-1]    
    return re

    
    def search(self, item):    
    	for i in range(0, len(self.items)):    
    	if self.items[i] == item:    
    	return i    
    return -1
    
    def display(self):    
    	print(self.items)


s = Stack()
# Push Elements: 
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()

# Pop Elements: 
s.pop()

# Top of Stack:
s.top()

# Search for an element:
print(s.search(2))

# Display:
s.display()

"""
Output:
[1, 2, 3, 4]
1
[1, 2, 3]

"""