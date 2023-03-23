# plottask.py
# author - Niall Wynne
# Week 08 Task
# A program that displays 
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range [0, 10]

# Have to import modules to use
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 2.0, 1000) # normal distribution from numpy 
                    #mean value 5, standard deviation of 2, 1000 values

xpoints = np.array(range(0, 10))
ypoints = xpoints * xpoints * xpoints # x cubed - multiply by itself 3 times

plt.plot(xpoints, ypoints, label = 'X Cubed', color = 'green') #plots the line of the points above, can add label and color.
plt.title('Weekly Task - 08') #adds a title
plt.xlabel('X Values') #labels the x axis, wasn't sure what to call it
plt.ylabel ('Y Values') #labels the y axis
plt.legend() #adds the legend to display the label
plt.hist(x, color = 'orange')
plt.show()