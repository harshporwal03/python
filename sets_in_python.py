'''a = {1,2,3,4,1}
print(type(a))
print(a)

it does not contain repetitive variables
'''

a={}
print(type(a))

b=set()
print(type(b))

# Set Methods

'''
a = {1,2,3,4,1}
print(a)
a.add(5)
print(a)
a.add((1,2,3,4)) #tuple can be added
#a.add([1,2,3,4,1]) #it will show error cuz list or dictionary cannot be added in a set
a.remove(1)
print(a)
a.discard(1)
print(a)
a.clear()
print(a)
print(len(a)) #prints the length
a.pop() 
a.unions() 
a.intersect()
'''