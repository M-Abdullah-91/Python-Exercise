no_of_days = int(input("Enter number of Days: "))

year = int(no_of_days/365)
week = int((no_of_days%365)/7)
remaining_days = int((no_of_days%365)%365)



print(f"{year} Year")
print(f"{week} Week")
print(f"{remaining_days} Days")