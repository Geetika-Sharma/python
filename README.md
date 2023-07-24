#Python

## Data-Types
In Python, data types are classifications that define the type of data that can be stored in a variable. Python is a dynamically-typed language, meaning you don't need to explicitly specify the data type when declaring a variable; the interpreter infers it based on the assigned value. Python supports several built-in data types, including:

1. **Numeric Types**:
   - `int`: Integer data type, representing whole numbers (e.g., 5, -10).
   - `float`: Floating-point data type, representing numbers with decimal points (e.g., 3.14, -0.5).

2. **Boolean Type**:
   - `bool`: Boolean data type, representing either `True` or `False`.

3. **Sequence Types**:
   - `str`: String data type, representing a sequence of characters (e.g., "Hello, Python!").
   - `list`: List data type, representing an ordered collection of elements (e.g., [1, 2, 3]).
   - `tuple`: Tuple data type, similar to lists but immutable (e.g., (10, 20, 30)).

4. **Mapping Type**:
   - `dict`: Dictionary data type, representing a collection of key-value pairs (e.g., {"name": "John", "age": 30}).

5. **Set Types**:
   - `set`: Set data type, representing an unordered collection of unique elements (e.g., {1, 2, 3}).

6. **None Type**:
   - `None`: Represents the absence of a value or a null value.

Python also supports type conversion or casting between different data types. For example, you can convert an `int` to a `float`, a `float` to an `int`, or a `str` to an `int`, and vice versa, using appropriate functions such as `int()`, `float()`, or `str()`.

Here are some examples of Python data types and their usage:

```python
# Numeric types
age = 25            # int
pi = 3.14159        # float

# Boolean type
is_student = True   # bool

# String type
name = "John"       # str

# List type
numbers = [1, 2, 3] # list

# Tuple type
coordinates = (10, 20) # tuple

# Dictionary type
person = {"name": "Alice", "age": 35} # dict

# Set type
unique_numbers = {1, 2, 3} # set

# None type
result = None       # None
```

Remember that Python being dynamically typed allows variables to change their data type during runtime, depending on the assigned value.

## Functions
In Python, functions are blocks of code that perform a specific task and can be reused throughout a program. Functions help in organizing code, improving code readability, and promoting code reusability. To define a function in Python, you use the `def` keyword followed by the function name, a pair of parentheses `()`, and a colon `:` to start the function block. The function block is indented, and it contains the code that defines what the function does.

Here's the general syntax of defining a function in Python:

```python
def function_name(parameters):
    # Function block with code
    # ...
    return result  # Optional: Return statement to return a value
```

Let's look at a simple example of a function that calculates the sum of two numbers:

```python
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Function call
sum_result = add_numbers(10, 5)
print("Sum:", sum_result)  # Output: Sum: 15
```

In the example above, we defined a function `add_numbers` that takes two parameters `num1` and `num2`. The function block calculates the sum of the two numbers and returns the result using the `return` statement.

Key points to remember about functions in Python:

1. **Parameters**: Functions can accept parameters (inputs) that can be used within the function block. Parameters are specified within the parentheses when defining the function.

2. **Return Statement**: Functions can return a value using the `return` statement. If the `return` statement is omitted, the function will return `None`.

3. **Function Call**: To execute a function and use its code, you need to call the function by using its name and providing any required arguments within the parentheses.

4. **Function Reusability**: Functions can be called multiple times from different parts of the code, allowing code reusability and modularization.

5. **Scope**: Variables defined inside a function have a local scope, meaning they can only be accessed within that function. Variables defined outside the function have a global scope, accessible from any part of the code.

6. **Default Arguments**: Functions can have default values for parameters. If a parameter is not provided when calling the function, the default value will be used.

7. **Arbitrary Arguments**: Functions can also accept an arbitrary number of arguments using `*args` or keyword arguments using `**kwargs`.

Functions are fundamental building blocks in Python, and they play a crucial role in writing efficient, maintainable, and organized code.

