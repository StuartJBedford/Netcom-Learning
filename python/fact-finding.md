# Fact finding exercise

**Define a list and tuple in python:**

- a list is a collection of things that are ordered and changeable
- a tuple is a collection of things which are ordered but unchangeable but allow duplicate values

**What is a namespace in python?**

- a namespace is a collection of currently defined names along with information about the object the name references, kind of like a dictionary, keys are the object name and value are the objects themselves

**what is the difference between a local variable and a global variable**

- a local variable is a variable that has been defined inside a function, it can only be used by that function and attempts to call the variable from another function would result in an undefined error

- a global variable is a variable that is created outside a function, it can be called and used by everyone, both inside and outside functions

x = "hello" like this is a global function

def function():
x = "world" - this would be a local variable

**what is an IDE?**

- An IDE is a piece of software that help programmers develop code more efficiently
- usually contains a code editor, build automation tool and a debugger
- example of an IDE would be VSCode, PyCharm, IntelliJ, Atom

**What are modules in python?**

- a module is a file in which you put a set of functions that can then be used in other projects,documents by using the import statement

inside a myModule.py file you do something like

def greeting(name):
print("Hello " + name)

and in your other document/project you call that module by importing like below

import myModule for example

**Difference between an array and a list**

- Array and list are data structures in Python that are used to store the data in a specific order. Arrays are useful for storing data that needs to be accessed in a specific order, such as a list of student names or a sequence of numbers, while lists are mutable, meaning that they can be changed after they are created.
- arrays are also great for numerical operations while lists cannot directly handle math operations

**What are operators?**

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

- arithmatic operators are + - / and /\*

- assignment operators are things like =, +=, /=, >>=
