
"""
Operations:

● Insert an element
● Remove an element
● Search an element
● Display queue

"""


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

while True:
	print("Enter the choice: ")
	print("1. Insert an element: ")
	print("2. Remove an element: ")
	print("3. Search an element: ")
	print("4. Display Queue: ")
	print("5. Exit ")

	choice = int(input("Choice: "))

	if choice == 1:
		num = int(input("Enter the element: "))
		q.insert(num)
	elif choice == 2:
		q.delete()
	elif choice == 3:
		num = int(input("Enter the element: "))
		s = q.search(num)
		if s == -1:
			print("Element absent ")
		else:
			print(s)
	elif choice == 4:
		q.display()
	elif choice == 5:
		break
	else:
		print("Invalid Choice")
		continue

"""
Output:
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 1
Enter the element: 10
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 1
Enter the element: 20
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 1
Enter the element: 30
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 1
Enter the element: 40
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 4
[10, 20, 30, 40]
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 2
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 4
[20, 30, 40]
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 3
Enter the element: 40
2
Enter the choice:
1. Insert an element:
2. Remove an element:
3. Search an element:
4. Display Queue:
5. Exit
Choice: 5
"""