### Scope of parameters

There are two main types of parameter scopes in Python:

1. **Local Scope**:
   - Parameters defined in the function's parameter list have a local scope.
   - They are accessible only within the function's body.
   - Any changes made to these variables within the function do not affect variables with the same name outside the function.

Example:

```python
def add_numbers(a, b):  # a and b have local scope
    result = a + b      # result also has local scope
    return result

sum_result = add_numbers(5, 10)
print(sum_result)      # Output: 15
# print(a)  # This will raise a NameError since 'a' is not defined outside the function.
```

2. **Global Scope**:
   - Variables defined outside of any function have a global scope.
   - They are accessible throughout the entire program, including inside functions.
   - However, if you want to modify a global variable inside a function, you need to use the `global` keyword explicitly to indicate that you are referring to the global variable and not creating a new local variable.

Example:

```python
global_variable = 100

def modify_global():
    global global_variable  # Explicitly declare global_variable as global
    global_variable += 1

modify_global()
print(global_variable)    # Output: 101
```

If the `global` keyword is not used, the function will create a new local variable with the same name, and the global variable remains unchanged.

### User Input
#### input( ) function
1. **Return Type**: The `input()` function always returns a string, even if the user enters a number. If you need to convert the input to a specific data type (e.g., int, float), you can use type casting functions like `int()` or `float()`.

2. **User Input**: The user can enter any text, including numbers, letters, symbols, or even an empty string. The program will treat it as a string unless explicitly converted to another data type.

3. **Prompt Message**: The optional prompt message provided to the `input()` function is displayed to the user before waiting for input. It helps provide context or instructions for what the user is expected to enter.

4. **Whitespace**: The `input()` function includes any leading and trailing whitespace (e.g., spaces or tabs) entered by the user. You may want to use the `strip()` method to remove unnecessary whitespace from the input.

Example:

```python
age_str = input("Please enter your age: ")
age = int(age_str)  # Convert the input string to an integer
print("You are", age, "years old.")
```

## Conditionals in Python 
They allow you to execute different blocks of code based on certain conditions. Python uses the `if`, `elif` (short for "else if"), and `else` statements to implement conditionals. The syntax for conditionals is as follows:

```python
if condition1:
    # Code block executed if condition1 is True
elif condition2:
    # Code block executed if condition1 is False and condition2 is True
elif condition3:
    # Code block executed if condition1 and condition2 are False and condition3 is True
...
else:
    # Code block executed if all conditions are False
```

Key points to remember about conditionals in Python:

1. **Indentation**: Python uses indentation (typically four spaces) to indicate the scope of code blocks. The code under each condition (if, elif, else) must be indented consistently.

2. **Comparison Operators**: Conditionals use comparison operators (e.g., `==`, `!=`, `<`, `>`, `<=`, `>=`) to evaluate conditions. These operators compare two values and return a Boolean value (`True` or `False`) based on whether the condition is met or not.

3. **Logical Operators**: You can use logical operators (`and`, `or`, `not`) to combine multiple conditions.

4. **Multiple Elif Blocks**: You can have multiple `elif` blocks to handle different cases if the previous conditions are not met.

Here's an example of using conditionals in Python to determine the grade based on the score:

```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
```

In this example, the program takes the user's score as input and then uses conditionals to determine the corresponding grade based on the score range. The `if` and `elif` conditions are evaluated one by one, and the code block under the first condition that evaluates to `True` is executed. If none of the conditions are met, the `else` block is executed.

## `try` and `except` 
The basic syntax of the `try` and `except` block in Python is as follows:

```python
try:
    # Code block where an exception might occur
    # ...
except ExceptionType:
    # Code block to handle the exception
    # ...
```

Here's how the `try` and `except` block works:

1. The code inside the `try` block is executed.
2. If an exception occurs while executing the code inside the `try` block, the program immediately jumps to the corresponding `except` block.
3. The `except` block handles the exception and allows you to provide specific actions or error messages to handle the exceptional case.

