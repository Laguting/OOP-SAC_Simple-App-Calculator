# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Turn the Simple App Calculator program into OOP.

from calculator_intros import calc_interface
from user_interface import Interface
from retry import Retry
from change_brand import Brand

class Calculator():
# Call calculator_intros for the brand, welcome, and loading features
    ci_2 = Brand()
    print(ci_2.change_bd()) # Display the brand of the calculator
    ci_1 = calc_interface("","","")
    print(ci_1.show_welcome()) # Welcome the user
    print(ci_1.loading_bar()) # Loading Bar
# Display the question for operations, and numbers as well as the result of the inputted datas
    perf_calc = Interface("", "")
    print(perf_calc.process()) # add, subtract, multiply, divide display
# Ask the user if the user want to try again
    re_1 = Retry("")
    print(re_1.re_try())