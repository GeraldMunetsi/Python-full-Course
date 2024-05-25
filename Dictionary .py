#dictionaries are unodered set of <key:values>  were the key values are immutable type
# and must be unique within one dictionary.Dictionaries are indexed by keys
#associative memories
#emptu dictionary
grade1={}
#dictionaries separated by comma key value pairs, string keys
grade2={'joy':10,'shean':30,'shanelle':50}
print(grade2)
#tuple keys
student_grades = {("John", "Smith"): "A", ("Emma", "Johnson"): "B+", ("Michael", "Brown"): "A-"}
print(student_grades)
#floating keys
stock_prices = {2.5: "GOOG", 1.8: "AAPL", 3.2: "MSFT"}
#Boolean keys
attendance = {True: "Present", False: "Absent"}
#Mixed type
data = {42: "Answer", "key": "value", (1, 2, 3): [4, 5, 6]}
grades3=dict([('Jack', 20),('king',10)])
print(grades3)
#returns all the keys in yhe dicgionary
print(grades3.keys())
#returns all keys used in the dictionary in asorted way
print(sorted(grades3.keys()))
#you can provide the key to extract the corresponding value
#print(grades3['jack'])
#testing membership
print( 'Answer' in data)



# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# Modifying values
person["age"] = 31
print(person["age"])   # Output: 31

# Adding new key-value pairs
person["occupation"] = "Engineer"
print(person)          # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

# Removing a key-value pair
del person["city"]
print(person)          # Output: {'name': 'John', 'age': 31, 'occupation': 'Engineer'}
#LOOPS IN DICTIONARIES
#retrieving the keys and corresponding values in aloop using the items() method
grade2={'joy':10,'shean':30,'shanelle':50}
for k,v in grade2.items():
    print(k,v)
 #using the enumerate funtion in looped sequence
points=[2,5,3,7]
for k, v in enumerate(points,start=1):
     print(k,v)
 #loop over 2 or more sequence
# the entries can be paired with zip()fun
names=["gerald","munashe","shean","tapo"]
points=[2,5,3,7]
for n, p in zip(names,points):
    print(n,p)
    #sorting
for x in sorted(grade2.keys()):
    print(x)
   
#looping over a sequence in reverse, reverse function
for x in reversed(sorted(grade2.keys())):
    print(x)
print((1,2,3)<(1,2,4))