Here's an example that demonstrates using `try` and `except` to handle division by zero:

```python
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integer numbers.")
```

In this example, the program attempts to divide `num1` by `num2`. If `num2` is zero or if the user inputs non-integer values, exceptions (`ZeroDivisionError` or `ValueError`) may occur. The corresponding `except` block handles each of these exceptions and provides an appropriate error message.

You can also use a generic `except` block without specifying the exception type. However, it is generally recommended to catch specific exceptions whenever possible, as it allows you to handle different exceptions differently.

```python
try:
    # Code that may raise an exception
    # ...
except:
    # Code to handle any exception
    # ...
```
## The `while` loop 

It allows you to repeatedly execute a block of code as long as a certain condition is true. It is used when you need to repeat an action until the specified condition becomes false. The basic syntax of the `while` loop is as follows:

```python
while condition:
    # Code block to be executed as long as the condition is True
    # ...
```

Here's how the `while` loop works:

1. The condition is evaluated before the loop starts. If the condition is `True`, the code inside the loop is executed.
2. After each iteration, the condition is checked again. If the condition is still `True`, the loop continues to execute the code block.
3. The loop continues iterating as long as the condition remains `True`. Once the condition becomes `False`, the loop terminates, and the program continues with the code after the loop.

Here's a simple example of a `while` loop that counts down from 5 to 1 and prints the numbers:

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

Output:
```
5
4
3
2
1
```

In this example, the loop starts with `count` set to 5. The condition `count > 0` is `True`, so the loop enters and prints the value of `count`. After each iteration, `count` is decremented by 1 (`count -= 1`), and the loop continues until `count` becomes 0. Once `count` is 0, the condition `count > 0` becomes `False`, and the loop terminates.

It's crucial to ensure that the condition in the `while` loop eventually becomes `False`, or else the loop will run indefinitely, resulting in an infinite loop. An infinite loop can cause your program to hang or become unresponsive.

To avoid infinite loops, you can modify the condition within the loop or use a control variable that changes during each iteration to eventually make the condition false.

```python
# Example with a control variable
total = 0
num = 1

while total < 100:
    total += num
    num += 1

print("Sum:", total)
```

Output:
```
Sum: 105
```

In this example, the loop continues to add `num` to the `total` variable until `total` is greater than or equal to 100. The loop terminates when the condition `total < 100` becomes `False`.


## The `for` loop 
It is used to iterate over a sequence of elements, such as lists, tuples, strings, or other iterable objects. It allows you to perform a specific action on each item in the sequence. The basic syntax of the `for` loop is as follows:

```python
for element in sequence:
    # Code block to be executed for each element in the sequence
    # ...
```

Here's how the `for` loop works:

1. The loop iterates over each element in the `sequence`.
2. For each iteration, the current element is assigned to the variable `element`.
3. The code block inside the loop is executed for each element in the sequence.

Here's a simple example of a `for` loop that prints each element in a list:

```python
fruits = ["apple", "banana", "orange", "grape"]

for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
orange
grape
```

In this example, the `for` loop iterates over each element in the `fruits` list. For each iteration, the current element is assigned to the variable `fruit`, and the `print()` function is used to display the value of `fruit`.

You can also use the `for` loop with other iterable objects, such as strings or tuples

### List Operations
Here are some common list operations in Python:

1. **Creating Lists**:
   You can create a list by enclosing comma-separated values within square brackets `[]`:

   ```python
   numbers = [1, 2, 3, 4, 5]
   fruits = ["apple", "banana", "orange"]
   ```

2. **Accessing Elements**:
   You can access elements in a list using indexing. Indexing starts from 0 for the first element:

   ```python
   fruits = ["apple", "banana", "orange"]
   print(fruits[0])  # Output: "apple"
   print(fruits[2])  # Output: "orange"
   ```

