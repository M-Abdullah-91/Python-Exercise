# program to convert a given number of min into hr.


minutes = int(input("Enter number of minutes: "))

hr = minutes/60
min = minutes%60

print(f'Hours: {hr}')
print(f'Remaining minutes: {min}')