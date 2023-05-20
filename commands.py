# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Turn the Simple App Calculator program into OOP.
from calculator_interface import calc_interface
ci_1 = calc_interface("","")
# Display the brand of the calculator
print(ci_1.get_brand())
# Welcome the user
print(ci_1.show_welcome())
# Print the inputted numbers and operations
# store the inputs in calc_history text file