3. **Slicing Lists**:
   You can extract a sublist (slice) from a list using slicing notation:

   ```python
   numbers = [1, 2, 3, 4, 5]
   sub_list = numbers[1:4]  # Elements from index 1 to 3 (4 is exclusive)
   print(sub_list)  # Output: [2, 3, 4]
   ```

4. **Appending Elements**:
   You can add elements to the end of a list using the `append()` method:

   ```python
   fruits = ["apple", "banana"]
   fruits.append("orange")
   print(fruits)  # Output: ["apple", "banana", "orange"]
   ```

5. **Inserting Elements**:
   You can insert elements at a specific index using the `insert()` method:

   ```python
   numbers = [1, 2, 4, 5]
   numbers.insert(2, 3)  # Insert 3 at index 2
   print(numbers)  # Output: [1, 2, 3, 4, 5]
   ```

6. **Removing Elements**:
   You can remove elements from a list using the `remove()` method or by specifying the index with the `del` statement:

   ```python
   fruits = ["apple", "banana", "orange"]
   fruits.remove("banana")  # Remove "banana" from the list
   print(fruits)  # Output: ["apple", "orange"]

   numbers = [1, 2, 3, 4, 5]
   del numbers[3]  # Remove element at index 3 (4th element)
   print(numbers)  # Output: [1, 2, 3, 5]
   ```

7. **List Length**:
   You can get the number of elements in a list using the `len()` function:

   ```python
   numbers = [1, 2, 3, 4, 5]
   length = len(numbers)
   print(length)  # Output: 5
   ```

8. **List Concatenation**:
   You can concatenate two lists using the `+` operator:

   ```python
   list1 = [1, 2, 3]
   list2 = [4, 5]
   combined_list = list1 + list2
   print(combined_list)  # Output: [1, 2, 3, 4, 5]
   ```

9. **List Repetition**:
   You can repeat a list multiple times using the `*` operator:

   ```python
   numbers = [1, 2, 3]
   repeated_list = numbers * 3
   print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
   ```

10. **Checking Membership**:
    You can check if an element is present in a list using the `in` keyword:

    ```python
    fruits = ["apple", "banana", "orange"]
    print("apple" in fruits)  # Output: True
    print("grape" in fruits)  # Output: False
    ```

These are some of the fundamental list operations in Python. Lists are mutable, meaning you can modify them after creation, which makes them powerful and widely used in various programming tasks.

## Comments 


In Python, there are two ways to write comments:

1. **Single-line comments**: To write a single-line comment, use the `#` symbol. Anything after the `#` symbol on the same line will be treated as a comment and ignored by the interpreter.

   ```python
   # This is a single-line comment in Python
   print("Hello, World!")  # This is also a comment
   ```

2. **Multi-line comments**: Python does not have a built-in syntax for multi-line comments like some other programming languages. However, you can use triple quotes (`'''` or `"""`) as a workaround to create multi-line comments. Although these are technically strings, they are not assigned to any variable, so they are effectively treated as comments and ignored.

   ```python
   '''
   This is a multi-line comment in Python.
   It spans multiple lines without the need for # on each line.
   '''
   
   """
   Another way to create a multi-line comment using triple quotes.
   """
   ```


## Set
In Python, a set is an unordered collection of unique elements. Sets are represented by curly braces `{}` and can contain elements of different data types, such as integers, strings, or even other sets. Sets do not allow duplicate elements, so any duplicate items are automatically removed when creating a set. Here's how you can create sets in Python:

```python
# Creating a set
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
```

Python provides several built-in methods and operators to perform various operations on sets. Some common set operations include:

1. **Union (`|`)**: Combines elements from two or more sets, removing any duplicates.

   ```python
   union_set = set1 | set2
   # Output: {1, 2, 3, 4, 5, 6, 8}
   ```

2. **Intersection (`&`)**: Returns a new set containing elements that are present in both sets.

   ```python
   intersection_set = set1 & set2
   # Output: {2, 4}
   ```

