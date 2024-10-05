 # Jasmine Schildt
 # 10/5/2024
 # P2LAB1
 # An assignment that calculates the radius, diameter, circumference, and area of a circle.

radius = int(input('What is the radius of the circle? '))
print(' ')

diameter = 2 * radius
circumference = 2 * 3.141592653589793 * radius
area = 3.141592653589793 * (radius**2)

print('The diameter of the circle is', end=' ')
print(f'{diameter:.1f}')
print(' ')

print('The circumference of the circle is', end=' ')
print(f'{circumference:.2f}')
print(' ')

print('The area of the circle is', end=' ')
print(f'{circumference:.3f}')
