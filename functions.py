def wish():
  print("Hello Good Morning")
wish()
wish()

def add(x,y):
  return x + y
result=add(10,20)
print("The sum is",result)
print("The sum is",add(100,200))

def even_odd(num):
  if num%2==0:
    print(num,"is Even Number")
  else:
    print(num,"is Odd Number")
even_odd(10)
even_odd(15)

def fact(num):
  result=1
  while num>=1:
    result=result*num
    num=num-1
  return result
for i in range(1,5):
  print("The Factorial of",i,"is",fact(i))

def calc(a,b):
  sum=a+b
  sub=a-b
  div=a/b
  mul=a*b
  return sum,sub,mul,div
t=calc(100,50)
print("The Results are",t)