3. **Difference (`-`)**: Returns a new set with elements that are present in the first set but not in the second set.

   ```python
   difference_set = set1 - set2
   # Output: {1, 3, 5}
   ```

4. **Symmetric Difference (`^`)**: Returns a new set with elements that are present in either of the sets, but not in both.

   ```python
   symmetric_difference_set = set1 ^ set2
   # Output: {1, 3, 5, 6, 8}
   ```

5. **Subset (`<=`)** and **Superset (`>=`)**: Check if one set is a subset or superset of another.

   ```python
   is_subset = set1 <= set2  # False
   is_superset = set1 >= set2  # False
   ```

6. **Adding Elements**:
   - Use the `add()` method to add a single element to the set.

   ```python
   set1.add(6)
   # Output: {1, 2, 3, 4, 5, 6}
   ```

   - Use the `update()` method or the `|=` operator to add multiple elements to the set.

   ```python
   set1.update({6, 7, 8})
   # Output: {1, 2, 3, 4, 5, 6, 7, 8}

   set1 |= {9, 10}
   # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
   ```

7. **Removing Elements**:
   - Use the `remove()` method to remove an element from the set. Raises a KeyError if the element does not exist in the set.

   ```python
   set1.remove(2)
   # Output: {1, 3, 4, 5, 6, 7, 8, 9, 10}
   ```

   - Use the `discard()` method to remove an element from the set, but does not raise an error if the element does not exist.

   ```python
   set1.discard(5)
   # Output: {1, 3, 4, 6, 7, 8, 9, 10}
   ```

8. **Clearing the Set**:
   - Use the `clear()` method to remove all elements from the set.

   ```python
   set1.clear()
   # Output: set()
   ```

## Dictionary 
It is a versatile and mutable data structure used to store key-value pairs. Dictionaries are represented using curly braces `{}`, and each key-value pair is separated by a colon `:`. Keys within a dictionary must be unique and immutable, such as strings, numbers, or tuples, while values can be of any data type, including other dictionaries. Here's how you can create dictionaries in Python:

```python
# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.8
}
```

In this example, `student` is a dictionary that stores information about a student. The keys are `"name"`, `"age"`, `"major"`, and `"gpa"`, while the corresponding values are `"John Doe"`, `25`, `"Computer Science"`, and `3.8`, respectively.

Dictionaries allow you to perform various operations to manipulate and access the data:

1. **Accessing Values**: You can access the values in a dictionary using the keys.

```python
print(student["name"])  # Output: "John Doe"
print(student["gpa"])   # Output: 3.8
```

2. **Updating Values**: You can update the values of keys in a dictionary.

```python
student["age"] = 26
student["gpa"] = 3.9
```

3. **Adding New Items**: You can add new key-value pairs to the dictionary.

```python
student["university"] = "ABC University"
```

4. **Removing Items**: You can remove items from the dictionary using the `del` keyword.

```python
del student["major"]
```

5. **Checking Key Existence**: You can check if a key exists in the dictionary using the `in` keyword.

```python
if "age" in student:
    print("Age is present in the dictionary.")
```

6. **Dictionary Methods**: Dictionaries have various built-in methods, such as `keys()`, `values()`, and `items()`, which return lists of keys, values, and key-value pairs, respectively.

```python
keys_list = student.keys()
values_list = student.values()
items_list = student.items()

print(keys_list)   # Output: dict_keys(['name', 'age', 'gpa', 'university'])
print(values_list) # Output: dict_values(['John Doe', 26, 3.9, 'ABC University'])
print(items_list)  # Output: dict_items([('name', 'John Doe'), ('age', 26), ('gpa', 3.9), ('university', 'ABC University')])
```


## Module 
It is a file containing Python definitions and statements. Modules allow you to organize your code into reusable units and help avoid naming conflicts. A module can define functions, classes, and variables that can be used in other Python programs. Python provides a vast standard library of modules that you can use directly in your code. Additionally, you can create your own custom modules to encapsulate functionality and promote code reusability.

