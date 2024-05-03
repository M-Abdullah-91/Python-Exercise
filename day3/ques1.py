# create a program that takes a year as input and return if it is leap year or not.


year = int(input("Enter a year: "))

if (year%4==0 and year%100 !=0) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")