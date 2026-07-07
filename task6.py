# All Formula Expressions in One Program

# Input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
side = float(input("Enter side: "))
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

weight = float(input("Enter weight (kg): "))
body_height = float(input("Enter height (m): "))

# Arithmetic
print("\nArithmetic Operations")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Floor Division =", a // b)
print("Power =", a ** b)

# Average
average = (a + b + c) / 3
print("\nAverage =", average)

# Rectangle
area_rectangle = length * breadth
perimeter_rectangle = 2 * (length + breadth)

print("\nRectangle")
print("Area =", area_rectangle)
print("Perimeter =", perimeter_rectangle)

# Square
area_square = side * side
perimeter_square = 4 * side

print("\nSquare")
print("Area =", area_square)
print("Perimeter =", perimeter_square)

# Circle
area_circle = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("\nCircle")
print("Area =", area_circle)
print("Circumference =", circumference)

# Triangle
area_triangle = 0.5 * breadth * height
print("\nTriangle Area =", area_triangle)

# Cube
volume_cube = side ** 3
print("Volume of Cube =", volume_cube)

# Cuboid
volume_cuboid = length * breadth * height
print("Volume of Cuboid =", volume_cuboid)

# Cylinder
volume_cylinder = 3.14 * radius * radius * height
print("Volume of Cylinder =", volume_cylinder)

# Simple Interest
SI = (principal * rate * time) / 100
print("\nSimple Interest =", SI)

# Compound Interest
amount = principal * (1 + rate / 100) ** time
CI = amount - principal
print("Compound Interest =", CI)

# Temperature Conversion
fahrenheit = (height * 9 / 5) + 32
celsius = (fahrenheit - 32) * 5 / 9

print("\nTemperature")
print("Celsius to Fahrenheit =", fahrenheit)
print("Fahrenheit to Celsius =", celsius)

# BMI
BMI = weight / (body_height ** 2)
print("\nBMI =", BMI)

# Percentage (Example: marks out of 3 subjects)
total = a + b + c
percentage = (total / 300) * 100

print("\nTotal Marks =", total)
print("Percentage =", percentage)