class Node:

	def __init__(self, dataval):
		self.dataval = dataval
		self.nextval = None
		self.prevval = None


class DLinkedList:

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
		new_node.prevval = node

	def insert_beg(self, data):
		new_node = Node(data)

		if self.headval:
			node = self.headval
			new_node.nextval = node
			node.prevval = new_node
			self.headval = new_node
		else:
			self.headval = new_node

	def print_list(self):
		i = 0
		if self.headval:
			node = self.headval
			print(node.dataval)
			while node.nextval:
				node = node.nextval
				print(node.dataval)

	def count(self):
		i = 0
		node = self.headval
		while node:
			node = node.nextval
			i += 1

	def insert(self, data, index):
		new_node = Node(data)
		node = self.headval
		if index == 1:
			self.insert_beg(data)
		elif index == self.count():
			self.insert_end(data)
		else:
			for i in range(1, index - 1):
				node = node.nextval
			new_node.nextval = node.nextval
			node.nextval.prevval = new_node
			node.nextval = new_node
			new_node.prevval = node

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
			if node.nextval.nextval is not None:
				node.nextval = node.nextval.nextval
				node.nextval.nextval.prevval = node.nextval

	def remove(self, item):
		node = self.headval
		prenode = None
		while node:
			if item is node.dataval:
				if node:
					prenode.nextval = node.nextval
					if node.nextval:
						node.nextval.prevval = prenode
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

	def replace(self, index, item):
		node = self.headval
		for i in range(1, index):
			node = node.nextval
		node.dataval = item

	def insert_after(self, element, item):
		new_node = Node(item)
		node = self.headval
		while node:
			if element == node.dataval:
				new_node.nextval = node.nextval
				node.nextval.prevval = new_node
				node.nextval = new_node
				new_node.prevval = node
				break
			node = node.nextval

	def rev_display(self):
		node = self.headval
		while node.nextval:
			node = node.nextval
		while node is not self.headval:
			print(node.dataval)
			node = node.prevval
		print(node.dataval)

ll = DLinkedList()

"""
1. Display list
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
"""

while True:
	print("Enter your choice: ")
	print("1. Display List")
	print("2. Insert at beginning ")
	print("3. Insert at End")
	print("4. Insert at specified postion")
	print("5. Delete from beginning")
	print("6. Delete from end")
	print("7. Delete at specified postion")
	print("8. Delete a particular element")
	print("9. Search an element")
	print("10. Replace element at specified index")
	print("11. Forward traversal")
	print("12. Reverse traversal")
	print("13. Insert after an element")
	print("14. Exit")

	choice = int(input("Choice: "))

	if choice == 1:
		ll.print_list()
	elif choice == 2:
		num = int(input("Enter the number to insert: "))
		ll.insert_beg(num)
	elif choice == 3:
		num = int(input("Enter the number to insert: "))
		ll.append(num)
	elif choice == 4:
		num = int(input("Enter the number to insert: "))
		index = int(input("Enter the index to insert the number at starting from 1: "))
		ll.insert(num, index)
	elif choice == 5:
		ll.delete_beg()
	elif choice == 6:
		ll.delete_end()
	elif choice == 7:
		index = int(input("Enter the index of the number to delete: "))
		ll.delete(index)
	elif choice == 8:
		ele = int(input("Enter the element: "))
		ll.remove(ele)
	elif choice == 9:
		num = int(input("Enter the element to search: "))
		i = ll.search(num)
		if i != -1:
			print(i)
		else:
			print("Number Absent. ")
	elif choice == 10:
		num = int(input("Enter the element: "))
		index = int(input("Enter the index, starting with 1: "))
		ll.replace(index, num)
	elif choice == 11:
		ll.print_list()
	elif choice == 12:
		ll.rev_display()
	elif choice == 13:
		num = int(input("Enter the number to insert: "))
		ele = int(input("Enter the element to insert after:"))
		ll.insert_after(ele, num)
	elif choice == 14:
		break
	else:
		print("Invalid Option")

"""
Output:
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 2
Enter the number to insert: 30
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 3
Enter the number to insert: 40
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 3
Enter the number to insert: 50
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 2
Enter the number to insert: 10
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 4
Enter the number to insert: 15
Enter the index to insert the number at starting from 1: 2
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 1
10
15
30
40
50
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 7
Enter the index of the number to delete: 2
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 1
10
30
40
50
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 8
Enter the element: 30
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 1
10
40
50
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 9
Enter the element to search: 40
2
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 10
Enter the element: 60
Enter the index, starting with 1: 2
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 1
10
60
50
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 11
10
60
50
Enter your choice:
1. Display List
2. Insert at beginning
3. Insert at End
4. Insert at specified postion
5. Delete from beginning
6. Delete from end
7. Delete at specified postion
8. Delete a particular element
9. Search an element
10. Replace element at specified index
11. Forward traversal
12. Reverse traversal
13. Insert after an element
14. Exit
Choice: 12
50
60
10
"""