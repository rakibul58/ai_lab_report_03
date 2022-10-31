# Find the area of Sector

# input for the angle and area
theta = float(input('Enter the the angle: '))
r = float(input('Enter Radius: '))

# formula for sector
area = (3.1416 * r**2) * (theta/360)

# output
print("Area is %0.2f" %area)