# • Find the area of the triangle.

# Input sides of the triangle
a = float(input("Enter a side of a triangle: "))
b = float(input("Enter the other side of a triangle: "))
c = float(input("Enter the last side of a triangle: "))

# Formula for the area of the triangle
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

# Output 
print('Area of the triangle is %0.2f' %area)