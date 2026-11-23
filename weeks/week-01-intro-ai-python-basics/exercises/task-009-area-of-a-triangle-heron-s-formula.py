"""Task 9: Area of a triangle (Heron's formula) (Week 1)."""

# Find the area of a triangle (Heron's formula)
a = 5
b = 6
c = 7
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

s = (a + b + c) / 2  # semi-perimeter
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
