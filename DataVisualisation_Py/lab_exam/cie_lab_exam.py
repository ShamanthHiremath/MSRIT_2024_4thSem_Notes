# -*- coding: utf-8 -*-
"""cie_lab_exam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NvN5IwqIAfORWMpFPyljwtYMxCH-FJ64
"""

# 1. a.	Write a python program to read 2 numbers from the keyboard and perform the basic arithmetic operations based on the choice. (1-Add, 2-Subtract, 3-Multiply, 4-Divide)

num1= int(input("ENTER FIRST NUM: "))
num2= int(input("ENTER SECOND NUM: "))

key = input("ENTER OPERAND: ")[0]

if(key=='+'):
    print("SUM: ", num1+num2)
elif(key=='-'):
    print("DIFFERENCE: ", num1-num2)
elif(key=='*'):
    print("PRODUCT: ", num1*num2)
elif(key=='/'):
    print("QUOTIENT: ", num1/num2)
else:
    print("WRONG OPERAND")

# 1. b.	Write a python program to create a list of tuples having first element as the strings and the second element as the length of the string. Output the list of tuples sorted based on the length of the string.

strings = ["apple", "banana", "cherry", "date"]
tuples = [(string, len(string)) for string in strings]

tuples.sort(key = lambda x:x[1])
print(tuples)

# 2. a.	Write a python program to display all the prime numbers in the given range

