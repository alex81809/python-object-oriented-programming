# Expression: creating class 
class Expression: 
    # Constructor: initializing the instance attributes
    def __init__(number, num1, num2, num3): 
        number.num1 = num1 
        number.num2 = num2 
        number.num3 = num3 
    
    # Method: calculating addition and printing result
    def calculate_addition(number): 
        result = number.num1 + number.num2 + number.num3 
        print(f"The addition of {number.num1}, {number.num2}, and {number.num3} is {result}")

# Object: creation and method implementation
expr1 = Expression(5, 10, 15)
expr1.calculate_addition()
