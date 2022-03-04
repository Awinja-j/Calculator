class calculate:
    def __init__(self, x, function_name, y) -> None:
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

    # This function takes in a function name and calls the function
    def calculate_function(self):
        if self.function_name == "+":
            return self.add()
        elif self.function_name == "-":
            return self.subtract()
        elif self.function_name == "*":
            return self.multiply()
        elif self.function_name == "/":
            return self.divide()
        else:
            return "Invalid function name"
