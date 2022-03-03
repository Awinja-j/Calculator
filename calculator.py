class calculate:
    def __init__(self, x, y, function_name) -> None:
        self.x = x
        self.y = y
        self.function_name = function_name

    # This function adds two numbers
    def add(self):
        return self.x + self.y

    # This function subtracts two numbers
    def subtract(self):
        return self.x - self.y

    # This function multiplies two numbers
    def multiply(self):
        return self.x * self.y

    # This function divides two numbers
    def divide(self):
        return self.x / self.y

    # This fucntion gets the power of two numbers
    def power(self):
        return self.x ** self.y

    # This function takes in a function name and calls the function
    def calculate_function(self):
        if self.function_name == "add":
            return self.add()
        elif self.function_name == "subtract":
            return self.subtract()
        elif self.function_name == "multiply":
            return self.multiply()
        elif self.function_name == "divide":
            return self.divide()
        elif self.function_name == "power":
            return self.power()
        else:
            return "Invalid function name"

# f = calculate(2, 3, "add")
# print(f.calculate_function())