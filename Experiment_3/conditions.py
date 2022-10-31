"""
Some operators check the relationship between two values, called relational operators.
Given two numerical
values, your job is just to find out the relationship between them that is (i)
First one is greater than the second (ii) the first one is less than the second or
(iii) First and the second one is equal.

# Input
The first line of the input file is an integer t (t < 15) which denotes how many
sets of inputs are there. Each of the following t lines contains two integers a and
b (|a|, |b| < 1000000001).

# Output
For each line of input produce one line of output. This line contains any
one of the relational operators ‘>’, ‘<’ or ‘=’, which indicates the relation
that is appropriate for the given two numbers
"""

t = int(input('Enter a number from 1 to 15: '))

# loop 
for x in range(t):
    # input 
    num1 = int(input('Enter number one: '))
    num2 = int(input('Enter number two: '))
    # conditions 
    if num1 == num2:
        print('\n=\n')
    elif num1>num2:
        print('\n>\n')
    else:
        print('\n<\n')