l=[1,1,1,2,2,2,3,3,3,4]
s=set(l)
li=list(s)
print(li)
s=0
for i in li:
  s += int(i)
print(s)