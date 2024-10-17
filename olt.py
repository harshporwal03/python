greet="hi"
print(greet.center(4,'-'))
print(greet.center(5,'*'))
print(greet.center(6,'>'))
print(greet.center(2,' '))

str="HELLO WORLD"
print(str.isupper())

print(str.replace('HELLO','HI'))

print(greet.replace('hi','Yo DADDY'))

print(str.split())

s='''Python
is a
programming language'''
print(s.splitlines())

a=input("Enter some text: ")
print(a[::-1])

b=input("Enter some text 2: ")
print(''.join(reversed(b)))

s1="banana"
print (s1.find("an",2))

print(s1.index("ana"))


cities=['Mumbai','London','Paris','New York']
new_cities=['Delhi', 'Chicago']
cities.extend(new_cities)
print("Updated List: ",cities)

cities.insert(5,'Hamirpur')
print(cities)

numsar=[354,524,548,1,5,21,9,2255,2]
numsar.sort()
print("ascending order: ",numsar)
numsar.sort(reverse=True)
print("descending order: ",numsar)

abc = ['a','n','d','k','t','l','j','D','R','W','R','F','H']
abc.sort()
print("ascending order: ",abc)
abc.sort(reverse=True)
print("descending order: ",abc)



