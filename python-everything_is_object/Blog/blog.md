
![Image](https://i.postimg.cc/LshGZL8Y/image.jpg)


## Introduction
This blog explores how Python stores objects in memory, how the language distinguishes identity from type, and why some objects can change while others cannot. These concepts reveal why certain operations behave unexpectedly, why function arguments sometimes update, and how Python manages memory behind the scenes. I will be breaking down everything I have learned in this project, with clear examples showing how identity, mutability, and function semantics work in real Python environments.

## id and type

Python offers several methods for identifying an object’s type, with the most basic ones being the built-in **type()** and **id()** functions.  
`type()` provides a quick way to check an object’s type, while `id()` returns the unique identifier of an object—an integer representing the memory address.

### TYPE()

#### How `type(obj)` Works
Used for type inspection and also for dynamic class creation  
- **object:** the object whose type you want to check  
- **name:** a string with the class name  
- **bases:** a tuple of base classes  
- **dict:** dictionary containing attributes and methods  
- **returns:**  
  - one argument → the type of the object  
  - three arguments → a new class object  

#### Why use `type()`
- Essential for understanding and creating objects in Python  
- Single argument → returns the class of an object  
- Three arguments → dynamically creates new types  
- Important for introspection and dynamic typing  

#### Example 1: Checking the type of objects

```
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Grâce"))   # <class 'str'>
```
#### Example 2: Comparing types
```
a = [1, 2, 3]
b = [1, 2, 3]
print(type(a) is type(b)) # Ouput: True
a is b # Output: False (they are not the same object)
```
###Example 3: Checking types of built-in structures
```
print(type({1, 2, 3})) # Output: <class 'set'>
print(type({"a": 1, "b": 3})) # Output: <class 'dict'>
print(type((1, 2, 3))) # Output: <class 'tuple>
```
### ID()

#### How `id(obj)` Function Work? 
- Returns the unique idenyifier of an object.
- **object:** The object whose unique identifier you want to retrieve.
- **returns:**  An interger representing the identity of the given object.

#### Why Use `id(obj)`
- Helps understand how Python handles objects in memory
- See if two variables refer to the same object
- Useful for debugging
- Helpful for understanding the behavior of mutable vs immutable objects

#### Example 1: Getting the id of an object.
The 'id()' returns the mnemory address of the integer 30, which is unique during the object's lifetime.
```
a = 30 
print(id(a)) # Output: a unique integer, e.g, 123442
```

#### Example 2: Comparing ids of variables.
This example uses id() to check is two variables refer to the same object.
```
a = [1, 2, 3]
b = a # this mean a and b are refering to the same id because they are using the same list
c = [1, 2, 3] # this represents a new object with the same value so it also not share the same list as a and b

a == b # Output: True
a == c # Output: False
``` 
### Mutable Objects
Mutable objects are types like Python lists, Python dicts, Python sets, or Python bytearray. Custom classes are generally mutable, meaning they can be changed after being created.

#### Example 1: observing changes in mutable objects
```
a = [1, 2 , 3]
print(id(a)) # Output: inital id

a.append(4) # modify the object
print(id(a)) # Output: same id
```

### Immutable Objects
Immutable objects operate the opposite way from mutable ones — they cannot be changed once created. Any modification creates a new object.
Common immutable types include integers, strings, floats, complex, tuples and bytes.

#### Example 1: IDs of immutable objects
```
a = 10
b = 10
a == b    # True (same value)
a is b    # True in CPython for small integers
```

#### Example 2: an immtable string (using tuple)
```
first_string = "Hi"
# first_string[3] = "Thomas" # This will raise an error 
second_string = first_string + "Thomas" # This creates a new string since we cannot append like with mutable objects
print(second_string)
```

### The difference between assignment and referencing
In Python, assignments is the process of binding a new to an objects, whereas, variables are references to objects. when a value is assigned to a variable, it creates a reference to the object that represnts the value. 

#### How assignments work:
Assignmenst use the following syntax: variable = expression. The expression on the right-hand sideis evaluated, and its value is then assigned to the variable on the left-hand. 

#### Example code: Assigning the value 30 to the variable 'a'
```
a = 30
print(a)
```

#### How referencing work:
Variables are references to objects. When a value is assigned to a variable, it creates a reference to the object that represents the value.

#### Example code: Illustrating Python references
```
a = [1, 2, 3]
b = a
b.append(5)
print(a)
print(b)

Output: both 'a' and 'b' refer to the same list object. When modifying the list through the b refrence by appending 5, the change is reflected in both a and b.
```

### How an immutable object is stored in memory?
Python stores immutable objects so that their value cannot be changed in place.
Instead of modifying the memory block, Python:
- creates a new object
- assigns the name to this new object
- leaves the old object unchanged
This is why operations like += on integers or strings create new memory objects.

#### Example code:
``` 
x = 5
print(id(x))

x = x + 1
print(id(x))  # different id → new object created
```

### Memory schema
#### Diagram 1 (Aliasing): it portrays both a and b variables refer to the same object:
``` 
a = [1, 2, 3]
b =a 
a is b # Output: True 

   a 
    \
      \  
        >
          [1, 2, 3]
       >
      /   
    /
   b 
``` 

#### Diagram 2: a and b have the same value but do not refer to the same object.
``` 
a = [1, 2, 3]
b = [1, 2, 3]
a == b True
a is b False

a ---->[1, 2, 3]
b ---->[1, 2, 3]
``` 

### Why does it matter and how differently does Python treat mutable and immutable objects:
Understanding mutability helps write efficient and bug-free code.
For example, when passing arguments to functions, mutable objects can be modified inside the function, which affects the original object. Immutable objects cannot be changed inside the function, so they remain the same unless reassigned.

### How arguments are passed to functions and what does that imply for mutable and immutable objects:
Arguments are passed to functions by object reference. This means that mutable objects can be changed within the function (original objects can be updated), while immutable objects cannot (a new object must be created). Understanding this concept is essential to avoid unintended side effects and bugs.

### How variable value are managed when passing to a function? (by assignment)
Python follows a model called call-by-object or call-by-assignment.
This means:
- The function receives the object reference
- If the object is mutable → function can modify it
- If the object is immutable → function cannot modify the original

#### Example 1:
```
def func(x):
    x.append(99)

a = [1, 2]
func(a)
print(a)   # modified
```

#### Example 2:
```
def func(n):
    n = n + 1

x = 5
func(x)
print(x)   # unchanged
```

### Integer pre-allocation? (262 first integers created when CPython starts)
CPython pre-allocates small integers to improve performance.
**These are:**
- from -5 to 256 (inclusive)
**This means:**
- integers in this range are reused
- variables referencing them will often share the same id

#### Example code:
```
a = 10
b = 10
a is b   # True
```

### The mechanism of aliases
Aliasing occurs when two or more variables reference the same object. In general, it is safer to avoid aliasing when you are working with mutable objects. Of course, for immutable objects, there’s no problem. That’s why Python is free to alias strings when it sees an opportunity to economize.

#### Example code:
```
a = [1, 2, 3]
b = a
a is b
True
```

### NSMALLPOSINTS, NSMALLNEGINTS
These constants define how many small integers Python pre-allocates.
- NSMALLPOSINTS = 257 (for 0 through 256)
- NSMALLNEGINTS = 5 (for -1 through -5)

**They are used internally by CPython to:**
- speed up integer creation
- reduce memory fragmentation
- avoid re-creating common integer objects

#### Why NSMALLPOSINTS and NSMALLNEGINTS have those values?
- Small integers (especially between -5 and 256) are used extremely often
- These values appear constantly in loops, indexing, slicing, boolean logic, counting, and interpreter operations
- Pre-allocating them avoids creating thousands of identical integer objects

### Tuple and Frozen Set
Tuples and frozensets are immutable containers, but their elements can be mutable.

#### Example code:
```
a = [1, 2]
b = (a, 3)
```
The tuple cannot change, but a inside it can be modified.

**Same for frozenset:**
```
fs = frozenset([3, 4, 5])
```

Elements cannot be changed unless they themselves are mutable.
This is why "immutable container" is not the same as "contains only immutable elements".

### Conculsions
Understanding Python objects, referencing, mutability, assignment, and memory handling is essential for writing reliable code. By knowing how Python stores and manages objects behind the scenes, it becomes easier to predict behavior, avoid side effects, debug problems, and write more efficient programs.


