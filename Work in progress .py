print("hello")
A={
'king':{'a':'5','b':'6'},
'queen':{'c':'1','d':'6'}}
for director, movieRatings in A.items():
    print(director,movieRatings)
for movie, rating in movieRatings.items():
    print(movie, rating)
print("-"*60)

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()

print(keys)  # Prints: dict_keys(['a', 'b', 'c'])

# You can also convert the view object to a list if desired
key_list = list(keys)
print(key_list)  # Prints: ['a', 'b', 'c']