class usr_intrfc():
    def __init__(self, input):
        self.input = input
# Ask for the user's initial inputs
    def usr_input(self):
        try:
            ask_usr = input("\n\33[1m\33[34m What operation would you like to perform? Enter Add = '+'; Subtraction = '-'; Multiplication = '*'; Division = '/': \33[0m")
            if ask_usr not in ["+", "-", "*", "/"]:
                raise ValueError
        except ValueError:
             print("\n\33[1m\33[31mInvalid Operation. Try again.\33[0m")
        return self.input
# Ask if they want to continue
