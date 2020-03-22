
class Dequeue:

	def __init__(self):

		self.items = []

	def add_front(self, data):
		l = len(self.items)
		self.items.append(-1)
		for i in range(l - 1, -1, -1):
			self.items[i + 1] = self.items[i]
		self.items[0] = data

	def add_back(self, data):
		self.items.append(data)

	def rem_front(self):
		self.items.pop(0)

	def rem_back(self):
		self.items.pop(len(self.items) - 1)

	def search(self, query):
		for i in range(0, len(self.items)):
			if self.items[i] is query:
				return i
		return -1

	def display(self):
		print(self.items)

dq = Dequeue()
dq.add_back(10)
dq.add_back(20)
dq.add_back(30)
dq.add_back(40)
dq.add_front(50)
dq.display()
print("---------")
dq.rem_back()
dq.display()
print("---------")
dq.rem_front()
dq.display()
print("---------")
print(dq.search(30))

