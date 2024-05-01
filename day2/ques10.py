# write a program a to check a number is prime or not

number = int(input("Enter a Number: "))

for i in range(2,number):
    if number % i ==0:
        print(f"{number} is Not prime Number")
        break
else:
    print(f"{number} is  prime Number")