from pyfiglet import Figlet
from termcolor import colored
class calc_interface():
# Brand of the Calculator
    def __init__(self, brand):
        self.brand = brand
    def get_brand(self):
        s_a_c = Figlet(font = "digital", justify = "right")
        print()
        print("⚜ " * 89)
        print()
        print(colored(s_a_c.renderText("                                                       Simple App Calculator"), "yellow"))
        return self.brand
# Welcome the user
# Loading Bar