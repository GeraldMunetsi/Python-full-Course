#Sorting,increasing or decreasing
var=[45,30,21,50]
sortvar=sorted(var)#increasing
print(sortvar)
sortvar=sorted(var, reverse=True)# reverse to decreasing
print(sortvar)
from operator import itemgetter
var=[('Carl', 45),  ('Amy', 30),('Zach', 21),  ('Jane', 50)]
sortvar=sorted(var)
print(sortvar)
sortvar=sorted(var, reverse=True)
print(sortvar)
sortvar=sorted(var, key=itemgetter(0))
print(sortvar)
sortvar=sorted(var, key=itemgetter(1), reverse=True)
print(sortvar)
var={'Carl':45,  'Amy':30,'Zach':21,  'Jane': 50}
var["Carl"]
print(var)
#sortvar=sorted(var.items())
#print(sortvar)
