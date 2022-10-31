# Solve the equation ax2 + bx + c = 0, where a, b and c are real numbers and a ≠ 0.

# input for a , b and c
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))


# formula for the equation
x1 = (-b+((b**2) - (4*a*c))**0.5)/(2*a)  
x2 = (-b-((b**2) - (4*a*c))**0.5)/(2*a)  

# output
print('The values are: ' , x1 , x2)
