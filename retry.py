from pyfiglet import Figlet
from termcolor import colored
from user_interface import Interface
perf_calc = Interface("", "")
from calculator_intros import calc_interface
ci_1 = calc_interface("","","")
# Allow the user to retry
class Retry():
    def __init__(self, retry):
        self.retry = retry
    def re_try(self):
        keep_going = True
        while keep_going:
        # ask if they wanted to continue
            again_usr = input("\n\33[36m Would you like to try again: Enter 'Y' if yes and 'N' if no: \33[0m")
                # If yes call process
            if again_usr.upper() == "Y":
               print(ci_1.loading_bar())
               perf_calc.process()
            # If no, Display "Thank you" and exit 
            else:
                try:
                    exit_1 = Figlet(font = "slant")
                    print()
                    print(colored(exit_1.renderText("                        Thank you! <3"), "magenta"))
                    print("\n\33[3m\33[1m                                                                 Until next time!... '૮₍ •⤙ •˶|\33[0m")
                    print("⚜ " * 89)
                    print()
                    keep_going = False
                    if again_usr.upper() not in ["N"]:
                        raise ValueError
                except ValueError:
                    print("\n\33[1m\33[31mInvalid Operation. Try again.\33[0m\n")
                    continue 
        return self.retry