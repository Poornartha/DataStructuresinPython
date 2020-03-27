# Stack Data Structure:

"""
Operations:
● Push an element
● Pop an element
● Top of Stack
● Search an element
● Display stack

"""


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
        if self.items:
            i = len(self.items)
            re = self.items[i - 1]
            return re
        return -1

    def search(self, item):
        for i in range(0, len(self.items)):
            if self.items[i] == item:
                return i
        return -1

    def display(self):
        for i in range(len(self.items) - 1, -1, -1):
            print(str(self.items[i]))


s = Stack()

while True:
    print("Enter your Choice: ")
    print("1. Push an element ")
    print("2. Pop an element ")
    print("3. Top of Stack ")
    print("4. Search an element")
    print("5. Display Stack")
    print("6. Exit ")

    choice = int(input("Choice: "))

    if choice == 1:
        num = int(input("Enter the number: "))
        s.push(num)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        print(s.top())
    elif choice == 4:
        num = int(input("Enter the number: "))
        obj = s.search(num)
        if obj != -1:
            print(obj)
        else:
            print("Invalid Number. ")
    elif choice == 5:
        s.display()
    elif choice == 6:
        break
    else:
        print("Invalid Choice.")

"""
Output:
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 1
Enter the number: 10
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 1
Enter the number: 20
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 1
Enter the number: 30
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 5
30
20
10
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 2
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 5
20
10
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 3
20
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 4
Enter the number: 20
1
Enter your Choice:
1. Push an element
2. Pop an element
3. Top of Stack
4. Search an element
5. Display Stack
6. Exit
Choice: 6
"""