def prime_check(n):
  if n>1:
    for i in range(2, n//2+1):
      if n%i==0:
        return False
    else:
      return True


n1 = int(input("Enter the start of range: "))
n2 = int(input("Enter the end of range: "))

print(f"Prime No's in range {n1} to {n2} are: ")
for num in range(n1,n2+1):
  prime = prime_check(num)
  if prime:
    print(num, end=", ")

# 2. b.	Write a python program to create a list with all the subject names of the 4th semester and perform the following operations.
# •	Display the list using for loop.
# •	Display 2nd and 5th element of the list.
# •	Display first 4 elements of the list using the range of indexes.
# •	Display last 4 elements of the list using the range of negative indexes.
# •	Display if "Python Programming Lab" is available in the List or not.
# •	Demonstrate the working of append () and insert () function.
# •	Demonstrate the working of remove() and pop() function.

subjs = ["DAA", "DCN", "MCIoT", "Maths", "FAFL", "PyLab", "DCNLab", "DAALab"]

# •	Display the list using for loop.
for subs in subjs:
  print(subs)

# Display 2nd and 5th element of the list.
print(subjs[1])
print(subjs[4])

# Display first 4 elements of the list using the range of indexes.
print(subjs[:4])

# Display last 4 elements of the list using the range of negative indexes.
print(subjs[-4:])

# Display if "Python Programming Lab" is available in the List or not.
if "PyLab" in subjs:
  print("Yes")

# Demonstrate the working of append () and insert () function.
subjs.append("IntraInternship")
print(subjs)
subjs.insert(3, "WrongSubject")
print(subjs)

# Demonstrate the working of remove() and pop() function.
subjs.pop()
print(subjs)
subjs.remove("WrongSubject")
print(subjs)

# 3. a.	Create a dictionary for words and their meanings. Write functions to add a new entry (word: meaning), search for a particular word and retrieve meaning, given meaning find words with same meaning, remove an entry, display all words sorted alphabetically. [Program must be menu driven].

word_meaning_dict = {}

def add_entry(word, meaning):
    if word in word_meaning_dict:
        print("Word already exists in the dictionary.")
    else:
        word_meaning_dict[word] = meaning
        print("Entry added successfully.")

def search_word(word):
    if word in word_meaning_dict:
        print("Meaning of", word + ":", word_meaning_dict[word])
    else:
        print("Word not found in the dictionary.")

def find_word_by_meaning(meaning):
    words = [word for word, mean in word_meaning_dict.items() if mean == meaning]
    if words:
        print("Words with the meaning", meaning + ":", ", ".join(words))
    else:
        print("No words found with the specified meaning.")

def remove_entry(word):
    if word in word_meaning_dict:
        del word_meaning_dict[word]
        print("Entry removed successfully.")
    else:
        print("Word not found in the dictionary.")

def display_sorted_words():
    sorted_words = sorted(word_meaning_dict.keys())
    print("Words in the dictionary (sorted alphabetically):")
    for word in sorted_words:
        print(word + ":", word_meaning_dict[word])

def display_menu():
    print("\nMenu:")
    print("1) Add a new word as entry")
    print("2) Search a word")
    print("3) Find words with same meaning")
    print("4) Remove an entry")
    print("5) Display")
#     print("6) Exit")

conti = "y"

while conti=="y":
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        word = input("Enter the word: ")
        meaning = input("Enter the meaning: ")
        add_entry(word, meaning)
    elif choice == '2':
        word = input("Enter the word to search: ")
        search_word(word)
    elif choice == '3':
        meaning = input("Enter the meaning to search: ")
        find_word_by_meaning(meaning)
    elif choice == '4':
        word = input("Enter the word to remove: ")
        remove_entry(word)
    elif choice == '5':
        display_sorted_words()
    else:
        print("Invalid choice. Please enter a valid option.")

    conti = input("Continue?  (y)/(n): ")

    if conti == "n":
        print("Exiting...")

# 3. b.	Write a python program to perform the following operations using user defined functions
# •	Display the maximum and minimum number from the array.
# •	Display the second largest number from the array without sorting

def inputArray():
  n = int(input("Enter the number of elements: "))
  arr = []
  for i in range(n):
    print(f"Enter element {i+1}: ", end=' ')
    ele = int(input())
    arr.append(ele)
  return arr

arr = inputArray()
print(arr)

#	Display the maximum and minimum number from the array.
print(f"Maxi element in arr is : {max(arr)}")
print(f"Mini element in arr is : {min(arr)}")

#	Display the second largest number from the array without sorting
num1 = max(arr)
arr.remove(num1)
num2 = max(arr)
print(f"Second largest element in arr is : {num2}")

# 5. a.	Write a python program to initialize a dictionary of usernames and passwords
# associated with it.passwd={‘rahul’: ‘genius’, ‘kumar’: ‘smart’, ‘ankita’: ‘intelligent’} perform the following functions:
# •	To print all the items in the dictionary.
# •	To print all the keys in the dictionary.
# •	To print all the values in the dictionary.
# •	To get the passwords of users. For example, passwd[‘rahul’]= genius
# •	Change the password of a particular user. For example, passwd[‘ankita’]=‘brilliant’

users = {
    "rahul": "xyz",
    "sanchit": "hawyeah",
    "saurabh": "nikhil",
}

# To print all the items in the dictionary.
print("All items in the dictionary:")
for key, value in users.items():
    print(key, ":", value)

# To print all the keys in the dictionary.
print("\nAll keys in the dictionary:")
for key in users.keys():
    print(key)

# To print all the values in the dictionary.
print("\nAll values in the dictionary:")
for value in users.values():
    print(value)

print(users["sanchit"])

users["sanchit"] = "I'm wet"

print("\n",users["sanchit"])

# 5 a.Develop a python program to count all the occurrences of vowels, consonants and digits from the given text using Regular expressions.

import re

strr = input("Enter the text: ")

vow = re.findall("[aeiou]", strr)
digits = re.findall("[0-9]", strr)
cons = re.findall("[^aeiou]", strr)

print(f"Vowels : {vow}")
print(f"Consonants : {cons}")
print(f"Digits : {digits}")

# 5. b.	Write a python program to create a tuple and perform the following operations
# •	Adding an items
# •	Displaying the length of the tuple
# •	Checking for an item in the tuple
# •	Accessing an items

tup = (1, 2, 3, 4, 5)

#	Adding an items
tup = tup + (6,)
print(tup)

print("Length of tuple: ",len(tup))
print(tup)

if 5 in tup:
  print("5 is in the tuple")
else:
  print("5 is not in the tuple")

print("3rd element is", tup[3])

# 5. c.	Write a python program to create a text file and ask the user to enter 5-6 lines of text. Display the longest and the shortest word from the file. Display the length of these words.

myfile =  open("new.txt", "w")

for i in range(5):
    line = input(f"Enter line: {i+1}: ")
    myfile.write(line + "\n")

myfile.close()

myfile = open("new.txt", "r")

longest_word = ""
shortest_word = None
contents=myfile.read()
words = contents.split()

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

    if shortest_word is None or len(word) < len(shortest_word):
        shortest_word = word

myfile.close()

print("\nLongest word in the file:")
print(f"{longest_word} (Length: {len(longest_word)})")
print("\nShortest word in the file:")
print(f"{shortest_word} (Length: {len(shortest_word)})")

# 6. a.	Write a python function binary Search () to read a sorted array and search for the key element. Display the appropriate messages.

def binsearch(s, e, key, arr):
    if(s>e):
        print("Element not found")
        return
    mid = s + (e-s)//2
    if(arr[mid] == key):
        print(f"{key} found at position {mid}")
        return
    elif(arr[mid] > key):
        binsearch(s, mid-1, key, arr)
    else:
        binsearch(mid+1, e, key, arr)

arr =[1,10,3,4,5,6,6,7,8,9]
arr.sort()
print(arr)
binsearch(0, len(arr), 10, arr)

# 6. b.	Write a python program to simulate saving account processing in a bank using constructors. Create Deposit and Withdraw with other member function and Check for Validation while withdrawing the amount. Raise the appropriate exceptions when depositing and withdrawing an incorrect amount. Display appropriate messages.

class BankAccount:
    """
    Doesnt work
    def __init__(self):
        self.name = input("Enter name: ")
        self.accNo = input("Enter A/C no: ")
        self.bal = input("Enter balance: ")
        self.typeAC = input("Enter type of account: ")
        self.add = input("Enter address: ")
    """
    def __init__(self, name, accNo, bal, typeAC, add):
        self.name = name
        self.accNo = accNo
        self.bal = bal
        self.typeAC = typeAC
        self.add = add

    def deposit(self, amount):

        if amount > 0:
            self.bal += amount
            print(f"Deposited Rs{amount}. New balance is Rs{self.bal}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.bal:
            self.bal -= amount
            print(f"Withdrew Rs{amount}. New balance is Rs{self.bal}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def details(self):
        print("\nAccount Information: \n")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.accNo}")
        print(f"Balance: Rs{self.bal}")
        print(f"Type: {self.typeAC}")
        print(f"Address: {self.add}")


person1 = BankAccount("JBSJBS", 123, 1000, "Savings", "Bangalore")
person1.deposit(2000)
person1.withdraw(1000)
person1.details()

# 7. a.	Develop a python program to create two classes called as Stack and Queue. Provide the necessary data members and methods to display the operations that can be performed on stacks and queues. Test for all type of conditions

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack contents:", self.stack)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty, nothing at front")
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue contents:", self.queue)

# Test cases
if __name__ == "__main__":
    # Testing Stack
    print("Testing Stack Operations:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    print("Popped item:", stack.pop())
    print("Peek item:", stack.peek())
    stack.display()
    print("Popped item:", stack.pop())
    print("Popped item:", stack.pop())
    print("Popped item:", stack.pop())  # Stack is empty
    stack.display()

    # Testing Queue
    print("\nTesting Queue Operations:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    print("Dequeued item:", queue.dequeue())
    print("Front item:", queue.front())
    queue.display()
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())  # Queue is empty
    queue.display()

# 7. b.	Write a python program to utilize NumPy and perform the following operations.
# •	Read and display a 2D Array.
# •	Display the array elements in the reverse order.
# •	Display all the elements of principal diagonal elements.
# •	Sort the 2D array in ascending and descending order

import numpy as np

#	Read and display a 2D Array.
arr2d = []
rows = int(input("Enter no of rows: "))
cols = int(input("Enter no of cols: "))

for i in range(rows):
  arr = []
  print(f"Enter {i+1} row elements: ")
  for j in range(cols):
    num = int(input())
    arr.append(num)
  arr2d.append(arr)

arr2d = np.array(arr2d)
print("\n", arr2d , "\n")

# Display the array elements in the reverse order.
print("2D Array in Reverse Order (without loop):")
print(arr2d[::-1])
print()

print("2D Array in Reverse Order (with loop):")
for row in reversed(arr2d):
    print(row)
print()

#	Display all the elements of principal diagonal elements.
diagonal_elements = np.diag(arr2d)
print("Principal diagonal elements:", diagonal_elements)
print()

# Sort the 2D array in ascending and descending order
arr_sorted_asc = np.sort(arr2d, axis=None)
arr_sorted_desc = np.sort(arr2d, axis=None)[::-1]

print("Sorted array in ascending order:")
print(arr_sorted_asc)
print("Sorted array in descending order:")
print(arr_sorted_desc)

# 8. a.	Develop a python program to read 20 random numbers. Display all the odd numbers from this list which are of length 2 and 4.

import random

arr = [random.randint(0, 100) for i in range(20)]
for num in arr:
  if num%2 == 1:
    num_str = str(num)  # Convert the integer to a string to check the number of digits
    if len(num_str) == 2:
      print("Len 2: ", num)
    elif len(num_str) == 4:
      print("Len 4: ", num)

# 8. b.	Develop a python program to create a text file and ask the user to enter 5-6 lines of text. Count the number of upper case, lower case and digits in the file. Display the details of the file.

myfile =  open("file2.txt", "w")

for i in range(5):
    line = input(f"Enter line: {i+1}: ")
    myfile.write(line + "\n")

myfile.close()

myfile = open("new.txt", "r")

upper_count = 0
lower_count = 0
digit_count = 0

for line in myfile:
    for char in line:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1

myfile.close()

print(f"Uppercase Count: {upper_count}, Lowercase Count: {lower_count}, Digit Count: {digit_count}")

# 9. a.	Develop a python program read a dataset and perform the following using Pandas
# •	Visualize the dataset using plot ().
# •	Draw the Scatter plot for the dataset on any column.
# •	Display the scatter plot with different colors.
# •	Draw the Histogram for the dataset on any column.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.csv')

plt.figure(figsize=(10, 6))
df.plot(kind='line', subplots=True, layout=(5, 5), figsize=(15, 10), title="Dataset Visualization")
plt.tight_layout()
plt.show()

df.plot.scatter(x = 'sepal.length', y = 'sepal.width', title = "Scatter plot variable for X and Y axis")
plt.show()

plt.scatter(df.index, df['sepal.length'], c='black')
plt.xlabel('Index')

df.plot(kind='hist')
plt.show()

# 9. b.	Develop a python program to demonstrate handling multiple exceptions using try, except , else and finally block statements

def handle_multiple_exceptions():
    try:
        # Code that may raise multiple exceptions
        value = int(input("Enter a number: "))  # May raise ValueError
        result = 10 / value  # May raise ZeroDivisionError
        my_list = [1, 2, 3]
        print(my_list[value])  # May raise IndexError
        my_dict = {'a': 1, 'b': 2}
        print(my_dict[value])  # May raise KeyError if value is not 0 or 1

    except ValueError as e:
        print(f"ValueError caught: {e}")

    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")

    except IndexError as e:
        print(f"IndexError caught: {e}")

    except KeyError as e:
        print(f"KeyError caught: {e}")

    else:
        # This block will run if no exceptions were raised
        print("All operations were successful!")

    finally:
        # This block will always run
        print("Execution completed, whether an exception was raised or not.")

# Call the function to demonstrate exception handling
handle_multiple_exceptions()

# 10. b. b.	Write a python program to demonstrate handling of the following exceptions using try and except.
# •	Name Error
# •	Index Error
# •	Key Error
# •	Zero Division Error

def handle_exceptions():
    # Handling NameError
    try:
        print(non_existent_variable)
    except NameError as e:
        print(f"NameError caught: {e}")

    # Handling IndexError
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError caught: {e}")

    # Handling KeyError
    try:
        my_dict = {'a': 1, 'b': 2}
        print(my_dict['c'])
    except KeyError as e:
        print(f"KeyError caught: {e}")

    # Handling ZeroDivisionError
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")

# Call the function to see exception handling in action
handle_exceptions()

# c.	Write a python program to read the Iris dataset and perform the following operations using Pandas
# •	Display first 5 rows of the dataset.
# •	Display last 5 rows of the dataset.
# •	Display the information about the dataset.
# •	Display the overview of the values of each column.
# •	Visualize the dataset using plot ().

df=pd.read_csv('iris.csv')

print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

print("\nInformation about the dataset:")
print(df.info())

print("\nOverview of the values of each column:")
print(df.describe())

plt.figure(figsize=(10, 6))
df.plot(kind='line', subplots=True, layout=(5, 5), figsize=(15, 10), title="Dataset Visualization")
plt.tight_layout()
plt.show()