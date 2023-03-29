# accounts.py
# Weekly Task 3
# Author - Niall Wynne
# Writing a program that reads in a 10 character account number and 
# outputs the account number with only the last 4 digits showing.

#accountno = input('Please enter a 10 digit account number: ')

#print ('xxxxxx' + accountno [6:10])  #W3 Schools and Lecture

# need to try extra part next

accountno = input('Please enter an account number: ') #not specifying account number length

print ('x' * (len(accountno) - 4) + accountno[-4:]) # x's calculated as length of account -4 so we can show the last 4 digits

# used the string slicing help on W3 schools to change the last part to allow for change in length of account number


