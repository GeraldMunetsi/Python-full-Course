#reusable code that performs tasks
#define a function
#def function_name(parameters):
    # Function code block
    # ...
    # ...
def greet(name):
    print("Hello", name )

# Calling the function with an argurment
greet("Gerald")
#returning a value ,the return functiom ends the function execution and sends a value back to the caller
def add(a, b):
    return a + b

# Calling the function and storing the returned value
result = add(3, 5)
print(result)

#acessing global variables
x = 10
def my_function():
    print(x)  # Accessing the global variable

my_function()  # Output: 10

#modifying global varibles
x = 10
def modify_global():
    global x  # Indicating that x is a global variable
    x = 20  # Modifying the global variable

print(x)  # Output: 10
modify_global()
print(x)  # Output: 20

#local variables take preceedance
x = 10
def my_function():
    x = 5  # A local variable with the same name as the global variable
    print(x)  # Accessing the local variable

my_function()  # Output: 5
print(x)  # Output: 10
#nested functions and scope
def outer_function():
    x = 10

    def inner_function():
        nonlocal x  # Accessing the x variable from the outer function
        x += 5
        print(x)

    inner_function()  # Output: 15

outer_function()

#1 functions with default parameter
def greet(name="there"):
    print("Hello, " + name + "!")

greet()  # Output: Hello, there!
greet("Alice")  # Output: Hello, Alice!
#2
def isnumberInRange(num, i=25,n=100):
    if num  in range(i,n):
        print("Found")
    else:
            print("Not Found")
isnumberInRange(20) # default ,i and n dont change
isnumberInRange(20,0)
isnumberInRange(20,0,10)
### 
def lstAppend(a="",L=[]):
            L.append(a)
            return L
result=lstAppend("c")
print(result)
##
def lstAppend(a="",L=None):
            if L is None:
                L=[]
                L.append(a)
                return L
result=lstAppend("c")
print(result)

##22
def fun(arg1,arg2=0, arg3=1,arg4=0):
            print(arg1,arg2,arg3,arg4)
            
fun("king")
fun(arg1=10)
### funtions and dictionaries
#adding a key valie yo a dictionary
def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value

student = {'name': 'John', 'age': 20}
add_to_dictionary(student, 'major', 'Computer Science')
print(student)  # Output: {'name': 'John', 'age': 20, 'major': 'Computer Science'}
   ##
def get_value(dictionary, key):
    return dictionary.get(key)

student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}
value1 = get_value(student, 'major')
value2=get_value(student, 'age')
print(value1,value2)  # Output: Computer Science
   


    
