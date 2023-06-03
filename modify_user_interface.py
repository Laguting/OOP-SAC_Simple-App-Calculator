from user_interface import Interface
from calculator_intros import calc_interface
ci_1 = calc_interface("","","")
class modified_interface(Interface):
    def __init__(self, result, in_process):
        self.result = result
        self.in_process = in_process
    def modified_process(self):
        with open("calc_history.text", "w") as calculatorhistory_file: # Open text file that will hold the history of inputs
            while True:
                from modify_perform_calculation import Modified_operations
                self.calculator = Modified_operations()
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
                    print()
                    number_1 = float(input("\n\33[43m1st number:\33[0m"))
                    number_2 = float(input("\n\33[43m2nd number:\33[0m"))
                    number_3 = float(input("\n\33[43m3nd number:\33[0m"))
                    print(ci_1.loading_bar())
                except ValueError:
                    print("\n\33[1m\33[31mThis calculator only accepts numbers\33[0m") 
                    continue
        # Add
                if ask_usr == "+":
                    result = self.calculator.addition(number_1,number_2,number_3)
                    self.print_result(f"\33[7m The result of inputting '{number_1} {ask_usr} {number_2} {ask_usr} {number_3}' is {result}\33[0m")
                    calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} {ask_usr} {number_3} = {result}" + '\n')
                    break
        # Subtract
                elif ask_usr == "-":
                    result = self.calculator.subtract(number_1,number_2,number_3)
                    self.print_result(f"\33[7m The result of inputting '{number_1} {ask_usr} {number_2} {ask_usr} {number_3}' is {result}\33[0m")
                    calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} {ask_usr} {number_3}= {result}" + '\n')
                    break
        # Multiply
                elif ask_usr == "*":
                    result = self.calculator.multiply(number_1,number_2,number_3)
                    self.print_result(f"\33[7m The result of inputting '{number_1} {ask_usr} {number_2}' is {result}\33[0m")
                    calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} {ask_usr} {number_3} = {result}" + '\n')
                    break
        # Divide
                else:
                    try:
                        ask_usr == "/"
                        result = self.calculator.divide(number_1,number_2, number_3)
                        self.print_result(f"\33[7m The result of inputting '{number_1} {ask_usr} {number_2} {ask_usr} {number_3}' is {result}\33[0m")
                        calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} {ask_usr} {number_3} = {result}" + '\n')
                        break
                    except ZeroDivisionError:
                         print("\n\33[1m\33[31mYou can't use zero(0) as your divisor\33[0m")
                break
        return self.in_process
# Print result
    def print_result(self,result):
        print(result)
        return self.result