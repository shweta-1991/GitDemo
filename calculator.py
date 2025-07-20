class BasicCalculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        return "Addition: {} + {} = {}".format(self.num1, self.num2, self.num1 + self.num2)

    def subtraction(self):
        return "Subtraction: {} - {} = {}".format(self.num1, self.num2, self.num1 - self.num2)
    def multiplication(self):
        return "Multiplication: {} * {} = {}".format(self.num1, self.num2, self.num1 * self.num2)
    def division(self):
        return "Division: {} / {} = {}".format(self.num1, self.num2, self.num1 / self.num2)


obj=BasicCalculator(10,5)
print(obj.addition())
print(obj.subtraction())
print(obj.multiplication())
print(obj.division())

