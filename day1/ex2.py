temp_in_cel = float(input("Enter Temperature in celsius: "))

temp_in_fah = (9/5 * temp_in_cel) +32
# formatted = round(temp_in_fah, 2)
formatted = f"{temp_in_fah:.2f}"


print(formatted)