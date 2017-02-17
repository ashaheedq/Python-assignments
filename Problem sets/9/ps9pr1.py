def count_ignore_case(s, sub):
    """takes a string s and a substring sub, and that uses one or more string methods
        to compute and return the number of occurrences of sub in s,
        but in a way that ignores the cases of the letters involved
    """
    new_sub = sub.upper()
    new_s = s.upper()
    num_sub = new_s.count(new_sub)
    return num_sub

count_ignore_case('Yes, yes, YES!', 'yEs')

def middle_name(fullname):
    """takes a string fullname that represents a person’s full name, and that uses
    string methods to extract and return a string representing the person’s middle name
    """

    mid_name = fullname.split()
    length = len(mid_name)
    mid_name = mid_name[1]

    if length >= 3:
        return mid_name
    else:
        return ''
