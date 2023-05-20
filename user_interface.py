class usr_intrfc():
    def __init__(self, operation, input):
        self.operation = operation
        self.input = input
# Ask for the user's initial inputs
    def usr_operation(self):   # Ask for operations
        try:
            ask_usr = input("\n\33[1m\33[34m What operation would you like to perform? Enter Add = '+'; Subtraction = '-'; Multiplication = '*'; Division = '/': \33[0m")
            if ask_usr not in ["+", "-", "*", "/"]:
                raise ValueError
        except ValueError:
             print("\n\33[1m\33[31mInvalid Operation. Try again.\33[0m")
        return self.operation
    def usr_input(self):
        try:
            number_1 = float(input("\n\33[43m1st number: \33[0m"))
            number_2 = float(input("\n\33[43m2nd number: \33[0m"))
            print()
        except ValueError:
            print("\n\33[1m\33[31mThis calculator only accepts numbers\33[0m") 
        return self.input
# Ask if they want to continue
