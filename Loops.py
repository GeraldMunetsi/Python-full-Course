#for item in sequence:
    # Code to be executed
words=["cat","dog","giraffe"]
for animal in words:
    print(animal, len(animal))
    
#RaNGE FUNCTION
#range(start, stop, step)
#for variable in range(start, stop, step):
    # Code to be executed
for i in range(5):
    print(i)
for number in range(10, 0, -1):
    print(number)
    
numbers = list(range(1, 6))
print(numbers)
print(len(numbers))

words=["jane","munashe","shean","shanelle"]
wordlist=[]
for i in range(len(words)):
    wordlist.append([words[i]])
    print(wordlist)
#with break statements
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

print("Loop finished")
#
r=range(0,20,2)
print(r)
print(list(r))
#true or false
print(range(0)==range(2,1,3))
print(range(0))
print(range(5))

