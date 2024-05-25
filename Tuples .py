#Tuples are immutable
tuple1=()
print(tuple1)
tuple2=(1,2,3,4,5)
#find lenght
print(len(tuple2))
#index
print(tuple2[3])
tuple3=(tuple1,tuple2)
print(tuple3)
#slice tuples
print(tuple3[1][0])
#tuple packing
tuple4=1,2,3
print(tuple4,len(tuple4))
#unpack
x,y ,z=tuple4
print(x,y,z)
