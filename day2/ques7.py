#calculate the area and circumference of circle

# area = pi r^2
# circumference = 2(pi)r
import math

radius = float(input('Enter radius of circle: '))

area = math.pi * (radius**2)
circumference = 2*(math.pi*radius)

print(f'Area of circle is {area}')
print(f'circumference of circle is {circumference}')