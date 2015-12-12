# Python3.4
# calc.py

"""
This library takes 2 parameters and performs a mathematical operation
and returns the result to the caller
"""


class Calc():
    """
    class with mathematical operations
    """

    def __init__(self, arg1, arg2):
        """ Initialize the values
        :param arg1:
        :param arg2:
        """
        self.num1 = arg1
        self.num2 = arg2

    def add(self):
        """ addition operation
        :return: addition of input values
        """
        return self.num1 + self.num2

    def subtract(self):
        """ subtraction operation
        :return: difference of input values
        """
        return self.num1 - self.num2

    def multiply(self):
        """ multiplication operation
        :return: multiplication of input values
        """
        return self.num1 * self.num2

    def divide(self):
        """ division operation
        :return: division of input values
        """
        return self.num1 / self.num2


if __name__ == "__main__":
    myCalc = Calc(1, 2)
    result1 = myCalc.add()
    result2 = myCalc.subtract()
    result3 = myCalc.multiply()
    result4 = myCalc.divide()

    print(result1, result2, result3, result4)
