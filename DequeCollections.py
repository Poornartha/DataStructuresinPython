
# Dequeue using Collections:

"""
Add element at Front
Remove element from Front
Add element at Rear
Remove element from Rear
Search for an element

"""

import collections

de = collections.deque([])

while True:
	print("Enter your Choice: ")
	print("1. Add element at Front")
	print("2. Remove element from front")
	print("3. Add element at rear")
	print("4. Remove element from rear")
	print("5. Search for element")
	print("6. Display Dequeue")
	print("7. Exit")

	choice = int(input("Choice: "))

	if choice == 1:
		num = int(input("Enter the number: "))
		de.appendleft(num)
	elif choice == 2:
		de.popleft()
	elif choice == 3:
		num = int(input("Enter the number: "))
		de.append(num)
	elif choice == 4:
		de.pop()
	elif choice == 5:
		num = int(input("Enter the number to search: "))
		print(de.index(num))
	elif choice == 6:
		print(de)
	elif choice == 7:
		break
	else:
		print("Invalid Choice")


"""
OUTPUT:
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 1
Enter the number: 10
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 1
Enter the number: 20
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 1
Enter the number: 30
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 6
deque([30, 20, 10])
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 3
Enter the number: 40
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 6
deque([30, 20, 10, 40])
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 2
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 4
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 6
deque([20, 10])
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 5
Enter the number to search: 20
0
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 5
Enter the number to search: 10
1
Enter your Choice:
1. Add element at Front
2. Remove element from front
3. Add element at rear
4. Remove element from rear
5. Search for element
6. Display Dequeue
7. Exit
Choice: 7
"""
