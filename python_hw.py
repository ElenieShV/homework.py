# HomeworkPython

a=float(input("Enter first number"))
b=float(input("Enter second number"))
c=float(input("Enter third number"))
sum=a+b+c
product=a*b*c
print("Sum of numbers",sum)
print("Product of numbers",product)


d1=float(input("Enter diagonal 1:"))
d2=float(input("Enter diagonal 2:"))
area=(d1*d2)/2
print ("area of rhombus:", area)


salary=float(input("Enter monthly salary:"))
loan=float(input("Enter loan payment:"))
utilities=float(input("Enter utilities payment:"))
balance=salary-loan-utilities
print("Balance amount:", balance)


distance=float(input("Enter distance (km):"))
consumption=float(input("Enter fuel consumption for 100 km (l):"))
price_per_liter=float(input("Enter fuel price for 1 liter (euro):"))
total_cost=(distance/100)*consumption*price_per_liter
print("Total trip's price (euro):", total_cost)
