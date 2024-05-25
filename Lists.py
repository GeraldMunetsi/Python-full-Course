listspeople=["Gerald","Shean","Shanelle"]
print("My family\n:{}".format(listspeople))
listsatypical=["Gerald",4,"Shanelle"]
print("Mixed\n:{}".format(listsatypical))
#concancenation
listsconca=listspeople+listsatypical
print("Concat\n[",listsconca)
#length of a list
print("Lenght of a list\n", len(listsconca))
#refer to item in a list by an index
print(listsconca[3])
print(listsconca[-2])
#slice list with [startindx:endindx]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start_index = 2
sliced_list = my_list[start_index:]
print(sliced_list) 
 # Output: [3, 4, 5, 6, 7, 8, 9, 10]
print("Listsconca[2:]", listsconca[2:])
#USE CASES OF ENUMERATE FUNCTION
#uusing the enumerate() funtion
#enumerate(iterable, start=0)
my_list = ['apple', 'banana', 'cherry', 'date']
#start_index = 1
for index, fruit in enumerate(my_list, start=1):
    print(index, fruit)
# Output:
# 1 banana
# 2 cherry
# 3 date

#The `enumerate()` function can be used to iterate over a list and modify its elements in place. In this example, each fruit is converted to uppercase using the `upper()` method.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    fruits[index] = fruit.upper()
print(fruits)

#By using `enumerate()`, you can easily create a dictionary where the indices serve as keys and the corresponding elements from the iterable serve as values.fruits = ['apple', 'banana', 'cherry']
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)
#Here, `enumerate()` is useful for searching a specific element (`'banana'` in this case) in a list and retrieving its index.
fruits = ['apple', 'banana', 'cherry']
target_fruit = 'banana'
for index, fruit in enumerate(fruits):
    if fruit == target_fruit:
        print(f"The index of {target_fruit} is {index}")
        break
#USE CASES OF RANGE FUNCTION IN LISTS



#unlike strings lists are mutable(add new elements, rwmove without creating another list)
#assign an index
listspeople[0]="Tapo"
print(listspeople)
#assign to a slice
listspeople[0:1]=["Tapo","King"]
print(listspeople)
#listspeople[0:1]=[]
print(listspeople)

#append
listspeople.append("Shy")
print(listspeople)


#clear a list by assigning to an empy list
#listspeople[:]=[]
print(listspeople)
#create lists from other lists
sublistspeople=listspeople[0:2]
print(sublistspeople)
#create lists from other lists
listscombined= [(listspeople[2]).upper(),listsatypical[0]+"Queen"]
print(listscombined)
#nest lists
nested_list=[listspeople,listscombined]
print(nested_list)
print(nested_list[0],nested_list[0][1])
nested_list.append("Hhh")
print(nested_list)
#k
lst1=[2,2,3,4,5]
lst2=[6,7,8,9,10]
lst1.append(-2.5)
print(lst1)
#extend function
lst2.extend(lst1)
print(lst2)
#remove
lst1.remove(-2.5)
print(lst1)
#insert at an index say 3
lst1.insert(3, 20)
print(lst1)
#remove item at an index say 3
del lst1[3]
print(lst1)
#remove and returns the last item in the list
lst2.pop()
print(lst2)
#returns the index in list1 of the first item whose value is 2
print(lst1.index(2))
#counts number of appearance of an item
print(lst1.count(2))
#reverse items
lst1.reverse()
print(lst1)
#sort
lst1.sort()
print(lst1)
#remove all items from the list
lst1.clear()
print(lst1)
