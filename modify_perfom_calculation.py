from perform_calculations import Operations
# Perform the calculations
class Modified_operations(Operations):
    def addition(self, number_1, number_2, number_3): # add
        sum = number_1 + number_2 + number_3
        return sum
    def subtract(self, number_1, number_2, number_3): # subtract
        minus = number_1 - number_2 - number_3
        return minus
    def multiply(self, number_1, number_2, number_3): # multiply
        product = number_1 * number_2 * number_3
        return product
    def divide(self, number_1, number_2, number_3): # divide
        quotient = number_1 / number_2 / number_3
        return quotient