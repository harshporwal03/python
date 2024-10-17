list=[10,20,30,40,50]
print(list[0])
print(list[-1])
print(list[1:3])
m=len(list)//2
print(list[::-1][m:]+list[m+1:])
list[0]=100
for i in list:print(i)

list.append("durga")
print(list)

list2=list*2
print(list2)

l=[[1,2,3 ,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,],[19,20,21,22,23,24,25,26,27]]

list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
list1=list1+list2
print(list1)

list=range(0,4)
print(type(list))
print(list)

listOfAirPlanes = ['AI','EA','VI']
print("iterating the list")
for index in range(len(listOfAirPlanes)):
  print(listOfAirPlanes[index])

print("iterating the list using keyword")
for airline in listOfAirPlanes:
  print(airline)


