list1=[1,2,3,4,5]
list2=[10,20,30,40,50]
list3=[]
def add_corr(a,b,c,d,e,f,g, h,i,j):
    return a+f,b+g,c+h,d+i,e+j
list3=list(add_corr(1,2,3,4,5,10,20,30,40,50))
sortedlst= sorted(list3)#, reverse=True
print(sortedlst, )
##write a single for loop to add corresponding elements of the two lists
def add_list(list1,list2):
  for list1, list2 in zip(list1,list2):
      list=[]
      list3.append(list1+list2)
      return list
list3=add_list(list1,list2)
print(list3)
  
 