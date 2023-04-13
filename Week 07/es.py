# Week 07 Task
# Author - Niall Wynne
# A program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.


import sys  # looked up when researching command line

arg = sys.argv[1] # skipping the python file name
'''
if arg == 'note.txt': # assuming file name is known and can be input into command line
    def letterFrequency(fileName, letter):
        file = open(fileName, 'r')
        text = file.read()
        return text.count(letter)
'''
# following feedback, tried to use 'with' statement instead of file = open()
# never closed file in above attempt
# the reading on with statements in the Real Python explained this further

def letterFrequency(fileName, letter):  #still making same assumption around file name
    with open(fileName, 'r') as file:
        text = file.read()
        return text.count(letter)


# call the function and display the letter count
print(letterFrequency('note.txt', 'e'))