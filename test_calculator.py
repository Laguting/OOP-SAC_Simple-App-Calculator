# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Turn the Simple App Calculator program into OOP.

from calculator_intros import calc_interface
from user_interface import Interface

class Calculator():
# Call calculator_intros for the brand, welcome, and loading features
    ci_1 = calc_interface("","","")
    print(ci_1.get_brand()) # Display the brand of the calculator
    print(ci_1.show_welcome()) # Welcome the user
    print(ci_1.loading_bar()) # Loading Bar
# Display the result of the equations
    perf_calc = Interface()
    print(perf_calc.process())# add
# subtract
# multiply
# divide
# Store the inputs in calc_history text file