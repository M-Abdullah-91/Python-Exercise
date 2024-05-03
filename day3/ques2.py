# Given a list of Number, find all the number number and store them in a new list


numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)