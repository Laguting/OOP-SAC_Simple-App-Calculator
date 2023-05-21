class Interface():
    def __init__(self, result, in_process):
        self.result = result
        self.in_process = in_process
    def process(self):
        with open("calc_history.text", "w") as calculatorhistory_file: # Open text file that will hold the history of inputs
            while True:
                from perform_calculations import Operations
                self.calculator = Operations()
# Ask for the operation to perform.   
                try:
                    ask_usr = input("\n\33[1m\33[34m What operation would you like to perform? Enter Add = '+'; Subtraction = '-'; Multiplication = '*'; Division = '/': \33[0m")
                    if ask_usr not in ["+", "-", "*", "/"]:
                        raise ValueError
                except ValueError:
                    print("\n\33[1m\33[31mInvalid Operation. Try again.\33[0m")
                    continue
# Ask the user for the numbers to perform calculations
                try:
                    number_1 = float(input("\n\33[43m1st number: \33[0m"))
                    number_2 = float(input("\n\33[43m2nd number: \33[0m"))
                    print()
                except ValueError:
                    print("\n\33[1m\33[31mThis calculator only accepts numbers\33[0m") 
                    continue
                if ask_usr == "+":
                    result = self.calculator.addition(number_1,number_2)
                    self.print_result(result)
                    break
                elif ask_usr == "-":
                    result = self.calculator.subtract(number_1,number_2)
                    self.print_result(result)
                    break
                calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} = {result}" + '\n')
                return self.in_process
# Print result
    def print_result(self,result):
        print(f"\n\33[7m {result}\33[0m")
        return self.result