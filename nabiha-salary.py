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
