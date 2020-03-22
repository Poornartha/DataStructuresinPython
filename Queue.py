
class Queue:

	def __init__(self):
		self.items = []

	def insert(self, data):
		self.items.append(data)

	def delete(self):
		re = self.items[0]
		self.items.pop(0)
		return re

	def display(self):
		print(self.items)

	def search(self, query):
		for i in range(0, len(self.items)):
			if self.items[i] is query:
				return i
		return -1


q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.display()
print("------")
q.delete()
q.display()
print(q.search(30))

"""
Output:
[10, 20, 30]
------
[20, 30]
1

"""