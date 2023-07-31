## Table of Contents
- [Variables and Data Types](#variables-and-data-types)
- [Control Flow](#control-flow)
- [Loops](#loops)
- [Functions](#functions)
- [Lists and List Manipulation](#lists-and-list-manipulation)
- [Dictionaries](#dictionaries)
- [Tuples and Tuples Operations](#tuples-and-its-operations)
- [File Handling](#file-handling)
- [Exception Handling](#exception-handling)
- [Modules and Libraries](#modules-and-libraries)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [String Manipulation](#string-manipulation)
- [Lambda Functions](#lambda-functions-and-built-in-functions)
- [Sets and its Operations](#sets-and-set-operations)
- [Comprehensions](#comprehensions)
- [Generators and Iterators](#generators-and-iterators)
- [Decorators](#decorators)
- [JSON Handling](#json-handling)
- [Virtual Environments and Pip](#virtual-environments-and-pip)
- [Regular Expressions](#regular-expressions)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)


### Variables and Data Types 
1. **Variables:** In Python, variables are used to store data values. You can declare a variable and assign a value to it using the equal (`=`) sign. Python is dynamically typed, so you don't need to specify the data type explicitly; it is inferred based on the value assigned to the variable.

```python
# Variable declaration and assignment
name = "John"
age = 30
is_student = True
```

2. **Data Types:**
   - **Numbers:** Python supports various types of numbers, including integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`).

```python
# Numbers
x = 5      # int
y = 3.14   # float
z = 2 + 3j # complex
```

   - **Strings:** Strings are used to represent textual data. You can use single quotes (`'`) or double quotes (`"`) to define a string.

```python
# Strings
message = "Hello, World!"
name = 'Alice'
```

   - **Booleans:** Booleans represent the two truth values, `True` and `False`. They are used in conditional expressions and control flow.

```python
# Booleans
is_raining = True
is_sunny = False
```

   - **Lists:** Lists are ordered collections of elements that can be of different data types. They are mutable, allowing you to add, remove, and modify elements.

```python
# Lists
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
```

   - **Tuples:** Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation.

```python
# Tuples
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
```

   - **Dictionaries:** Dictionaries are collections of key-value pairs. They are unordered, and the elements are accessed by their keys rather than their positions.

```python
# Dictionaries
person = {'name': 'John', 'age': 30, 'occupation': 'Engineer'}
```


### Control Flow
Control flow is essential for decision-making and controlling the flow of your Python code. Let's dive deeper into `if`, `else`, and `elif` statements:

1. **`if` statement:** The `if` statement is used to execute a block of code if a certain condition is true. It is the foundation of decision-making in Python.

```python
# Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")
```

2. **`if`-`else` statement:** You can use the `else` keyword along with `if` to execute a different block of code when the condition is false.

```python
# if-else statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

3. **`if`-`elif`-`else` statement:** The `elif` keyword allows you to check multiple conditions sequentially, and the first true condition's block will be executed. The `else` block is executed if none of the conditions are true.

```python
# if-elif-else statement
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")
```

4. **Nested `if` statements:** You can use nested `if` statements to check multiple conditions within each other.

```python
# Nested if statements
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is not greater than 5")
```

5. **Logical Operators:** You can use logical operators like `and`, `or`, and `not` to combine multiple conditions.

```python
# Logical operators
x = 10
y = 20
if x > 5 and y > 15:
    print("Both x and y meet the conditions")
if x > 5 or y > 15:
    print("Either x or y (or both) meet the conditions")
if not x > 15:
    print("x is not greater than 15")
```

### Loops
Loops are essential for iterating over sequences and performing repetitive tasks. Let's explore both `for` and `while` loops in Python:

1. **`for` loop:** The `for` loop is used to iterate over a sequence (e.g., a list, tuple, string) or any iterable object. It executes a block of code for each element in the sequence.

```python
# Basic for loop with a list
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
# Output: apple, banana, orange

# For loop with a string
message = "Hello"
for char in message:
    print(char)
# Output: H, e, l, l, o
```

2. **`range()` function with `for` loop:** The `range()` function is often used with `for` loops to generate a sequence of numbers. It is commonly used to control the number of iterations.

```python
# Using range() with for loop
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Using range() with a step
for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9
```

3. **`while` loop:** The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true. It is useful when you don't know the number of iterations beforehand.

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0, 1, 2, 3, 4

# Using break and continue
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Output: 0, 1, 2, 3, 4

# Using continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
# Output: 1, 3, 5, 7, 9
```

The `for` loop is ideal for iterating over known sequences, while the `while` loop is more suitable when the number of iterations depends on a condition. 

### Functions
Functions are blocks of reusable code that perform a specific task. Understanding how to define functions, pass arguments, and return values is essential in Python. Additionally, default arguments and variable-length arguments enhance the flexibility of functions. Let's dive into each aspect:

1. **Defining Functions:**
In Python, you define functions using the `def` keyword followed by the function name, parentheses `()`, and a colon `:`. The function body is indented and contains the code to be executed when the function is called.

```python
# Function without arguments and return value
def greet():
    print("Hello, there!")

# Function with arguments and a return value
def add(a, b):
    return a + b
```

2. **Passing Arguments:**
Functions can take one or more arguments. You can pass values to a function by specifying them within the parentheses when calling the function.

```python
# Calling the greet() function
greet()  # Output: Hello, there!

# Calling the add() function with arguments
result = add(5, 3)
print(result)  # Output: 8
```

3. **Returning Values:**
Functions can return values using the `return` statement. You can use the returned value for further computation or to store the result in a variable.

```python
# Function returning a value
def multiply(a, b):
    return a * b

# Calling the multiply() function with arguments and storing the result
result = multiply(4, 6)
print(result)  # Output: 24
```

4. **Default Arguments:**
You can assign default values to function arguments. If a value is not provided for that argument during the function call, the default value will be used.

```python
# Function with default argument
def power(x, n=2):
    return x ** n

# Calling the power() function with one argument (using the default value)
result1 = power(3)
print(result1)  # Output: 9

# Calling the power() function with two arguments
result2 = power(2, 3)
print(result2)  # Output: 8
```

5. **Variable-Length Arguments:**
Python allows you to define functions with variable-length arguments using `*args` and `**kwargs`.

```python
# Function with variable-length arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the sum_all() function with any number of arguments
result1 = sum_all(1, 2, 3)
print(result1)  # Output: 6

result2 = sum_all(1, 2, 3, 4, 5)
print(result2)  # Output: 15
```

### Lists and List Manipulation
Lists are one of the most commonly used data structures in Python. They are versatile and allow you to store a collection of items in a specific order. Let's explore lists and various list manipulation operations:

1. **Creating Lists:**
You can create a list by enclosing items in square brackets `[]`, separated by commas.

```python
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "orange"]

# Creating a mixed list
mixed_list = [1, "hello", 3.14, True]
```

2. **Accessing Elements:**
You can access individual elements of a list using indexing. Python uses 0-based indexing.

```python
# Accessing elements in a list
print(numbers[0])   # Output: 1
print(fruits[1])    # Output: "banana"
print(mixed_list[3]) # Output: True
```

3. **List Slicing:**
List slicing allows you to extract a portion of a list using a start index, an end index (exclusive), and an optional step.

```python
# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:5])    # Output: [2, 3, 4, 5]
print(numbers[::2])    # Output: [1, 3, 5, 7, 9]
print(numbers[::-1])   # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

4. **Appending and Inserting Elements:**
You can add elements to a list using the `append()` method, which adds the element to the end of the list. The `insert()` method allows you to insert an element at a specific index.

```python
# Appending and inserting elements in a list
fruits = ["apple", "banana", "orange"]
fruits.append("grape")       # ['apple', 'banana', 'orange', 'grape']
fruits.insert(1, "kiwi")     # ['apple', 'kiwi', 'banana', 'orange', 'grape']
```

5. **List Comprehensions:**
List comprehensions provide a concise way to create lists based on existing lists or other iterable objects.

```python
# List comprehension to create a new list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)       # Output: [1, 4, 9, 16, 25]

# List comprehension with condition
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)          # Output: [2, 4]
```

6. **Other List Operations:**
Lists offer many other useful methods like `remove()`, `pop()`, `index()`, `count()`, `sort()`, and `reverse()` for various list manipulations.

```python
# Other list operations
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)            # [1, 2, 4, 5]
numbers.pop()                # [1, 2, 4]
numbers.index(2)             # Output: 1
numbers.count(4)             # Output: 1
numbers.sort()               # [1, 2, 4]
numbers.reverse()            # [4, 2, 1]
```


### Dictionaries
Dictionaries are another important data structure in Python. They allow you to store data in the form of key-value pairs, where each value is associated with a unique key. Dictionaries are useful for organizing and retrieving data based on meaningful identifiers (keys). Let's explore dictionaries in Python:

1. **Creating Dictionaries:**
You can create a dictionary by enclosing key-value pairs in curly braces `{}`.

```python
# Creating a dictionary of person information
person = {
    "name": "John",
    "age": 30,
    "occupation": "Engineer"
}

# Creating an empty dictionary
empty_dict = {}
```

2. **Accessing Values:**
You can access the values in a dictionary using their corresponding keys.

```python
# Accessing values in a dictionary
print(person["name"])        # Output: "John"
print(person["age"])         # Output: 30
print(person["occupation"])  # Output: "Engineer"
```

3. **Modifying and Adding Key-Value Pairs:**
You can modify the value associated with a key or add new key-value pairs to the dictionary.

```python
# Modifying a value in the dictionary
person["age"] = 32

# Adding a new key-value pair to the dictionary
person["city"] = "New York"
```

4. **Dictionary Methods:**
Dictionaries provide several useful methods for manipulation and retrieval:

```python
# Dictionary methods
person.keys()       # Returns a list of all keys: ['name', 'age', 'occupation', 'city']
person.values()     # Returns a list of all values: ['John', 32, 'Engineer', 'New York']
person.items()      # Returns a list of key-value tuples: [('name', 'John'), ('age', 32), ('occupation', 'Engineer'), ('city', 'New York')]
person.get("age")   # Returns the value for the given key: 32
person.pop("city")  # Removes the key-value pair and returns the value: 'New York'
len(person)         # Returns the number of key-value pairs in the dictionary: 3
```

5. **Dictionary Comprehension:**
Like lists, dictionaries also support comprehension for creating dictionaries in a concise manner.

```python
# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Tuples and its Operations
Tuples are similar to lists in Python, but they are immutable, meaning their elements cannot be changed or modified after creation. Tuples are typically used to store a collection of related items that should not be modified. Let's explore tuples and various tuple manipulation operations:

1. **Creating Tuples:**
You can create a tuple by enclosing items in parentheses `()` separated by commas.

```python
# Creating a tuple of numbers
numbers = (1, 2, 3, 4, 5)

# Creating a tuple of strings
fruits = ("apple", "banana", "orange")

# Creating a mixed tuple
mixed_tuple = (1, "hello", 3.14, True)
```

2. **Accessing Elements:**
Like lists, you can access individual elements of a tuple using indexing. Python uses 0-based indexing.

```python
# Accessing elements in a tuple
print(numbers[0])   # Output: 1
print(fruits[1])    # Output: "banana"
print(mixed_tuple[3]) # Output: True
```

3. **Tuple Slicing:**
Tuple slicing allows you to extract a portion of a tuple using a start index, an end index (exclusive), and an optional step.

```python
# Tuple slicing
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[1:5])    # Output: (2, 3, 4, 5)
print(numbers[::2])    # Output: (1, 3, 5, 7, 9)
print(numbers[::-1])   # Output: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
```

4. **Tuple Unpacking:**
You can unpack a tuple into multiple variables, which is useful for swapping values or handling functions that return multiple values.

```python
# Tuple unpacking
coordinates = (10, 20)
x, y = coordinates
print(x, y)   # Output: 10 20
```

5. **Tuple Concatenation:**
You can concatenate two tuples using the `+` operator, which creates a new tuple containing elements from both tuples.

```python
# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2
print(result_tuple)   # Output: (1, 2, 3, 4, 5, 6)
```

6. **Tuple Methods:**
Tuples are immutable, so they have fewer methods compared to lists. However, they still provide useful methods like `index()` and `count()`.

```python
# Tuple methods
numbers = (1, 2, 3, 4, 5, 3, 4)
numbers.index(3)      # Output: 2 (index of the first occurrence of 3)
numbers.count(4)      # Output: 2 (number of occurrences of 4)
```

Tuples are often used in situations where you want to ensure that the data remains unchanged.

### File Handling 
File handling in Python allows you to work with files, read data from them, and write data to them. Python provides built-in functions and methods to perform file operations. Let's explore how to read from and write to files:

1. **Opening a File:**
To work with a file, you need to open it using the `open()` function. You provide the file name and the mode in which you want to open the file (read, write, append, etc.).

```python
# Opening a file in read mode
file = open("example.txt", "r")
```

2. **Reading from a File:**
Once the file is opened, you can read its content using various methods like `read()`, `readline()`, or `readlines()`.

```python
# Reading the entire content of the file
content = file.read()
print(content)

# Reading one line from the file
line = file.readline()
print(line)

# Reading all lines and storing them as a list
lines = file.readlines()
print(lines)
```

3. **Closing the File:**
After reading from the file, it's essential to close it using the `close()` method to free up system resources.

```python
# Closing the file
file.close()
```

4. **Writing to a File:**
To write data to a file, you need to open it in write mode (`"w"`) or append mode (`"a"`).

```python
# Opening a file in write mode
file = open("example.txt", "w")

# Writing to the file
file.write("Hello, this is a sample text.\n")
file.write("Writing to a file is easy!\n")

# Closing the file
file.close()
```

5. **Appending to a File:**
If you want to add content to an existing file without overwriting it, you can open the file in append mode.

```python
# Opening a file in append mode
file = open("example.txt", "a")

# Appending to the file
file.write("This line is appended to the file.\n")

# Closing the file
file.close()
```

6. **Context Managers (Using `with` statement):**
Using the `with` statement is a recommended way to work with files as it automatically handles file closure, even if an exception occurs.

```python
# Using with statement for file handling
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# The file will be automatically closed after exiting the 'with' block
```

Always ensure to close the file after reading from or writing to it to avoid resource leaks. Using context managers with the `with` statement is a cleaner and safer approach for file handling in Python.

### Exception Handling 
Exception handling in Python allows you to gracefully handle errors and exceptions that may occur during program execution. The `try`, `except`, `else`, and `finally` blocks are used to implement exception handling. Let's explore each block:

1. **`try` and `except` Blocks:**
The `try` block is used to enclose the code that may raise an exception. If an exception occurs within the `try` block, the corresponding `except` block is executed, and the program continues running without crashing.

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: Division by zero occurred!")
```

2. **Handling Multiple Exceptions:**
You can handle multiple exceptions by listing them in the `except` block or by using a generic `except` block to catch any exception.

```python
try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero occurred!")
except ValueError:
    print("Error: Invalid input, please enter a valid number!")
except:
    print("Error: An unknown exception occurred!")
```

3. **`else` Block:**
The `else` block is executed only if no exceptions occur in the `try` block. It is useful for code that should run when no errors are encountered.

```python
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero occurred!")
except ValueError:
    print("Error: Invalid input, please enter valid numbers!")
else:
    print("The result is:", result)
```

4. **`finally` Block:**
The `finally` block is executed no matter what, whether an exception occurred or not. It is used for cleanup actions like closing files or releasing resources.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    file.close()
```

### Modules and Libraries 
Modules and libraries are essential components in Python that allow you to organize code, reuse functionality, and access a wide range of additional features. Let's explore Python's built-in modules and how to use external libraries with `import`:

1. **Built-in Modules:**
Python comes with a rich set of built-in modules that provide a wide range of functionality. These modules are part of the Python Standard Library and are available for use without installing any external libraries.

```python
# Example: Using built-in modules
import math

# Using functions from the math module
print(math.sqrt(25))      # Output: 5.0
print(math.pi)            # Output: 3.141592653589793
```

2. **Importing Specific Functions:**
You can import specific functions from a module to avoid importing the entire module.

```python
# Importing specific functions from a module
from math import sqrt, pi

# Using the imported functions directly
print(sqrt(25))           # Output: 5.0
print(pi)                 # Output: 3.141592653589793
```

3. **External Libraries with `import`:**
In addition to built-in modules, Python has a vast ecosystem of external libraries that can be installed and used in your code. To use external libraries, you first need to install them using tools like `pip`. Once installed, you can import them and use their functionality.

```python
# Example: Using an external library (requests)
import requests

# Making an HTTP GET request using the requests library
response = requests.get("https://www.example.com")
print(response.status_code)        # Output: 200 (if the request was successful)
print(response.text[:100])         # Output: <!doctype html>\n<html ... (first 100 characters of the response content)
```

4. **Installing External Libraries:**
You can use `pip`, the package installer for Python, to install external libraries. Open the command prompt or terminal and run the following command:

```
pip install library_name
```

Replace `library_name` with the name of the library you want to install. For example, to install the `requests` library, you would run:

```
pip install requests
```

5. **Using Aliases:**
You can use aliases when importing modules or libraries to provide shorter names for easier usage.

```python
# Using aliases when importing modules
import math as m
import requests as req

print(m.sqrt(25))         # Output: 5.0
response = req.get("https://www.example.com")
```

### Object-Oriented Programming (OOP) 
Object-Oriented Programming (OOP) is a programming paradigm that focuses on creating and organizing code using objects. Objects are instances of classes, and classes define the blueprint for creating objects with similar attributes (data) and behaviors (methods). OOP promotes code reusability, modularity, and maintainability. Let's explore the key concepts of OOP:

1. **Classes and Objects:**
A class is a user-defined blueprint or a template that defines the properties (attributes) and behaviors (methods) of objects. An object is an instance of a class, representing a specific entity or concept in the program.

```python
# Defining a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating objects (instances) of the class
dog1 = Dog("Buddy", 2)
dog2 = Dog("Max", 3)

# Accessing object attributes and calling methods
print(dog1.name)   # Output: Buddy
print(dog2.age)    # Output: 3
dog1.bark()        # Output: Woof!
```

2. **Constructor (`__init__` method):**
The `__init__` method is a special method in Python that is called when an object is created. It initializes the object's attributes.

3. **Inheritance:**
Inheritance allows a class (child class) to inherit properties and behaviors from another class (parent class). It promotes code reuse and allows you to create more specialized classes.

```python
# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# Child class (inherits from Animal)
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Child class (inherits from Animal)
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Creating objects of child classes
cat = Cat("Felis catus")
dog = Dog("Canis lupus familiaris")

# Calling the overridden method based on the object's class
cat.make_sound()   # Output: Meow!
dog.make_sound()   # Output: Woof!
```

4. **Encapsulation:**
Encapsulation is the concept of bundling data and methods that operate on that data within a single unit (class). It allows you to control access to the data, providing security and hiding the internal implementation.

```python
# Encapsulation example
class Student:
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def set_name(self, name):
        self.__name = name

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

# Creating a student object and accessing data
student1 = Student("Alice", 101)
print(student1.get_name())         # Output: Alice
print(student1.get_roll_number())   # Output: 101

# Modifying data using setter methods
student1.set_name("Bob")
print(student1.get_name())         # Output: Bob
```

5. **Polymorphism:**
Polymorphism allows objects of different classes to be treated as objects of a common parent class. It enables flexibility and dynamic behavior in your code.

```python
# Polymorphism example
class Shape:
    def draw(self):
        pass

# Child classes (different implementations of draw())
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Using polymorphism with a list of objects
shapes = [Circle(), Square()]

for shape in shapes:
    shape.draw()
# Output: Drawing a circle
#         Drawing a square
```

### String Manipulation 
String manipulation is a common task in programming, and Python provides a rich set of string methods for performing various operations on strings. Let's explore some of the most useful string methods for manipulation and formatting:

1. **String Concatenation:**
You can concatenate two or more strings using the `+` operator.

```python
# String Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"
```

2. **String Length:**
The `len()` function returns the length (number of characters) of a string.

```python
# String Length
text = "Python"
length = len(text)
print(length)  # Output: 6
```

3. **Changing Case:**
Python provides methods to change the case of strings.

```python
# Changing Case
text = "Hello, World!"
print(text.upper())  # Output: "HELLO, WORLD!"
print(text.lower())  # Output: "hello, world!"
print(text.capitalize())  # Output: "Hello, world!"
print(text.title())  # Output: "Hello, World!"
```

4. **Substring:**
You can extract a substring from a string using slicing or the `find()` method.

```python
# Substring
text = "Hello, World!"
print(text[0:5])  # Output: "Hello"
print(text.find("World"))  # Output: 7
```

5. **Replacing:**
You can replace occurrences of a substring with another using the `replace()` method.

```python
# Replacing
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)  # Output: "Hello, Python!"
```

6. **Splitting and Joining:**
The `split()` method splits a string into a list of substrings based on a delimiter, while the `join()` method joins a list of strings into a single string using a delimiter.

```python
# Splitting and Joining
text = "apple,banana,orange"
fruits_list = text.split(",")
print(fruits_list)  # Output: ['apple', 'banana', 'orange']

delimiter = "-"
new_text = delimiter.join(fruits_list)
print(new_text)  # Output: "apple-banana-orange"
```

7. **Stripping Whitespace:**
The `strip()` method removes leading and trailing whitespace characters from a string.

```python
# Stripping Whitespace
text = "    Hello, World!     "
print(text.strip())  # Output: "Hello, World!"
```

8. **String Formatting:**
Python supports string formatting using `%` and the newer f-strings (formatted string literals).

```python
# String Formatting
name = "Alice"
age = 25

# Using % formatting
result = "My name is %s and I am %d years old." % (name, age)
print(result)  # Output: "My name is Alice and I am 25 years old."

# Using f-string (formatted string literals) - Python 3.6 and above
result_f = f"My name is {name} and I am {age} years old."
print(result_f)  # Output: "My name is Alice and I am 25 years old."
```

### Lambda Functions and Built-in Functions 
Lambda Functions:
Lambda functions, also known as anonymous functions, are concise function definitions that can have any number of arguments but only one expression. They are typically used for short, simple operations. The syntax for a lambda function is `lambda arguments: expression`.

```python
# Lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda function to add two numbers
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7
```

Built-in Functions:
Python provides several built-in functions that are readily available and perform common tasks. Some essential built-in functions include:

1. **len()**:
The `len()` function returns the number of items in an object, such as a string, list, tuple, or dictionary.

```python
# Using len() function
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13
```

2. **range()**:
The `range()` function generates a sequence of numbers within a specified range. It is often used in loops.

```python
# Using range() function
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# Creating a list using range()
numbers = list(range(1, 6))
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

3. **zip()**:
The `zip()` function combines multiple iterables (e.g., lists, tuples) into a single iterable of tuples, pairing the corresponding elements.

```python
# Using zip() function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

# Pairing corresponding elements using zip()
for name, age in zip(names, ages):
    print(name, age)
# Output:
# Alice 25
# Bob 30
# Charlie 22
```

4. **sorted()**:
The `sorted()` function returns a new sorted list from an iterable. It does not modify the original iterable.

```python
# Using sorted() function
numbers = [5, 2, 9, 1, 7]

# Sorting the list in ascending order
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 7, 9]

# Sorting the list in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [9, 7, 5, 2, 1]
```

### Sets and Set Operations 
Sets are an unordered collection of unique elements in Python. They are useful for handling collections of data where duplicates are not allowed and for performing set operations such as union, intersection, and difference. Let's explore sets and their operations:

1. **Creating Sets:**
You can create a set by enclosing elements in curly braces `{}` or by using the `set()` constructor.

```python
# Creating a set
set1 = {1, 2, 3, 4, 5}

# Creating a set using the set() constructor
set2 = set([4, 5, 6, 7, 8])
```

2. **Adding and Removing Elements:**
You can add elements to a set using the `add()` method, and you can remove elements using the `remove()` or `discard()` method. The difference between `remove()` and `discard()` is that `remove()` raises an error if the element is not present, while `discard()` does nothing in such cases.

```python
# Adding and removing elements in a set
set1.add(6)          # Adding an element: {1, 2, 3, 4, 5, 6}
set1.remove(2)       # Removing an element: {1, 3, 4, 5, 6}
set1.discard(10)     # No error even if the element is not present
```

3. **Set Operations:**
Sets support various mathematical set operations, such as union, intersection, difference, and symmetric difference.

```python
# Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_set = A | B            # Union: {1, 2, 3, 4, 5, 6, 7, 8}
intersection_set = A & B     # Intersection: {4, 5}
difference_set = A - B       # Difference: {1, 2, 3}
symmetric_difference_set = A ^ B  # Symmetric Difference: {1, 2, 3, 6, 7, 8}
```

4. **Other Set Methods:**
Sets have various other methods like `clear()`, `pop()`, `copy()`, and `issubset()`.

```python
# Other set methods
set1.clear()             # Clears all elements from set1: {}
element = set2.pop()     # Removes and returns an arbitrary element from set2
set3 = set2.copy()       # Creates a copy of set2
subset_check = set3.issubset(A)  # Checks if set3 is a subset of A
```

5. **Frozen Sets:**
A frozen set is an immutable version of a set. Once created, you cannot add or remove elements from a frozen set.

```python
# Creating a frozen set
frozen_set = frozenset([1, 2, 3, 4])
```

### Comprehensions 
Comprehensions are a concise and powerful feature in Python that allows you to create lists, dictionaries, and sets in a single line of code. Comprehensions offer a more readable and efficient way to generate collections based on existing collections or conditions. Let's explore list, dictionary, and set comprehensions:

1. **List Comprehensions:**
List comprehensions allow you to create lists based on existing lists or iterables, applying an expression to each element.

```python
# List comprehension to create a new list of squares
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# List comprehension with a condition (filtering)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]
```

2. **Dictionary Comprehensions:**
Dictionary comprehensions allow you to create dictionaries based on existing dictionaries or iterables, applying an expression to keys and values.

```python
# Dictionary comprehension to create a new dictionary with squares as values
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension with a condition (filtering)
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names if len(name) > 3}
print(name_lengths)  # Output: {'Alice': 5, 'Charlie': 7}
```

3. **Set Comprehensions:**
Set comprehensions allow you to create sets based on existing lists or iterables.

```python
# Set comprehension to create a new set of squares
numbers = [1, 2, 3, 4, 5]
squared_set = {num ** 2 for num in numbers}
print(squared_set)  # Output: {1, 4, 9, 16, 25}

# Set comprehension with a condition (filtering)
even_squares = {num ** 2 for num in numbers if num % 2 == 0}
print(even_squares)  # Output: {4, 16}
```

### Generators and Iterators 
Generators and iterators are concepts in Python that allow for memory-efficient iteration over large data sets or custom data structures. They provide a way to generate and consume data one item at a time, without having to store the entire sequence in memory. Let's explore generators and custom iterators:

1. **Generators:**
Generators are functions that use the `yield` keyword to produce a sequence of values. When called, a generator function returns an iterator object. The values are generated on-the-fly as you iterate over the generator, rather than being stored in memory all at once.

```python
# Generator function to generate squares of numbers
def squares_generator(n):
    for i in range(n):
        yield i ** 2

# Using the generator
squares = squares_generator(5)
for square in squares:
    print(square)
# Output: 0 1 4 9 16
```

2. **Memory Efficiency of Generators:**
Generators are memory-efficient because they generate values on-the-fly and do not store the entire sequence in memory. They are suitable for large datasets and infinite sequences.

3. **Iterators:**
Iterators are objects that implement the `__iter__()` and `__next__()` methods. The `__iter__()` method returns the iterator object itself, and the `__next__()` method returns the next value in the sequence. When there are no more items to return, the `__next__()` method raises the `StopIteration` exception.

```python
# Custom iterator class for squares of numbers
class SquaresIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            square = self.current ** 2
            self.current += 1
            return square
        else:
            raise StopIteration

# Using the custom iterator
squares_iter = SquaresIterator(5)
for square in squares_iter:
    print(square)
# Output: 0 1 4 9 16
```

4. **Built-in Iterators:**
Python has built-in iterators for common data structures like lists, tuples, dictionaries, strings, etc. The `iter()` function can be used to create an iterator from these objects.

```python
# Using built-in iterator for list
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
```

5. **Using Generators vs. Custom Iterators:**
Generators are a more concise way to create iterators, especially for simple sequences. Custom iterators provide more control and flexibility, allowing you to define more complex iteration logic.

### Decorators 
Decorators are a powerful and advanced concept in Python that allows you to modify the behavior of functions or methods without changing their code. Decorators are implemented using functions and are denoted by the `@decorator_name` syntax. They are widely used for adding functionality to functions, such as logging, authentication, memoization, and more. Let's understand decorators step-by-step:

1. **Simple Function:**
Let's start with a simple function.

```python
def say_hello():
    return "Hello, World!"
```

2. **Using a Decorator:**
A decorator is a function that takes another function as an argument and returns a new function. The decorator function is applied to the target function using the `@decorator_name` syntax.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")
```

3. **Calling the Decorated Function:**
When we call the decorated function `say_hello()`, it will execute the wrapper function defined in the decorator `my_decorator()`, which modifies the behavior of the original `say_hello()` function.

```python
say_hello()
# Output:
# Something is happening before the function is called.
# Hello, World!
# Something is happening after the function is called.
```

4. **Decorators with Arguments:**
You can also create decorators that take arguments.

```python
def repeat(num_times):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(num_times=3)
def say_hello(name):
    print(f"Hello, {name}!")
```

5. **Chaining Decorators:**
You can chain multiple decorators by stacking them on top of each other using multiple `@decorator_name` lines.

```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
@repeat(num_times=2)
def say_hello(name):
    return f"Hello, {name}!"
```

6. **Preserving Function Metadata:**
To preserve the metadata (such as docstrings, name, etc.) of the original function when using decorators, use the `functools.wraps` decorator from the `functools` module.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        # ...
    return wrapper
```

### JSON Handling 
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for both humans and machines to read and write. JSON is widely used for data exchange between web servers and clients, and it has become the standard format for APIs and configuration files. In Python, you can work with JSON data using the built-in `json` module. Let's explore how to handle JSON data in Python:

1. **Encoding (Serialization):**
Encoding means converting Python data structures (such as dictionaries and lists) into a JSON string.

```python
import json

# Creating a Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "languages": ["Python", "JavaScript", "Java"]
}

# Encoding the dictionary into a JSON string
json_string = json.dumps(data)
print(json_string)
# Output: {"name": "John Doe", "age": 30, "is_student": false, "languages": ["Python", "JavaScript", "Java"]}
```

2. **Decoding (Deserialization):**
Decoding means converting a JSON string into Python data structures.

```python
# JSON string to be decoded
json_string = '{"name": "John Doe", "age": 30, "is_student": false, "languages": ["Python", "JavaScript", "Java"]}'

# Decoding the JSON string into a Python dictionary
data = json.loads(json_string)
print(data)
# Output: {'name': 'John Doe', 'age': 30, 'is_student': False, 'languages': ['Python', 'JavaScript', 'Java']}
```

3. **Reading JSON from File:**
You can read JSON data from a file using the `json.load()` function.

```python
# Reading JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

4. **Writing JSON to File:**
You can write JSON data to a file using the `json.dump()` function.

```python
# Writing JSON data to a file
data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "languages": ["Python", "C++"]
}

with open('output.json', 'w') as file:
    json.dump(data, file)
```

5. **Working with Nested Data:**
JSON can represent nested data structures, such as dictionaries containing dictionaries or lists.

```python
nested_data = {
    "person": {
        "name": "Alice",
        "age": 25
    },
    "skills": ["Python", "JavaScript", "C++"]
}

json_string = json.dumps(nested_data)
print(json_string)
# Output: {"person": {"name": "Alice", "age": 25}, "skills": ["Python", "JavaScript", "C++"]}
```

### Virtual Environments and Pip 
Virtual environments and `pip` are essential tools in Python for managing dependencies and isolating projects. They allow you to create isolated environments for each project, preventing conflicts between packages and ensuring consistent behavior across different projects. Let's explore how to create virtual environments and use `pip` to manage Python packages:

1. **Virtual Environments:**
Virtual environments are isolated Python environments that contain their own Python interpreter and installed packages. They are created using the `venv` module (built into Python 3.3+), or you can use `virtualenv` (a third-party tool) for earlier versions of Python.

**Creating a Virtual Environment:**

Using `venv` (Python 3.3+):

```bash
# Create a new virtual environment (replace "myenv" with your preferred name)
python3 -m venv myenv
```

Using `virtualenv` (if not using Python 3.3+):

```bash
# Install virtualenv (if not already installed)
pip install virtualenv

# Create a new virtual environment (replace "myenv" with your preferred name)
virtualenv myenv
```

**Activating the Virtual Environment:**

On Windows:

```bash
myenv\Scripts\activate
```

On macOS and Linux:

```bash
source myenv/bin/activate
```

After activating the virtual environment, any packages you install will be isolated to this environment.

2. **Using `pip` to Manage Packages:**
`pip` is a package manager for Python that allows you to install, upgrade, and remove Python packages easily.

**Installing a Package:**

```bash
# Install a package into the virtual environment
pip install package_name
```

**Listing Installed Packages:**

```bash
# List all packages installed in the virtual environment
pip list
```

**Upgrading a Package:**

```bash
# Upgrade a package to the latest version
pip install --upgrade package_name
```

**Uninstalling a Package:**

```bash
# Uninstall a package from the virtual environment
pip uninstall package_name
```

**Freezing Installed Packages:**

To save a list of all installed packages and their versions to a requirements file, use:

```bash
pip freeze > requirements.txt
```

**Installing Packages from a Requirements File:**

To install packages listed in a requirements file, use:

```bash
pip install -r requirements.txt
```


### Regular Expressions 
Regular expressions (often abbreviated as regex or regexp) are powerful tools for pattern matching and text manipulation. They provide a concise and flexible way to search, extract, and replace text based on specific patterns. Regular expressions are widely used in various programming languages, including Python, for tasks such as data validation, text processing, and web scraping. Let's explore the basics of regular expressions in Python:

1. **Importing the `re` Module:**
In Python, regular expressions are supported by the built-in `re` module. You need to import this module to work with regular expressions.

```python
import re
```

2. **Basic Pattern Matching:**
The `re.search()` function is used to find the first occurrence of a pattern in a string. If a match is found, it returns a match object; otherwise, it returns `None`.

```python
# Search for a pattern in a string
text = "Hello, Python!"
pattern = r"Python"
match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found.")
```

3. **Regular Expression Patterns:**
Regular expression patterns are sequences of characters that define a search pattern. Special characters in regular expressions have special meanings. For example:
   - `.` : Matches any single character except a newline.
   - `*` : Matches zero or more occurrences of the preceding character.
   - `+` : Matches one or more occurrences of the preceding character.
   - `?` : Matches zero or one occurrence of the preceding character.
   - `[]` : Matches any character within the square brackets.
   - `()` : Groups patterns together.
   - `|` : Acts like a logical OR.

```python
# Example of using regular expression patterns
text = "apple, banana, orange"
pattern = r"apple|banana|orange"
match = re.search(pattern, text)

if match:
    print("Found:", match.group())
else:
    print("Not Found.")
```

4. **Extracting Substrings with Groups:**
You can use parentheses `()` to create groups in regular expressions and extract specific parts of the matched text.

```python
# Extracting substrings using groups
text = "John Doe (30 years old)"
pattern = r"(.+) \((\d+) years old\)"
match = re.search(pattern, text)

if match:
    print("Name:", match.group(1))
    print("Age:", match.group(2))
```

5. **Replacing Text:**
You can use `re.sub()` to replace text that matches a pattern with a specified string.

```python
# Replacing text using regular expressions
text = "Hello, World!"
pattern = r"Hello"
replacement = "Hi"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: "Hi, World!"
```

### Debugging and Troubleshooting 
Debugging and troubleshooting are critical skills for every developer. Identifying and resolving issues in your code efficiently can save time and frustration. Here are some tips and common debugging techniques to help you become a more effective troubleshooter:

1. **Use Print Statements:**
One of the simplest and most effective ways to debug code is by using print statements. Inserting print statements at strategic points in your code can help you understand the flow of execution and the values of variables at different stages.

```python
def add(a, b):
    print("Adding", a, "and", b)
    return a + b

result = add(5, 3)
print("Result:", result)
```

2. **Inspect Variable Values:**
Print the values of variables to check if they hold the expected values. This can help you identify if there are any unexpected changes in the values.

3. **Use the Python Debugger (pdb):**
Python provides a built-in debugger called `pdb`, which allows you to set breakpoints, step through code, inspect variables, and more. You can run your script with the `-m pdb` option to enable the debugger.

```bash
python -m pdb your_script.py
```

4. **Use Exception Handling:**
Wrap parts of your code with try-except blocks to catch and handle exceptions gracefully. This can help you identify specific points in your code where errors are occurring.

```python
try:
    # Code that may raise an exception
except SomeException as e:
    # Handle the exception
    print("An error occurred:", e)
```

5. **Logging:**
Instead of using print statements, you can use Python's logging module to log messages at different levels (debug, info, warning, error, etc.). Logging provides more control over the output and allows you to log messages to files, the console, or other destinations.

6. **Divide and Conquer:**
If you encounter a large issue, divide the problem into smaller parts and tackle them one by one. Focus on debugging and testing smaller portions of your code.

7. **Check Input and Output:**
Verify the input data and output results to ensure they meet your expectations. Incorrect input data can lead to unexpected behavior.

8. **Version Control:**
Use version control systems like Git to keep track of changes to your code. If you encounter an issue, you can easily revert to a previous version.

9. **Documentation and Online Resources:**
Refer to documentation, forums, and online resources when you encounter difficult issues. Often, someone else may have faced a similar problem and found a solution.

10. **Code Reviews:**
Ask for code reviews from colleagues or peers. Fresh eyes might spot issues that you missed.

11. **Use IDE and Debugging Tools:**
IDEs like Visual Studio Code, PyCharm, or Eclipse have built-in debugging tools that can help you debug code efficiently.
