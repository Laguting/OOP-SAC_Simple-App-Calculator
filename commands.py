# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Turn the Simple App Calculator program into OOP.

from calculator_interface import calc_interface #calculator interface

ci_1 = calc_interface("","","")
print(ci_1.get_brand()) # Display the brand of the calculator
print(ci_1.show_welcome()) # Welcome the user
print(ci_1.loading_bar()) # Loading Bar

from user_interface import usr_intrfc
from user_interface import numbers
ui_1 = usr_intrfc("","")
ui_2 = numbers("","")
# Ask for the user's input
print(ui_1.usr_operation())
print(ui_2.usr_one())
print(ui_2.usr_two())
# Print the inputted numbers and operations
# store the inputs in calc_history text file