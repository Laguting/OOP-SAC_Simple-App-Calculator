# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Turn the Simple App Calculator program into OOP.

# Call calculator_intros for the brand, welcome, and loading features
from calculator_intros import calc_interface
ci_1 = calc_interface("","","")
# Display the brand of the calculator
print(ci_1.get_brand())
# Welcome the user
print(ci_1.show_welcome())
# Loading Bar
print(ci_1.loading_bar())