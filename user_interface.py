class Interface():
# Ask for the operation to perform.
# Ask the user for the numbers to perform calculations
    def process(self):
        with open("calc_history.text", "w") as calculatorhistory_file: # Open text file that will hold the history of inputs
            while True:
                try:
                    ask_usr = input("\n\33[1m\33[34m What operation would you like to perform? Enter Add = '+'; Subtraction = '-'; Multiplication = '*'; Division = '/': \33[0m")
                    if ask_usr not in ["+", "-", "*", "/"]:
                        raise ValueError
                except ValueError:
                    print("\n\33[1m\33[31mInvalid Operation. Try again.\33[0m")
                    continue