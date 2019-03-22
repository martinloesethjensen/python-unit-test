""" Calculater class that can add, subtrack, multiply and devide """


# https://stackify.com/unit-testing-basics-best-practices/

class Calculater:
    """ init takes 0 arguments """

    def __init__(self):
        # you should here create two instance variables
        # total and error_msg

        self.total = 0
        self.error_msg = ''

    def add(self, num) -> [int, float]:
        """ Add takes 1 argument an 'int' or 'float',
            the number to add to 'total' """

        if Calculater.check_int_or_float(num):
            self.total += num

        else:
            self.check_type(input_type=type(num))

    def subtract(self, num):
        if Calculater.check_int_or_float(num):
            self.total -= num

        else:
            self.check_type(input_type=type(num))

    def multiply(self, num):
        if Calculater.check_int_or_float(num):
            self.total *= num

        else:
            self.check_type(input_type=type(num))

    def divide(self, num):
        if Calculater.check_int_or_float(num):
            self.total /= num

        else:
            self.check_type(input_type=type(num))

    @staticmethod
    def check_int_or_float(number):
        return type(number) in [int, float]

    def check_type(self, input_type: type):
        if input_type is bool:
            self.error_msg = "Number can not be a boolean"
            raise TypeError("Number can not be a boolean")
        elif input_type is str:
            self.error_msg = "Number can not be a string"
            raise TypeError("Number can not be a string")
        else:
            self.error_msg = "Unknown type"
            raise TypeError("Unknown type")

    def __str__(self) -> str:
        """ Returns 'total' or 'Error message' """

        if self.error_msg != '':
            self.temp = self.error_msg
            self.error_msg = ''
            return self.temp

        return str(self.total)

    def display(self):
        """ Returns 'total' or 'Error message' """

        return str(self.total)

    def __repr__(self) -> str:
        return super().__repr__()
