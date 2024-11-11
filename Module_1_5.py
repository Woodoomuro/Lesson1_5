immutable_var=('z',2,'a',4)#('z', 2, 'a', 4)
print(immutable_var)
print(type(immutable_var))#<class 'tuple'>
#immutable_var[1]=[5]
#print(immutable_var) #TypeError: 'tuple' object does not support item assignment

mutable_list=[234,'apple',432]
print(type(mutable_list))#<class 'list'>
mutable_list[0]=6789
print(mutable_list)#[6789, 'apple', 432]

