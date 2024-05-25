#a set is an unordered collection with no duplicates elements
#use cases are membership.testing, eliminating duplicate entries
#mathematical calculations such as unions ,intersections
#removing duplicates
basket={"apple","apple","bananas","oranges"}
print(basket)
#testing for membership
print("apple" in basket)
#another way to declare single character sets
someChar=set('2,3,4,¥,&,$')
print(someChar)
#set operations
set1=set('gerald')
set2=set('shean')
#union
print(set1| set2)
# intersection
print(set1 & set2)
#difference
print(set1 -set2)
#asymetric difference
print(set1^set2)
