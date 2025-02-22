months =["january","february","march","april","may","june","july","august","september","october","november","december"]
salary = float(input("Enter your salary:"))
while salary < 0 or salary==0 or salary == " ":
    print("Invalid salary")
    salary = float(input("Enter your salary again:"))
month = input ("Enter the month that yu're storing the salary:").lower()
while month not in months:
    print("Invalid month")
    month = input("Enter the month again:").lower()

savings_percentage = float(input("Enter the percentage for savings :"))
electricity_percentage=float(input("Enter the percentage for rent:"))
rent_percentage=float(input("Enter the percentage for the rent:"))
while savings_percentage < 0 or savings_percentage > 100 or electricity_percentage < 0 or electricity_percentage > 100 or rent_percentage < 0 or rent_percentage > 100:
    print(" Thes iput of the percentages is wrong , please enter them again")
    savings_percentage = float(input("Enter the percentage for savings again:"))
    electricity_percentage=float(input("Enter the percentage for rent again:"))
    rent_percentage=float(input("Enter the percentage for the rent again:"))

savings = (savings_percentage/100)*salary
rent =(rent_percentage/100)*salary
electricity= (electricity_percentage/100)*salary

totalexpenses= savings + rent + electricity

remainder= salary - totalexpenses

yearlyrent=rent*12
yearlyelec=electricity*12

salarysq= salary**2

extra_savings= 50
savings_division=extra_savings/savings

print ("Your salary is ",salary,"in the month of ",month)
print ("Your savings for ",month," is ",savings)
print ("Your rent for ",month," is ",rent)
print ("Your electricity for ",month ," is ",electricity)
print ("Your total expenses for " ,month, "is" ,totalexpenses)
print("After these expeneses the amout remaining is :",remainder)
print("The yearly rent cost is ",yearlyrent,"and the yealry elecricity expenses is ",yearlyelec)
print("Your salary raised for the power of two JUST FOR FUN is ",salarysq)
print("Additional savings of 50$ dividedby your savings is ",savings_division)






