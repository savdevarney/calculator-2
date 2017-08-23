"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input_string = raw_input(">")
    t_input = input_string.split(" ")
    if t_input[0] == "q":
        print "You are now exiting!"
        break

    else:
        opp = t_input[0]
        if opp == "+":
            print add(int(t_input[1]), int(t_input[2]))
        elif opp == "-":
            print subtract(int(t_input[1]), int(t_input[2]))
        elif opp == "*":
            print multiply(int(t_input[1]), int(t_input[2]))




# Your code goes here
