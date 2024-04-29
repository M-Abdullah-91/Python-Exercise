num1 = int(input("Enter first number: "))   # 1
num2 = int(input("Enter second number: "))  # 2

print(f"Before Swapping: num1={num1}\t num2={num2} ")

num1 = num1 + num2 # 1+2 = 3
num2 = num1 - num2  # 3 - 2 = 1
num1 = num1 - num2  # 3 -1 = 2

print(f"After Swapping: num1={num1}\t num2={num2} ")