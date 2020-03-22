# Singly Linked List:

class Node:

	def __init__(self, dataval):
		self.dataval = dataval
		self.nextval = None


class SLinkedList:

	def __init__(self):
		self.headval = None

	def append(self, data):
		new_node = Node(data)

		if self.headval is None:
			self.headval = new_node
			return

		node = self.headval
		while node.nextval:
			node = node.nextval
		node.nextval = new_node

	def insert_beg(self, data):
		new_node = Node(data)

		node = self.headval
		new_node.nextval = node
		self.headval = new_node

	def print_list(self):
		if self.headval:
			node = self.headval
			print(node.dataval)
			while node.nextval:
				node = node.nextval
				print(node.dataval)

	def insert(self, data, index):
		new_node = Node(data)
		node = self.headval
		if index == 1:
			self.insert_beg(data)
		else:
			for i in range(1, index - 1):
				node = node.nextval
			new_node.nextval = node.nextval
			node.nextval = new_node

	def delete_beg(self):
		self.headval = self.headval.nextval

	def delete_end(self):
		if self.headval:
			node = self.headval
			if node.nextval is None:
				self.delete_beg()
			else:
				while node.nextval.nextval:
					node = node.nextval
				node.nextval = None

	def delete(self, index):
		node = self.headval
		if index == 1:
			self.delete_beg()
		else:
			for i in range(1, index - 1):
				node = node.nextval
			node.nextval = node.nextval.nextval

	def remove(self, item):
		node = self.headval
		prenode = None
		while node:
			if item is node.dataval:
				if node:
					prenode.nextval = node.nextval
				else:
					self.headval = None
			prenode = node
			node = node.nextval

	def search(self, item):
		node = self.headval
		i = 1
		while node:
			if item is node.dataval:
				return i
			else:
				node = node.nextval
				i += 1

	def insert_after(self, element, item):
		new_node = Node(item)
		node = self.headval
		while node:
			if element is node.dataval:
				new_node.nextval = node.nextval
				node.nextval = new_node
			node = node.nextval


ll = SLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.insert_beg(50)
ll.insert_beg(60)
ll.insert_beg(70)
ll.print_list()
print("-------")
ll.insert(100, 4)
ll.insert(90, 5)
ll.print_list()
print("-------")
ll.delete_beg()
ll.delete_end()
ll.delete_end()
ll.print_list()
print("-------")
ll.delete(1)
ll.remove(90)
ll.print_list()
print("-------")
ll.insert_after(100, 80)
ll.print_list()
print(ll.search(80))


"""
OUTPUT:
70
60
50
10
20
30
-------
70
60
50
100
90
10
20
30
-------
60
50
100
90
10
-------
50
100
10
-------
50
100
80
10
3
"""
