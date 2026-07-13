# Salary Calculator

name=input("Enter Your Name: ")
basic_salary=float(input("Enter your Basic Salary: "))
                 
hra = basic_salary*20/100
da = basic_salary*10/100
gross = basic_salary + hra + da

print("\nName: ",name)
print("Base Salary: ",basic_salary)
print("HRA: ",hra)
print("DA: ",da)
print("Gross Salary: ",gross)