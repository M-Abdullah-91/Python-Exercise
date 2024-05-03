# write a program to check if the number is positive, negative or zero


num = int(input("Enter a Number: "))
if num>0:
    print(f"{num} is positive number")
elif num<0:
    print(f"{num} is Negative Number")
else:
    print(f"{num} is Zero")