# bank.py
# Author: Niall Wynne
# Week 2 problem

number1 = int(input('Enter first amount in cent: '))
print(f'Amount = {number1}')

number2 = int(input('Enter second amount in cent: '))
print(f'Amount = {number2}')

total = number1/100 + number2/100    

# print(f'The sum of these is {total}')

# print('The sum of these is €2.45') Initial attempt.

# Left in the code from my initial attempts so I could see the difference.

txt = "The sum of these is €{:.2f}"
print(txt.format(total))


# added the last two lines after finishing the lab and following the link to the Python tutorial.

