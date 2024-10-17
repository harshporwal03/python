a = int(input("enter the age : "))
if(a>=17):
    print("Eligible")
else:
    print("Not eligible")
    a=18-a
    print("you have to wait for : " +str(a))