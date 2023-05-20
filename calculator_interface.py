from pyfiglet import Figlet
from termcolor import colored
class calc_interface():
    def __init__(self, brand, welcome):
        self.brand = brand
        self.welcome = welcome
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
    def show_welcome(self):
        s_a_c = Figlet(font = "starwars", justify = "right")
        print()
        print(colored(s_a_c.renderText("            W e l c o m e              "), "green"))
        print("\33[35m                                                                ┻┳|              \33[0m")
        print("\33[35m                                                                ┳┻| _\33[0m")
        print("\33[35m                                                                ┻┳|•.•) i'm watching.....\33[0m")
        print("\33[35m                                                                ┳┻|  ⊂ﾉ)\33[0m")
        print("\33[35m                                                                ┻┳|\33[0m")
        print()
        print("⚜ " * 89)
        print()
        return self.welcome
# Loading Bar