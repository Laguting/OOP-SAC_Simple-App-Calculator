# Import calculator_intros
from pyfiglet import Figlet
from termcolor import colored
class Brand():
    def __init__(self, brand):
        self.brand = brand
    def change_bd(self):
        s_a_c = Figlet(font = "digital", justify = "right")
        print()
        print("⚜ " * 89)
        print()
        print(colored(s_a_c.renderText("                                                            ======= AETH3R ======="), "red"))
        return self.brand