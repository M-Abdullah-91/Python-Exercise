principal = int(input("Enter Principal amount: "))
rate = int(input("Enter interest rate: "))
time = int(input("Enter time period in years: "))


compound = principal*(1 + rate/100) ** time

print(compound)