Here's how you can use modules in Python:

1. **Importing a Module**:
   To use the functions, classes, or variables defined in a module, you need to import it into your Python script. You can import the entire module or specific items from the module.

   ```python
   # Import the entire module
   import math
   print(math.sqrt(25))  # Output: 5.0

   # Import specific items from the module
   from math import sqrt, pi
   print(sqrt(25))  # Output: 5.0
   print(pi)       # Output: 3.141592653589793
   ```

2. **Creating Your Own Module**:
   To create a custom module, you need to create a new Python file with the desired functions, classes, or variables. Save the file with a `.py` extension. You can then import and use this module in other Python scripts.

   **Example - my_module.py**:
   ```python
   def greet(name):
       return f"Hello, {name}!"

   def add(a, b):
       return a + b
   ```

   **Using the custom module in another script**:
   ```python
   import my_module

   print(my_module.greet("Alice"))  # Output: "Hello, Alice!"
   print(my_module.add(2, 3))      # Output: 5
   ```

3. **Using Aliases**:
   You can use aliases to provide a shorter name for a module when importing it.

   ```python
   import math as m
   print(m.sqrt(25))  # Output: 5.0
   ```

4. **Standard Library Modules**:
   Python comes with a standard library that includes many modules for various purposes. You can use these modules directly by importing them into your code.

   ```python
   import random
   print(random.randint(1, 10))  # Output: Random integer between 1 and 10
   ```

5. **Third-Party Modules**:
   In addition to the standard library, Python has a vast ecosystem of third-party modules created by the community. You can install these modules using package managers like `pip` and then import and use them in your code.

   ```python
   # Install a third-party module using pip
   # pip install requests

   import requests
   response = requests.get("https://www.example.com")
   print(response.status_code)  # Output: 200 (if successful)
   ```

## OOPS 
It stands for Object-Oriented Programming (OOP), is a programming paradigm that revolves around the concept of "objects." It is a way of organizing and designing code based on real-world entities and their interactions. Python fully supports OOP, and it is one of the reasons why Python is popular for its readability, simplicity, and flexibility.

In OOP, the fundamental building blocks are:

1. **Class**: A class is a blueprint for creating objects. It defines the structure and behavior of objects. Think of a class as a template or a blueprint for objects of a specific type. For example, a `Car` class can have attributes like `color`, `brand`, and `model`, as well as methods like `start_engine()` and `stop_engine()`.

   ```python
   class Car:
       def __init__(self, color, brand, model):
           self.color = color
           self.brand = brand
           self.model = model

       def start_engine(self):
           print("Engine started")

       def stop_engine(self):
           print("Engine stopped")
   ```

2. **Object**: An object is an instance of a class. It represents a specific realization of the class, with its own unique data and attributes. For example, you can create multiple `Car` objects, each with different colors, brands, and models.

   ```python
   car1 = Car("Red", "Toyota", "Corolla")
   car2 = Car("Blue", "Honda", "Civic")
   ```

3. **Attributes**: Attributes are variables that store data within an object. They represent the characteristics or properties of an object. In the `Car` class above, `color`, `brand`, and `model` are attributes.

4. **Methods**: Methods are functions defined within a class that operate on the object's data. They represent the behavior or actions that an object can perform. In the `Car` class above, `start_engine()` and `stop_engine()` are methods.

5. **Encapsulation**: Encapsulation is the concept of bundling data (attributes) and methods that operate on that data within a single unit (i.e., the class). It helps in hiding the implementation details from the outside world and allows controlled access to the object's data and behavior.

6. **Inheritance**: Inheritance is a mechanism that allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reusability and helps to create a hierarchy of classes. The subclass can add its own unique attributes and methods or override the inherited ones.

7. **Polymorphism**: Polymorphism allows different classes to be treated as if they are objects of a common parent class. It enables flexibility and dynamic behavior in the code.
