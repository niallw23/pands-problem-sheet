# sqrt.py
# Author - Niall Wynne
# A program that takes a positive floating-point number as input 
# and outputs an approximation of its square root.
# Need to create a function
# Week 6 Task

num = float(input('Enter a positive floating point number:'))

# reference in readme
def sqrt(num):
    approx = num * 0.5
    better = 0.5 * (approx + num / approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + num /approx)
    return approx

print (f'The square root of {num} is approx. {sqrt(num)}')

