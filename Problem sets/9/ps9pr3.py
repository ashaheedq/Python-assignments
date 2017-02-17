## Abdulshaheed Alqunber
## ps9pr3
from ps9pr2 import Date

def get_age_on(birthday, other):
    """takes two Date objects as parameters: one to represent
    a person’s birthday, and one to represent an arbitrary date
    then return the person’s age on that date as an integer
    """

    if birthday.__eq__(other) == True:
        return 1
    else:
        years = birthday.diff(other) // 365
        return years

def print_birthdays(filename):
    """takes a string filename as a parameter. The function should then open
    the file that corresponds to that filename, read through the file,
    and print some information derived from that file
    """
    file = open(filename, 'r')
    for line in file:
        line = line[:-1]
        elems = line.split(',')
        bday = int(elems[1])
        bmonth= int(elems[2])
        byear = int(elems[3])
        bdate = Date(bday, bmonth, byear)
        print(elems[0], '(' + str(bdate) + ')', '(' + str(bdate.day_of_week()) + ')', end='\n')

    file.close()
