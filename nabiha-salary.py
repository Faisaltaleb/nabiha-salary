salary = float(input("Enter your salary:"))
month = input ("Enter the month that yu're storing the salary:")
savings_percentage = float(input("Enter the percentage for savings :"))
electricity_percentage=float(input("Enter the percentage for rent:"))
rent_percentage=float(input("Enter the percentage for the rent:"))

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

print ("/nYour salary is ",salary,"in the month of ",month)
print ("/nYour savings for ",month," is ",savings)
print ("/nYour rent for ",month," is ",rent)
print ("/nYour electricity for ",month ," is ",electricity)
print ("/nYour total expenses for " ,month, "is" ,totalexpenses)
print("/n After these expeneses the amout remaining is :",remainder)
print("/nThe yearly rent cost is ",yearlyrent,"and the yealry elecricity expenses is ",yearlyelec)
print("/nYour salary raised for the power of two JUST FOR FUN is ",salarysq)
print("/nAdditional savings of 50$ dividedby your savings is ",savings_division)






