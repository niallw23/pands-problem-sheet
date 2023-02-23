# weekday.py
# Author - Niall Wynne
# The program should output whether or not today is a weekday

#Need to import module
import datetime

weeknum = datetime.datetime.today().weekday()


if weeknum < 5:
    print ('Today is a weekday')

else:
    print ('It is the weekend')