# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions with numeric inputs
#
# name: abdulshaheed alqunber   
# email: asq@bu.edu

#function 1
def mirror(s):
    """takes a string s and returns the original
    and a mirrored version of it"""
    mirrored = s[-1::-1]
    return s + mirrored

#function 2
def is_mirror(s):
    """takes a string and determine if its a mirrored or not"""
    length = len(s)
    original = length // 2
    word = s[:original]
    mirrored = mirror(word)
    return mirrored == s 
    
#function 3
def replace_end(values, new_end_vals):
    """takes a list "values" and another list "new_end_vals" and replaces the last x elements
    of the list "values", x = length of the second input"""
    x = len(values) 
    y = len(new_end_vals)
    if x <= y:
        return new_end_vals
    else: 
        mod_values = values[:y-1]
        new_list = mod_values + new_end_vals
        return new_list

#function 4
def repeat_elem(values, index, num_times):
    """takes a list "value" and integer "index" and a positive integer "num_times
    which returns a new list in which element at "index" repeated "num_times" times"""
    element = [values[index]]
    repeated = element * num_times
    last = values[(index+1): ]
    first = values[:index]
    new = first + repeated + last
    return new


# sample test call for functions
print("mirror(s) returns", mirror("shaheed"))

print("is_mirror(s) returns", is_mirror("aliila"))

print("replace_end(values, new_end_vals) returns", replace_end([3, 5, 7, 9, 11], [13, 17, 19]))

print("repeat_elem(values, index, num_times) returns", repeat_elem([3, 5, 7, 9, 11], 2, 5))
