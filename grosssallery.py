a=input("enter male or female: ")
b=int(input("enter salary: "))

if a=="male":
    net_salary=b+(5/100*b)
else:
    net_salary=b+(10/100*b)

print("Total Salary: ", net_salary)